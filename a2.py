from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Jane Austen"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)


@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i, question in enumerate(questions):
        user_answer = request.form.get(f'question-{question}')
        if user_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
