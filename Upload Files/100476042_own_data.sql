SET search_path TO Coursework, public;

-- DATA INSERTIONS --

--------------- NORMAL DATA ---------------

-- EXAM --
INSERT into exam(excode, extitle, exlocation, exdate, extime) VALUES
    ('DB01', 'Database system exam 1', 'UEA Lecture hall 01', '2025-11-08', '09:30'),
    ('DB02', 'Database system exam 2', 'UEA Lecture hall 03', '2025-11-14', '13:15'),
    ('DB03', 'Database system exam 3', 'UEA Congregation hall', '2025-11-21', '11:00'),
    ('SD01', 'Systems development, multiple choice', 'Online exam', '2025-11-16', '16:25'),
    ('SD02', 'Systems development, long questions', 'Online exam', '2025-11-25', '16:25'),
    ('WP01', 'Web-based programming, General exam', 'UEA Thomas Paine room 2', '2025-11-14', '14:55'),
    ('WP02', 'Web-based programming, Higher exam', 'Kings College London, main hall', '2025-11-17', '15:30'),
    ('AI01', 'Ai, end of year exam', 'University of Birmingham, hall 2', '2025-11-02', '10:15'),
    ('AI02', 'Ai, Large language models and beyond', 'University of Birmingham, room 305', '2025-11-07', '12:00'),
    ('MA01', 'Maths Group A, Calculus 1', 'University of sheffield, The Diamond, room 13', '2025-11-09', '9:05');

-- STUDENT --
INSERT into student(sno, sname, semail) VALUES
    (1, 'Emily Parker', 'eparker23@example.edu'),
    (2, 'Liam Nguyen', 'lnguyen17@example.edu'),
    (3, 'Sophia Patel', 'spatel45@example.edu'),
    (4, 'Jacob Thompson', 'jthomson02@example.edu'),
    (5, 'Ava Brooks', 'abrooks88@example.edu'),
    (6, 'Ethan Davis', 'edavis14@example.edu'),
    (7, 'Isla Robinson', 'irobinson30@example.edu'),
    (8, 'Noah Campbell', 'ncampbell23@example.edu'),
    (9, 'Mia Ahmed', 'mahmed42@example.edu'),
    (10, 'Oscar Bennett', 'obennett01@example.edu');


-- ENTRY --
INSERT into entry(eno, excode, sno, egrade) VALUES
    (1, 'DB01', 3, 49.19),  -- Sophia Patel takes DB01
    (2, 'WP02', 5, 74.26),  -- Ava Brooks takes WP02
    (3, 'SD01', 7, NULL),   -- Isla Robinson registered, NOT TAKEN
    (4, 'DB01', 2, 61.39),  -- Liam Nguyen takes DB01
    (5, 'DB02', 3, NULL),   -- Sophia Patel registered, NOT TAKEN
    (6, 'AI02', 4, 0.73),   -- Jacob Thompson takes AI02
    (7, 'WP01', 5, NULL),   -- Ava Brooks registered, NOT TAKEN
    (8, 'AI01', 4, 47.84),  -- Jacob Thompson takes AI01
    (9, 'MA01', 10, 24.02), -- Oscar Bennett takes MA01
    (10, 'SD02', 7, NULL);  -- Isla Robinson registered, NOT TAKEN


-- CANCEL --
INSERT into cancel(eno, excode, sno, cdate, cuser) VALUES
    (11, 'WP01', 1, '2025-09-27 19:08:34', 'admin'),   -- Emily Parker registered
    (12, 'DB03', 2, '2025-01-04 04:58:36', 'admin'),   -- Liam Nguyen registered
    (13, 'MA01', 3, '2025-03-23 17:30:30', 'admin'),   -- Sophia Patel registered
    (14, 'AI01', 4, '2025-03-11 14:51:10', 'admin'),   -- Jacob Thompson
    (15, 'SD01', 5, '2025-01-20 05:09:07', 'admin'),   -- Ava Brooks
    (16, 'AI02', 6, '2025-08-10 22:21:59', 'admin'),   -- Ethan Davis
    (17, 'DB02', 7, '2025-08-08 04:16:45', 'admin'),   -- Isla Robinson
    (18, 'WP02', 8, '2025-05-19 17:23:25', 'admin'),   -- Noah Campbell
    (19, 'SD02', 9, '2025-04-14 01:34:17', 'admin'),   -- Mia Ahmed
    (20, 'DB01', 10, '2025-02-19 20:53:34', 'admin');  -- Oscar Bennett
---------------------------------------------

/*
--------------- Abnormal Data ---------------

-- EXAM --
INSERT into exam(excode, extitle, exlocation, exdate, extime) VALUES
-- Primary Key Violation (Duplicate excode)
-- Output:
    /* 
    ERROR:  duplicate key value violates unique constraint "exam_pkey"
    Key (excode)=(DB01) already exists. 
    */
    ('DB01', 'Abnormal exam 1', 'Abnormal location', '2025-11-01', '09:00'),

