-- COURSEWORK --

--------------- SCHEMA CREATION ---------------
CREATE SCHEMA IF NOT EXISTS Coursework;
SET search_path TO Coursework, public;
-----------------------------------------------


--------------- TABLE CREATION ---------------
-- Create exam table
CREATE TABLE IF NOT EXISTS exam (
    excode CHAR(4) PRIMARY KEY,
    extitle VARCHAR(200) UNIQUE NOT NULL,
    exlocation VARCHAR(200) NOT NULL,
    exdate DATE NOT NULL CHECK (exdate BETWEEN '2025-11-01' AND '2025-11-30'),
    extime TIME NOT NULL CHECK (extime BETWEEN '09:00' AND '18:00')
);

-- Create student table
CREATE TABLE IF NOT EXISTS student (
    sno INTEGER PRIMARY KEY,
    sname VARCHAR(200) NOT NULL,
    semail VARCHAR(200) UNIQUE NOT NULL
);

-- Create entry table
CREATE TABLE IF NOT EXISTS entry (
    eno INTEGER PRIMARY KEY,
    excode CHAR(4) NOT NULL,
    sno INTEGER NOT NULL,
    egrade DECIMAL(5,2) CHECK (egrade BETWEEN 0 AND 100),
    CONSTRAINT fk_entry_exam FOREIGN KEY (excode) REFERENCES exam(excode) ON DELETE CASCADE,
    CONSTRAINT fk_entry_student FOREIGN KEY (sno) REFERENCES student(sno) ON DELETE CASCADE
);

-- Create cancel table
CREATE TABLE IF NOT EXISTS cancel (
    eno INTEGER PRIMARY KEY,
    excode CHAR(4) NOT NULL,
    sno INTEGER NOT NULL,
    cdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cuser VARCHAR(200) NOT NULL
);

----------------------------------------------


------------------- INDEXES -------------------

-- Primary keys indexed as they're often used im WHEN statements
-- excode
CREATE INDEX index_exam_code ON exam(excode);

-- sno
CREATE INDEX index_student_number ON student(sno));

-- eno
CREATE INDEX index_entry_number ON entry(eno);

-- exdate
-- Frequently filtered for, index used to speed up process
CREATE INDEX index_exam_date ON exam(exdate);

-----------------------------------------------


------------ FUNCTIONS / TRIGGER ------------

-- Functions --


-- Triggers Functions --

-- Preventing entry into multiple exams on the same day
CREATE OR REPLACE FUNCTION check_exam_day_limit()
RETURNS trigger AS $enforce_exam_day_limit$
    DECLARE
        exam_date DATE;

    BEGIN
        /*
        Assign exdate to exam_date identified using the excode
        Allows exception to specify registered date
        */
        SELECT exdate INTO exam_date FROM exam WHERE excode = NEW.excode;

        /*
        JOINS entry and exam using the exam code,
        Searches entry to see if student number is present,
        and if the date of the new exam is the same as the regestered entry
        */
        IF EXISTS (
            SELECT 1 FROM entry
            INNER JOIN exam ON entry.excode = exam.excode
            WHERE entry.sno = NEW.sno AND exam.exdate = exam_date
        ) 
        /*
        If it does exist, conflict is then raised and specified
        */
        Then 
            RAISE EXCEPTION 
            'Student: % is already registered for an exam (%) on that date: %',
            NEW.sno, NEW.excode, exam_date;
        END IF;

        -- Else insert normally
        RETURN NEW;

    END;
$enforce_exam_day_limit$ LANGUAGE PLPGSQL;

-- Triggers function before inserting to entry table
CREATE OR REPLACE TRIGGER enforce_exam_day_limit BEFORE INSERT ON entry
    FOR EACH ROW EXECUTE FUNCTION check_exam_day_limit();


-- Prevents a student from entering the same exam more than once in a year
CREATE OR REPLACE FUNCTION check_exam_attempt_limit()
RETURNS trigger AS $enforce_exam_attempt_limit$
    DECLARE
        exam_year INT;

    BEGIN
        /*
        Extracts the year from exdate 
        Assigns it to exam_year identified using the excode
        Allows exception to specify registered date
        */
        SELECT date_part('year', exdate) INTO exam_year FROM exam WHERE excode = NEW.excode;

        /*
        JOINS entry and exam using the exam code,
        Searches entry to see if student number is present,
        if the same exam is entered twice in the same year it raises exceptions
        */
        IF EXISTS(
            SELECT 1 FROM entry
            INNER JOIN exam ON entry.excode = exam.excode
            WHERE entry.sno = NEW.sno 
                AND entry.excode = NEW.excode
                AND date_part('year', exam.exdate) = exam_year
        )
        /*
        If it does exist, conflict is then raised and specified
        */
        Then 
            RAISE EXCEPTION 
            'Student: % already has exam (%) this year',
            NEW.sno, NEW.excode;
        END IF;

        -- Else insert normally
        RETURN NEW;

    END;
$enforce_exam_attempt_limit$ LANGUAGE PLPGSQL;


-- Triggers function before inserting to entry table
CREATE OR REPLACE TRIGGER enforce_exam_attempt_limit BEFORE INSERT ON entry
    FOR EACH ROW EXECUTE FUNCTION check_exam_attempt_limit();


-- Automatically fills cancel table upon entry deletion
CREATE OR REPLACE FUNCTION autofill_cancel_table()
RETURNS trigger AS $autofill_cancel_table$
    BEGIN

        /*
        Inserts deleted data into cancel table to retain integrity
        */
        INSERT INTO cancel(eno, excode, sno, cdate, cuser) VALUES
            (OLD.eno, OLD.excode, OLD.sno, NOW(), 'System user');

        RETURN NULL;

    END;
$autofill_cancel_table$ LANGUAGE PLPGSQL;

-- Triggers function upon entry deletion
CREATE OR REPLACE TRIGGER autofill_cancel_table AFTER DELETE ON entry
    FOR EACH ROW EXECUTE FUNCTION autofill_cancel_table();

-----------------------------------------------


-------------------- VIEWS --------------------

-- Student Timeable

-- Joins the 3 tables and provides a view table with 
-- exam details and students name 
CREATE OR REPLACE VIEW student_timetable AS
SELECT student.sno, student.sname, exam.excode, exam.extitle, exam.exlocation, exam.exdate, exam.extime 
FROM exam
INNER JOIN entry ON exam.excode = entry.excode
INNER JOIN student ON entry.sno = student.sno
ORDER BY exdate, extime;

-- Exam Results (Distinction/Pass/Fail)

-- Joins the 3 tables and provides an case statement
-- which calculates egrade into a result
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
WHERE sname = 'Emily Parker';

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
