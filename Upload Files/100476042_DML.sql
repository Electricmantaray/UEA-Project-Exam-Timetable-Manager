

----------- TRANSACTIONS OF INTEREST -----------
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
-----------------------------------------------
