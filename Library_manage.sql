CREATE DATABASE lib_management;

CREATE TABLE Books
(
	book_id INT PRIMARY KEY,
    book_name VARCHAR(50),
    published_year DATE
);

CREATE TABLE Students
(
	student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    student_age INT
);

CREATE TABLE BorrowedBooks
(
	trans_id INT PRIMARY KEY AUTO_INCREMENT,
    Bstd_id INT,
    Bbook_id INT,
    FOREIGN KEY (Bstd_id) REFERENCES Students(student_id),
    FOREIGN KEY (Bbook_id) REFERENCES Books(book_id)
);

CREATE TABLE LibrarySummary
(
	Namee VARCHAR(50),
    Total INT
);
SELECT * FROM LibrarySummary;

SELECT
	bb.trans_id,
	bb.Bstd_id,
    s.student_name,
    bb.Bbook_id,
    b.book_name
FROM BorrowedBooks bb
INNER JOIN Students s
ON bb.Bstd_id = s.student_id
INNER JOIN Books b
ON bb.Bbook_id = b.book_id
ORDER BY s.student_id;

SELECT * FROM BorrowedBooks
ORDER BY Bstd_id ASC;

INSERT INTO Books
VALUES
	(444, "JAVA Full Course", "3000-03-23"),
    (555, "CPP Full Course", "206-05-1"),
    (667, "JS Full Course", "1956-12-25");
SELECT * FROM Books;

INSERT INTO Students
VALUES
	(400, "Sanji", 39),
    (500, "Luffy", 47),
    (600, "Zoro", 51);
SELECT * FROM Students;

    
INSERT INTO BorrowedBooks (Bstd_id, Bbook_id)
VALUES
	(100,444),
    (300,555),
    (100,667);
SELECT * FROM BorrowedBooks
ORDER BY Bstd_id ASC;

INSERT INTO BorrowedBooks (Bstd_id, Bbook_id)
VALUES
    (400,667);
SELECT * FROM BorrowedBooks;

INSERT INTO LibrarySummary
VALUES  ("STUDENTS", NULL),
		("BOOKS", NULL),
        ("BORROWED_BOOKS", NULL);
-- Show books published after January 1, 2010.

SELECT * FROM Books
WHERE published_year > "2000-12-30";


-- Count how many books each student borrowed.
SELECT 
	s.student_id,
	s.student_name,
	COUNT(bb.Bbook_id) AS "Total books Borrowed"
FROM Students s
LEFT JOIN BorrowedBooks bb
ON s.student_id = bb.Bstd_id
GROUP BY s.student_id, s.student_name
ORDER BY COUNT(bb.Bbook_id) DESC;

-- Calculate the average student age.
SELECT ROUND(avg(student_age), 2) AS "students avg age"
FROM students;

--  Count the total borrowing transactions.
SELECT COUNT(trans_id) AS "Total Borrowed Books"
FROM BorrowedBooks;

-- Show students whose age is above the average age.
SELECT * FROM Students
WHERE student_age > (SELECT AVG(student_age) FROM Students);

-- Show students who never borrowed a book.

SELECT * FROM Students
WHERE student_id NOT IN (SELECT Bstd_id FROM BorrowedBooks);
    
-- Update Students count after inserting a student.
DELIMITER $
CREATE TRIGGER total_students
AFTER INSERT ON Students
FOR EACH ROW
BEGIN
UPDATE LibrarySummary
SET Total = (SELECT COUNT(student_id) FROM Students)
WHERE Namee = "STUDENTS";
END $
DELIMITER ;

-- Update Students count after DROP a student.
DELIMITER $
CREATE TRIGGER total_students_del
AFTER DELETE ON Students
FOR EACH ROW
BEGIN
UPDATE LibrarySummary
SET Total = (SELECT COUNT(student_id) FROM Students)
WHERE Namee = "STUDENTS";
END $
DELIMITER ;

SELECT * FROM librarysummary;
DELETE FROM Students
WHERE student_name = "RENCE";
SELECT * FROM librarysummary;


-- Update Books count after inserting a book.
DELIMITER $
CREATE TRIGGER total_books_ins
AFTER INSERT ON Books
FOR EACH ROW
BEGIN
UPDATE LibrarySummary
SET Total = (SELECT COUNT(book_id) FROM Books)
WHERE Namee = "BOOKS";
END $
DELIMITER ;

-- Update Books count after DELETE a book.
DELIMITER $
CREATE TRIGGER total_books_del
AFTER DELETE ON Books
FOR EACH ROW
BEGIN
UPDATE LibrarySummary
SET Total = (SELECT COUNT(book_id) FROM Books)
WHERE Namee = "BOOKS";
END $
DELIMITER ;

SELECT * FROM librarysummary;
DELETE FROM Books
WHERE book_id = 123;
SELECT * FROM librarysummary;
SELECT * FROM Books;


-- Update Borrowedbooks count after borrowing a book.
DELIMITER $
CREATE TRIGGER total_Bbooks_ins
AFTER INSERT ON BorrowedBooks
FOR EACH ROW
BEGIN
UPDATE LibrarySummary
SET Total = (SELECT COUNT(Bbook_id) FROM BorrowedBooks)
WHERE Namee = "BORROWED_BOOKS";
END $
DELIMITER ;


-- Update Borrowedbooks count after returning the book.
DELIMITER $
CREATE TRIGGER total_Bbooks_del
AFTER DELETE ON BorrowedBooks
FOR EACH ROW
BEGIN
UPDATE LibrarySummary
SET Total = (SELECT COUNT(Bbook_id) FROM BorrowedBooks)
WHERE Namee = "BORROWED_BOOKS";
END $
DELIMITER ;

SELECT * FROM librarysummary;
DELETE FROM BorrowedBooks
WHERE trans_id = 10;
SELECT * FROM librarysummary;
SELECT * FROM BorrowedBooks;

show triggers;

drop trigger if exists total_students;

-- Display all books borrowed by a specific student.
DELIMITER $
CREATE PROCEDURE BorrowedByStudent(IN s_id INT)
BEGIN
	SELECT
		book_id,
        book_name,
        published_year
	FROM Books
    WHERE book_id IN (SELECT Bbook_id FROM BorrowedBooks
					 WHERE Bstd_id = s_id);
END $
DELIMITER ;

CALL BorrowedByStudent(200);
CALL BorrowedByStudent(100);

-- Find students who borrowed every book
SELECT
    s.student_id,
    s.student_name
FROM Students s
INNER JOIN BorrowedBooks bb
    ON s.student_id = bb.Bstd_id
GROUP BY s.student_id, s.student_name
HAVING COUNT(DISTINCT bb.Bbook_id) = (
    SELECT COUNT(*)
    FROM Books
);