-- Duplicated Title Violation (extitle Not Unique)
-- Output:
    /* 
    ERROR:  duplicate key value violates unique constraint "exam_extitle_key"
    Key (extitle)=(Database system exam 2) already exists. 
    */
    ('A001', 'Database system exam 2', 'Abnormal location', '2025-11-01', '9:00'),

-- NULL Violation (excode, extitle, exlocation, exdate, extime)
-- Output:
    /* 
    ERROR:  null value in column "excode" of relation "exam" violates not-null constraint
    Failing row contains (null, Abnormal exam 2, Abnormal location, 2025-11-01, 09:00:00). 
    ERROR:  null value in column "extitle" of relation "exam" violates not-null constraint
    Failing row contains (A002, null, Abnormal location, 2025-11-01, 09:00:00). 
    ERROR:  null value in column "exlocation" of relation "exam" violates not-null constraint
    Failing row contains (A003, Abnormal exam 3, null, 2025-11-01, 09:00:00). 
    ERROR:  null value in column "exdate" of relation "exam" violates not-null constraint
    Failing row contains (A004, Abnormal exam 4, Abnormal location, null, 09:00:00). 
    ERROR:  null value in column "extime" of relation "exam" violates not-null constraint
    Failing row contains (A005, Abnormal exam 5, Abnormal location, 2025-11-01, null). 
    */
    (NULL, 'Abnormal exam 2', 'Abnormal location', '2025-11-01', '09:00'),
    ('A002', NULL,  'Abnormal location', '2025-11-01', '09:00'),
    ('A003', 'Abnormal exam 3', NULL, '2025-11-01', '09:00'),
    ('A004', 'Abnormal exam 4', 'Abnormal location', NULL, '09:00'),
    ('A005', 'Abnormal exam 5', 'Abnormal location', '2025-11-01', NULL),

-- Abnormally Long code/title and location (Greater than their limits)
-- Output:
    /*
    ERROR:  value too long for type character(4) 
    ERROR:  value too long for type character varying(200) 
    */
    ('A9999', 'Abnormal exam 9999', 'Abnormal location',  '2025-11-01', '09:00'),
    ('A006', 'Lorem ipsum dolor sit amet consectetur adipiscing 
    elit quisque faucibus ex sapien vitae pellentesque sem 
    placerat in id cursus mi pretium tellus duis convallis 
    tempus leo eu aenean sed diam urna tempor',
    'Lorem ipsum dolor sit amet consectetur adipiscing 
    elit quisque faucibus ex sapien vitae pellentesque sem 
    placerat in id cursus mi pretium tellus duis convallis 
    tempus leo eu aenean sed diam urna tempor',
    '2025-11-01', '09:00'),

-- Constraint Violations (exdate outside of November 2025, extime outside the 09:00-18:00)
-- Output:
    /*
    ERROR:  new row for relation "exam" violates check constraint "exam_exdate_check"
    Failing row contains (A007, Abnormal exam 7, Abnormal location, 2024-12-25, 09:00:00).
    ERROR:  new row for relation "exam" violates check constraint "exam_extime_check"
    Failing row contains (A008, Abnormal exam 8, Abnormal location, 2025-11-01, 21:00:00). 
    */
    ('A007', 'Abnormal exam 7', 'Abnormal location', '2024-12-25', '09:00'),
    ('A008', 'Abnormal exam 8', 'Abnormal location', '2025-11-01', '21:00');


-- STUDENT --
INSERT into student(sno, sname, semail) VALUES
-- Primary Key Violation (Duplicate sno)
-- Output: 
    /*
    ERROR:  duplicate key value violates unique constraint "student_pkey"
    Key (sno)=(1) already exists. 
    */
    (1, 'Abnormal Student', 'Abnormal1@example.edu'),

-- Duplicated Email Violation (semail Not Unique)
-- Output: 
    /*
    ERROR:  duplicate key value violates unique constraint "student_semail_key"
    Key (semail)=(lnguyen17@example.edu) already exists. 
    */
    (9999, 'Abnormal Student', 'lnguyen17@example.edu'),

-- Empty Violation (sno, sname, semail)
-- Output:
    /*
    ERROR:  null value in column "sno" of relation "student" violates not-null constraint
    Failing row contains (null, Void1, void1@example.edu). 
    ERROR:  null value in column "sname" of relation "student" violates not-null constraint
    Failing row contains (9998, null, Void2@example.edu). 
    ERROR:  null value in column "semail" of relation "student" violates not-null constraint
    Failing row contains (9997, Void3, null). 
    */
    (NULL, 'Void1', 'void1@example.edu'),
    (9998, NULL, 'Void2@example.edu'),
    (9997, 'Void3', NULL),

-- Invalid Entry Type (INTEGER -> CHAR, CHAR -> INTEGER)
-- Output:
    /*
    Data type is automatically corrected and inserted
    */
    ('9996', 'Abnormal Student', 'abnormal2@example.edu'),
    (9995, 1234, 1234),

