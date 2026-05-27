# Django Counter App

A simple Django project that counts how many times a user has visited the homepage using sessions.

---

##  Features

* Tracks number of visits using Django sessions
* Increments counter on every page refresh
* Reset counter using a session destroy route
* Simple routing and views practice

---

## Technologies Used

* Python
* Django
* HTML
* Sessions (Django built-in)

---

##  Project Structure

```
counter/
│
├── counter/
│   └── settings.py
│   └── urls.py
│
├── app/
│   └── views.py
│   └── urls.py
│
├── templates/
│   └── index.html
│
└── manage.py
```

---

## How to Run the Project

### 1. Activate virtual environment

```bash
.\env\Scripts\activate
```

### 2. Install Django

```bash
pip install django
```

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Start server

```bash
python manage.py runserver
```

---

## Routes

| Route               | Description                  |
| ------------------- | ---------------------------- |
| `/`                 | Shows counter (visits count) |
| `/delete_session/` | Resets the counter           |

---

##  What I Learned

* How sessions work in Django
* How to store and modify session data
* How to create routes and views
* Handling GET requests and redirects
