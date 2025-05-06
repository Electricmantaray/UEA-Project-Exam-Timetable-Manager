--------------- SCHEMA CREATION ---------------
CREATE SCHEMA IF NOT EXISTS Coursework;
SET search_path TO Coursework, public;
-----------------------------------------------


--------------- TABLE CREATION ---------------
-- Exam table, stores exam details
CREATE TABLE IF NOT EXISTS exam (
    excode CHAR(4) PRIMARY KEY,
    extitle VARCHAR(200) UNIQUE NOT NULL,
    exlocation VARCHAR(200) NOT NULL,
    exdate DATE NOT NULL CHECK (exdate BETWEEN '2025-11-01' AND '2025-11-30'),
    extime TIME NOT NULL CHECK (extime BETWEEN '09:00' AND '18:00')
);

-- Student table, stores individual student detials
CREATE TABLE IF NOT EXISTS student (
    sno INTEGER PRIMARY KEY,
    sname VARCHAR(200) NOT NULL,
    semail VARCHAR(200) UNIQUE NOT NULL
);

-- Entry table, links students to exams, storing their grade
CREATE TABLE IF NOT EXISTS entry (
    eno INTEGER PRIMARY KEY,
    excode CHAR(4) NOT NULL,
    sno INTEGER NOT NULL,
    egrade DECIMAL(5,2) CHECK (egrade BETWEEN 0 AND 100),
    CONSTRAINT fk_entry_exam FOREIGN KEY (excode) REFERENCES exam(excode) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_entry_student FOREIGN KEY (sno) REFERENCES student(sno) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Cancel table, stores cancelled enteries
CREATE TABLE IF NOT EXISTS cancel (
    eno INTEGER PRIMARY KEY,
    excode CHAR(4) NOT NULL,
    sno INTEGER NOT NULL,
    cdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cuser VARCHAR(200) NOT NULL
);

----------------------------------------------


------------------- INDEXES -------------------

-- Indexes to optimise common queries
CREATE INDEX IF NOT EXISTS index_exam_code ON exam(excode);
CREATE INDEX IF NOT EXISTS index_student_number ON student(sno);
CREATE INDEX IF NOT EXISTS index_entry_number ON entry(eno);
CREATE INDEX IF NOT EXISTS index_exam_date ON exam(exdate);
-- Useful for filtering by

-----------------------------------------------


------------ FUNCTIONS / TRIGGER ------------

-- Triggers Functions --

-- Enforce: A student cannot register for multiple exams on the same day
CREATE OR REPLACE FUNCTION check_exam_day_limit()
RETURNS trigger AS $enforce_exam_day_limit$
    DECLARE
        exam_date DATE;

    BEGIN
        -- Allows exception to specify registered date
        SELECT exdate INTO exam_date FROM exam WHERE excode = NEW.excode;

        -- Searches entry to see if student number is present,
        -- and if the date of the new exam is the same as the regestered entry
        IF EXISTS (
            SELECT 1 FROM entry
            INNER JOIN exam ON entry.excode = exam.excode
            WHERE entry.sno = NEW.sno AND exam.exdate = exam_date
        ) 

        Then 
            RAISE EXCEPTION 
            'Student: % is already registered for an exam (%) on that date: %',
            NEW.sno, NEW.excode, exam_date;
        END IF;

        RETURN NEW;

    END;
$enforce_exam_day_limit$ LANGUAGE PLPGSQL;

CREATE OR REPLACE TRIGGER enforce_exam_day_limit BEFORE INSERT ON entry
    FOR EACH ROW EXECUTE FUNCTION check_exam_day_limit();


-- Enforce: A student cannot take the same exam more than once in a year
CREATE OR REPLACE FUNCTION check_exam_attempt_limit()
RETURNS trigger AS $enforce_exam_attempt_limit$
    DECLARE
        exam_year INT;

    BEGIN
        -- Allows exception to specify registered date
        SELECT date_part('year', exdate) INTO exam_year FROM exam WHERE excode = NEW.excode;


        -- Searches entry to see if student number is present,
        -- if the same exam is entered twice in the same year it raises exceptions
        IF EXISTS(
            SELECT 1 FROM entry
            INNER JOIN exam ON entry.excode = exam.excode
            WHERE entry.sno = NEW.sno 
                AND entry.excode = NEW.excode
                AND date_part('year', exam.exdate) = exam_year
        )

        Then 
            RAISE EXCEPTION 
            'Student: % already has exam (%) this year',
            NEW.sno, NEW.excode;
        END IF;

        RETURN NEW;

    END;
$enforce_exam_attempt_limit$ LANGUAGE PLPGSQL;


CREATE OR REPLACE TRIGGER enforce_exam_attempt_limit BEFORE INSERT ON entry
    FOR EACH ROW EXECUTE FUNCTION check_exam_attempt_limit();


-- Automatically records cancelled entries into cancel table
CREATE OR REPLACE FUNCTION autofill_cancel_table()
RETURNS trigger AS $autofill_cancel_table$
    BEGIN

        -- Inserts deleted data into cancel table to retain integrity
        INSERT INTO cancel(eno, excode, sno, cdate, cuser) VALUES
            (OLD.eno, OLD.excode, OLD.sno, NOW(), COALESCE(current_user, 'System user'));

        RETURN NULL;

    END;
$autofill_cancel_table$ LANGUAGE PLPGSQL;

CREATE OR REPLACE TRIGGER autofill_cancel_table AFTER DELETE ON entry
    FOR EACH ROW EXECUTE FUNCTION autofill_cancel_table();

-----------------------------------------------


-------------------- VIEWS --------------------

-- Student Timeable
-- View: Timetable for each student with registered exams 
CREATE OR REPLACE VIEW student_timetable AS
SELECT student.sno, student.sname, exam.excode, exam.extitle, exam.exlocation, exam.exdate, exam.extime 
FROM exam
INNER JOIN entry ON exam.excode = entry.excode
INNER JOIN student ON entry.sno = student.sno
ORDER BY exdate, extime;

-- Exam Results (Distinction/Pass/Fail)
-- View: Results for exams, including grade outcome
CREATE OR REPLACE VIEW exam_results AS
SELECT exam.excode, student.sname, exam.extitle,
CASE
	WHEN egrade >= 70.00 THEN 'Distinction'
	WHEN egrade >= 50.00 THEN 'Pass'
	WHEN egrade < 50.00 THEN 'Fail'
	WHEN egrade is NULL THEN 'Not taken'
END AS result
FROM exam
INNER JOIN entry ON exam.excode = entry.excode
INNER JOIN student ON entry.sno = student.sno
ORDER BY excode, sname

-----------------------------------------------


----------- TRANSACTIONS OF INTEREST -----------
/*
-- A
INSERT INTO student VALUES
	(11, 'Transaction Student', 'tstudent@example.edu');

-- B
INSERT INTO exam VALUES
	('TB01', 'Transaction B', 'Online exam', '2025-11-29', '12:15');

-- C
BEGIN TRANSACTION;

DELETE FROM student
WHERE sno = 1;

COMMIT;

-- D
BEGIN TRANSACTION;

DELETE FROM exam
WHERE excode = 'DB03';

COMMIT;

-- E
INSERT INTO entry VALUES
	(11, 'AI02', 10, NULL);

-- F
UPDATE entry
SET egrade = 75.00
WHERE eno = 11;

-- G
SELECT sname, excode, extitle, exlocation, exdate, extime FROM student_timetable
WHERE sno = 10;

-- H
SELECT * FROM exam_results;

-- I
SELECT * FROM exam_results
WHERE excode = 'DB01';
*/
-----------------------------------------------