-- Abnormally Long names and emails (Greater than 200 characters)
-- Output:
    /*
    ERROR:  value too long for type character varying(200) 
    */
    (9994, 'Lorem ipsum dolor sit amet consectetur adipiscing 
    elit quisque faucibus ex sapien vitae pellentesque sem 
    placerat in id cursus mi pretium tellus duis convallis 
    tempus leo eu aenean sed diam urna tempor', 
    'Lorem ipsum dolor sit amet consectetur adipiscing 
    elit quisque faucibus ex sapien vitae pellentesque sem 
    placerat in id cursus mi pretium tellus duis convallis 
    tempus leo eu aenean sed diam urna tempor');


-- ENTRY --
INSERT into entry(eno, excode, sno, egrade) VALUES
-- Primary Key Violation (Duplicate eno)
-- Output: 
    /*
    ERROR:  duplicate key value violates unique constraint "entry_pkey"
    Key (eno)=(1) already exists.
    */
    (1, 'DB02', 1, NULL),

-- Duplicated Entrys Violations (A student can only enter a specific exam once per year)
-- Output: 
    /*
    ERROR:  Student: 1 already has exam (DB01) this year
    */
    (9999, 'DB01', 1, NULL),
    (9998, 'DB01', 1, NULL),

-- Empty Violation (eno, excode, sno)
-- Output:
    /*
    ERROR:  null value in column "eno" of relation "entry" violates not-null constraint
    Failing row contains (null, DB01, 2, null). 
    ERROR:  null value in column "excode" of relation "entry" violates not-null constraint
    Failing row contains (9997, null, 3, null). 
    ERROR:  null value in column "sno" of relation "entry" violates not-null constraint
    Failing row contains (9996, DB03, null, null). 
    */
    (NULL, 'DB01', 2, NULL),
    (9997, NULL, 3, NULL),
    (9996, 'DB03', NULL, NULL),

-- Foreign Key Violation (Non-existent excode or sno)
-- Output:
    /*
    ERROR:  insert or update on table "entry" violates foreign key constraint "fk_entry_exam"
    Key (excode)=(NONE) is not present in table "exam".
    ERROR:  insert or update on table "entry" violates foreign key constraint "fk_entry_student"
    Key (sno)=(7421) is not present in table "student"
    */
    (9995, 'NONE', 4, NULL),
    (9994, 'AI02', 7421, NULL),

-- Same Day Exam Violation (Same student has multiple exams on the same day)
-- Output: 
    /*
    ERROR:  Student: 6 is already registered for an exam (DB02) on that date: 2025-11-14
    */
    (9993, 'DB02', 6, NULL),
    (9992, 'WP01', 6, NULL),

-- Constraint Violation (egrade outside of 0-100 bounds, egrade with 3 or more decimal places)
-- Output:
    /*
    ERROR:  new row for relation "entry" violates check constraint "entry_egrade_check"
    Failing row contains (9991, MA01, 4, 101.00). 
    Rounds the decimal places to 2, 50.5555 -> 50.56
    */
    (9991, 'MA01', 4, 101.00),
    (9990, 'SD01', 7, 50.5555);


-- CANCEL --
INSERT into cancel(eno, excode, sno, cdate, cuser) VALUES
-- Primary Key Violation (Duplicate)
-- Output:
    /*
    ERROR:  duplicate key value violates unique constraint "cancel_pkey"
    Key (eno)=(11) already exists. 
    */
    (11, 'MA01', 10, '2025-01-01 00:00:00', 'admin'),

-- Empty Violation (eno, excode, sno, cuser)
-- Output:
    /*
    ERROR:  null value in column "eno" of relation "cancel" violates not-null constraint
    Failing row contains (null, SD02, 5, 2025-01-01 00:00:00, admin).
    ERROR:  null value in column "excode" of relation "cancel" violates not-null constraint
    Failing row contains (9999, null, 3, 2025-01-01 00:00:00, admin). 
    ERROR:  null value in column "sno" of relation "cancel" violates not-null constraint
    Failing row contains (9998, DB03, null, 2025-01-01 00:00:00, admin).
    ERROR:  null value in column "cuser" of relation "cancel" violates not-null constraint
    Failing row contains (9997, AI02, 3, 2025-01-01 00:00:00, null). 
    */
    (NULL, 'SD02', 5, '2025-01-01 00:00:00', 'admin'),
    (9999, NULL, 3, '2025-01-01 00:00:00', 'admin'),
    (9998, 'DB03', NULL, '2025-01-01 00:00:00', 'admin'),
    (9997, 'AI02', 3, '2025-01-01 00:00:00', NULL),

-- Foreign Key Violation (Non-existent excode and Student already cancelled sno)
-- Output:
    /*
    ERROR:  insert or update on table "cancel" violates foreign key constraint "fk_cancel_exam"
    Key (excode)=(CODE) is not present in table "exam". 
    ERROR:  insert or update on table "cancel" violates foreign key constraint "fk_cancel_student"
    Key (sno)=(6435) is not present in table "student". 
    */
    (9996, 'CODE', 9, '2025-01-01 00:00:00', 'admin'),
    (9995, 'DB02', 6435, '2025-01-01 00:00:00', 'admin');
---------------------------------------------

*/