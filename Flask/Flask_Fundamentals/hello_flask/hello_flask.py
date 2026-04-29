from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/Champion')
def Champion():
    return "Champion !"

@app.route('/say/<name>')
def say(name):
    return name

@app.route('/repeat/<times>/<word>')
def repeat(times,word):
    return (word +" ")*int(times)

if __name__ == "__main__":
    app.run(debug=True)



