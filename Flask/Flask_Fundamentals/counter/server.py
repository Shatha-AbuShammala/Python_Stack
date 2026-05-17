from flask import Flask, session, redirect, render_template

app = Flask(__name__)
app.secret_key = "secret_key_here"  

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0  
    
    session['count'] += 1  
    return render_template('index.html', count=session['count'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()  
    return redirect('/')  

# BONUS
@app.route('/add_two')
def add_two():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 2
    return redirect('/')

# BONUS
@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)