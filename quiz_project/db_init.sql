USE package;  -- your database name

DROP TABLE IF EXISTS quizzes;

CREATE TABLE quizzes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    type TEXT
);

INSERT INTO quizzes (name, description, type) VALUES
('Python Basics', 'A quiz on basic Python knowledge', 'MCQ'),
('Math Quiz', 'Simple math problems', 'MCQ');
