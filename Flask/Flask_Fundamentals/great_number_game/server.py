from flask import Flask, session, redirect, render_template, request
import random

app = Flask(__name__)
app.secret_key = "abc"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    number = session['number']
    
    if guess < number:
        result = "Too low!"
    elif guess > number:
        result = "Too high!"
    else:
        session.clear()
        return render_template('index.html', result="Correct!")
    
    return render_template('index.html', result=result)

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)