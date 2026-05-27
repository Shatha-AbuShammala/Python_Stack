# Great Number Game (Django)

A simple number guessing game built using Django sessions. The server randomly selects a number between 1 and 100, and the user tries to guess it.

---

## Features

* Random number generation (1–100)
* Session-based game state
* Tracks user guesses
* Displays hints (Too High / Too Low / Correct)
* Reset game functionality

---

## Technologies Used

* Python
* Django
* HTML
* Sessions

---

## How the Game Works

1. When the user opens the homepage:

   * Django generates a random number
   * Stores it in session

2. User submits a guess via form

3. Server compares:

   *  Too High
   *  Too Low
   *  Correct guess

4. Attempts are tracked in session

---

## 📁 Project Structure

```id="str1"
great_number_game/
│
├── game/
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   └── index.html
│
├── great_number_game/
│   └── settings.py
│   └── urls.py
│
└── manage.py
```

---

## How to Run

### 1. Activate virtual environment

```bash id="run1"
.\env\Scripts\activate
```

### 2. Install Django

```bash id="run2"
pip install django
```

### 3. Run migrations

```bash id="run3"
python manage.py migrate
```

### 4. Start server

```bash id="run4"
python manage.py runserver
```

---

## Routes

| Route     | Description             |
| --------- | ----------------------- |
| `/`       | Game homepage + form    |
| `/guess/` | Handles user guesses    |
| `/reset/` | Resets the game session |

---

## What I Learned

* How to use Django sessions
* How to store game state per user
* Handling POST requests with forms
* URL routing and redirects
* Random number generation in Python

---


