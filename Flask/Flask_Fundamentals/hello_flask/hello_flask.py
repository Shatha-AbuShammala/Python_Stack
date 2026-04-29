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
#Ninja Bounce
@app.route('/repeat/<int:times>/<word>')
def repeat(times,word):
    return (word +" ")*(times)

#SENSI bouns
@app.errorhandler(404)  
def page_not_found(error):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)



