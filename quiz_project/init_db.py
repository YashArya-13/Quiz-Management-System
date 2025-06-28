import sqlite3

# Connect to the SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()

# Create table
cursor.executescript("""
DROP TABLE IF EXISTS quizzes;

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    type TEXT
);

INSERT INTO quizzes (name, description, type) VALUES
('Python Basics', 'A quiz on basic Python knowledge', 'MCQ'),
('Math Quiz', 'Simple math problems', 'MCQ');
""")

conn.commit()
conn.close()

print("Database initialized successfully.")
