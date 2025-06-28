from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quizzes')
def quizzes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quizzes")
    quizzes = cursor.fetchall()
    conn.close()
    return render_template('quiz_list.html', quizzes=quizzes)

@app.route('/quiz/<int:quiz_id>')
def show_quiz(quiz_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, question_text, option1, option2, option3, option4 FROM questions WHERE quiz_id = %s", (quiz_id,))
    questions = cursor.fetchall()
    conn.close()
    return render_template("quiz.html", questions=questions, quiz_id=quiz_id)

@app.route('/submit_quiz/<int:quiz_id>', methods=['POST'])
def submit_quiz(quiz_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, correct_option FROM questions WHERE quiz_id = %s", (quiz_id,))
    answers = cursor.fetchall()
    score = 0
    for q_id, correct in answers:
        user_ans = request.form.get(f"q{q_id}")
        if user_ans and int(user_ans) == correct:
            score += 1
    conn.close()
    return f"<h2>Your Score: {score} / {len(answers)}</h2><a href='/quizzes'>Back to Quizzes</a>"

if __name__ == '__main__':
    app.run(debug=True)
