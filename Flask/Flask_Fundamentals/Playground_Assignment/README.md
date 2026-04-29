# Playground Assignment - Flask

## Description
A Flask server that renders HTML templates with dynamic boxes using Jinja2.

## How to Run
1. Install Flask
pip install flask

2. Run the server
python play.py

3. Open your browser and try:
- localhost:5000/play
- localhost:5000/play/7
- localhost:5000/play/5/green

## Routes
- `/play` → displays 3 blue boxes
- `/play/<x>` → displays x blue boxes
- `/play/<x>/<color>` → displays x boxes with the given color

## Project Structure
Playground_Assignment/
├── play.py
└── templates/
      └── index.html