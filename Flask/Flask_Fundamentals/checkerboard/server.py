from flask import Flask,render_template
app =Flask(__name__)

@app.route('/')
def board():
    return render_template('index.html', rows=8, cols=8)

@app.route('/<int:x>')
def board_x(x):
    return render_template('index.html', rows=x, cols=8)
@app.route('/<int:x>/<int:y>')
def board_x_y(x,y):
    return render_template('index.html', rows=x, cols=y)

if __name__ == "__main__":
    app.run(debug=True)

