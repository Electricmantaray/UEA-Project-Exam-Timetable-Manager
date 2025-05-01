-- COURSEWORK --

SET search_path TO Coursework;

-- DATA INSERTIONS --

--------------- NORMAL DATA ---------------

-- EXAM
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

-- STUDENT
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

-- ENTRY
INSERT into entry(eno, excode, sno, egrade) VALUES
    (1, 'DB01', 3, 49.19),
    (2, 'WP02', 5, 74.26),
    (3, 'SD01', 7, 80.23),
    (4, 'DB01', 2, 61.39),
    (5, 'DB02', 3, 62.02),
    (6, 'AI02', 4, 0.73),
    (7, 'WP01', 5, NULL),
    (8, 'AI01', 4, 47.84),
    (9, 'MA01', 10, 24.02),
    (10, 'SD02', 7, NULL);

-- CANCEL
INSERT into cancel(eno, excode, sno, cdate, cuser) VALUES
    (),
    (),
    (),
    (),
    ();
---------------------------------------------


--------------- Abnormal Data ---------------

-- EXAM
INSERT into exam(excode, extitle, exlocation, exdate, extime) VALUES
-- Primary Key Violation (Duplicate excode)
-- Output:
-- 
    ('DB01', 'Abnormal exam 1', 'Abnormal location', '2025-11-01', '09:00'),

-- Duplicated Title Violation (extitle Not Unique)
-- Output:
-- 
    ('A001', 'Database system exam 2', 'Abnormal location', '2025-11-01', '9:00'),

-- NULL Violation (excode, extitle, exlocation, exdate, extime)
-- Output:
-- 
    (NULL, 'Abnormal exam 2', 'Abnormal location', '2025-11-01', '09:00'),
    ('A002', NULL,  'Abnormal location', '2025-11-01', '09:00'),
    ('A003', 'Abnormal exam 3', NULL, '2025-11-01', '09:00'),
    ('A004', 'Abnormal exam 4', 'Abnormal location', NULL, '09:00'),
    ('A005', 'Abnormal exam 5', 'Abnormal location', '2025-11-01', NULL),

-- Abnormally Long code/title and location (Greater than their limits)
-- Output:
-- 
    ('A9999', 'Abnormal exam 9999', 'Abnormal location',  '2025-11-01', '09:00'),
    ('A0006', 'Lorem ipsum dolor sit amet consectetur adipiscing 
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
-- 
    ('A007', 'Abnormal exam 7', 'Abnormal location', '2024-12-25', '09:00'),
    ('A008', 'Abnormal exam 8', 'Abnormal location', '2025-11-01', '21:00');

-- STUDENT
INSERT into student(sno, sname, semail) VALUES
-- Primary Key Violation (Duplicate sno)
-- Output: 
-- 
    (1, 'Abnormal Student', 'Abnormal1@example.edu'),

-- Duplicated Email Violation (semail Not Unique)
-- Output: 
-- 
    (2, 'Abnormal Student', 'lnguyen17@example.edu'),

-- Empty Violation (sno, sname, semail)
-- Output:
-- 
    (NULL, 'Void1', 'void1@example.edu'),
    (9999, NULL, 'Void2@example.edu'),
    (9998, 'Void3', NULL),

-- Invalid Entry Type (INTEGER -> CHAR, CHAR -> INTEGER)
-- Output:
-- 
    ('1', 'Abnormal Student', 'abnormal2@example.edu'),
    (9997, 1234, 1234),

-- Abnormally Long names and emails (Greater than 200 characters)
-- Output:
-- 
    (9996, 'Lorem ipsum dolor sit amet consectetur adipiscing 
    elit quisque faucibus ex sapien vitae pellentesque sem 
    placerat in id cursus mi pretium tellus duis convallis 
    tempus leo eu aenean sed diam urna tempor', 
    'Lorem ipsum dolor sit amet consectetur adipiscing 
    elit quisque faucibus ex sapien vitae pellentesque sem 
    placerat in id cursus mi pretium tellus duis convallis 
    tempus leo eu aenean sed diam urna tempor');

-- ENTRY
INSERT into entry(eno, excode, sno, egrade) VALUES
-- Primary Key Violation (Duplicate eno)
-- Output: 
-- 
    (1, 'DB02', 1, NULL),

-- Duplicated Entrys Violations (Multiple entrys for the same student and exam)
-- Output: 
-- 
    (9999, 'DB01', 1, NULL),
    (9998, 'DB01', 1, NULL),

-- Empty Violation/Foreign Key Violation (eno, Foreign Key Violation: excode, sno)
-- Output:
-- 
    (NULL, 'DB01', 2, NULL),
    (9997, NULL, 3, NULL),
    (9996, 'DB03', NULL, NULL),

-- Same Day Exam Violation (Same student has multiple exams on the same day)
-- Output:
--
    (9995, 'DB02', 6, NULL),
    (9996, 'WP01', 6, NULL),

-- Constraint Violation (egrade outside of 0-100 bounds, egrade with 3 or more decimal places)
-- Output
-- 
    (9995, 'MA01', 4, 101.00),
    (9994, 'SP01', 7, 50.5555);

-- CANCEL
INSERT into cancel(eno, excode, sno, cdate, cuser) VALUES
    (),
    (),
    (),
    (),
    ();
---------------------------------------------
