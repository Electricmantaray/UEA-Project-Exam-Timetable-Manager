-- COURSEWORK --

--------------- SCHEMA CREATION ---------------
CREATE SCHEMA IF NOT EXISTS Coursework;
SET search_path TO Coursework;
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
    eno INTEGER NOT NULL,
    excode CHAR(4) NOT NULL,
    sno INTEGER NOT NULL,
    cdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cuser VARCHAR(200) NOT NULL,
    PRIMARY KEY (eno),
    CONSTRAINT fk_cancel_exam FOREIGN KEY (excode) REFERENCES exam(excode) ON DELETE CASCADE,
    CONSTRAINT fk_cancel_student FOREIGN KEY (sno) REFERENCES student(sno) ON DELETE SET NULL
);

----------------------------------------------


------------ FUNCTIONS / TRIGGER ------------

-- Functions --


-- Triggers Functions --

-- Preventing entry into multiple exams on the same day
CREATE OR REPLACE FUNCTION exam_day_limit()
RETURNS trigger AS $exam_day_limit$
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

        RETURN NEW;

    END;
$exam_day_limit$ LANGUAGE PLPGSQL;

-- Triggers function before inserting to entry table
CREATE OR REPLACE TRIGGER exam_day_limit BEFORE INSERT ON entry
    FOR EACH ROW EXECUTE FUNCTION exam_day_limit();




-- Function --





----------------------------------------------