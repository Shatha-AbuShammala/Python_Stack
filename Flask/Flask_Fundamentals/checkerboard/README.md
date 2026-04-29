# Checkerboard Assignment - Flask

## Description
A Flask server that renders a checkerboard using Jinja2 and static CSS files.

## How to Run
1. Install Flask
pip install flask

2. Run the server
python server.py

3. Open your browser and try:
- localhost:5000/
- localhost:5000/4
- localhost:5000/10/10

## Routes
- `/` → displays 8x8 checkerboard
- `/<x>` → displays 8 rows x columns checkerboard
- `/<x>/<y>` → displays x rows y columns checkerboard

## Project Structure
Checkerboard/
├── server.py
├── static/
│     └── style.css
└── templates/
      └── index.html