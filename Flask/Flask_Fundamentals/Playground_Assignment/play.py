from flask import Flask,render_template
app= Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', num=3, color='blue')

@app.route('/play/<int:x>')
def paly_x(x):
    return render_template('index.html', num=x, color='blue')

@app.route('/play/<int:x>/<color>')
def paly_x_color(x,color):
    return render_template('index.html', num=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)