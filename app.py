from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

questions = [
    {
        "question": "What is the output of print(2 * 3 + 4)?",
        "options": ["10", "14", "12", "8"],
        "answer": "10"
    },
    {
        "question": "Which datatype is used to store text in Python?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },
    {
        "question": "Which language is primarily used for data analysis?",
        "options": ["C++", "Python", "Java", "Swift"],
        "answer": "Python"
    },
    {
        "question": "Which of the following is used to define a function in Python?",
        "options": ["function", "def", "define", "func"],
        "answer": "def"
    },
    {
        "question": "What symbol is used for single-line comment in Python?",
        "options": ["//", "<!-- -->", "#", "/* */"],
        "answer": "#"
    },
]


@app.route('/')
def home():
    return render_template('home.html', total=len(questions))

@app.route('/start')
def start():
    session['score'] = 0
    session['current'] = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    current = session.get('current', 0)

    if request.method == 'POST':
        selected = request.form.get('option')
        if selected == questions[current]['answer']:
            session['score'] += 1
        session['current'] += 1
        current = session['current']

        if current >= len(questions):
            return redirect(url_for('result'))

    if current < len(questions):
        q = questions[current]
        return render_template('quiz.html', question=q, current=current + 1, total=len(questions))
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
