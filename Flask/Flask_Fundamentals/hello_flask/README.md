# Understanding Routing - Flask

## Description
A Flask server that handles different URL routes and returns specified responses.

## How to Run
1. Install Flask
pip install flask

2. Run the server
python server.py

3. Open your browser and try:
- localhost:5000/
- localhost:5000/Champion
- localhost:5000/say/YourName
- localhost:5000/repeat/35/hello

## Routes
- `/` → returns "Hello World!"
- `/Champion` → returns "Champion!"
- `/say/<name>` → returns "Hi {name}!"
- `/repeat/<times>/<word>` → returns the word repeated {times} times