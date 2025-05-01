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
    CONSTRAINT fk_cancel_entry FOREIGN KEY (eno) REFERENCES entry(eno) ON DELETE CASCADE,
    CONSTRAINT fk_cancel_exam FOREIGN KEY (excode) REFERENCES exam(excode) ON DELETE CASCADE,
    CONSTRAINT fk_cancel_student FOREIGN KEY (sno) REFERENCES student(sno) ON DELETE SET NULL
);

----------------------------------------------

-- Triggers --

-- Preventing multiple exams on the same day
/*
CREATE OR REPLACE FUNCTION 
*/
