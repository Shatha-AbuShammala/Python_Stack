# Multiple Apps Project (Django)

A Django project demonstrating how to structure and manage multiple independent apps inside a single Django project.

This project includes:

* Blogs app
* Surveys app
* Users app

The assignment focuses on Django routing, app structure, URL configuration, and modular project organization.

---

## Features

### Blogs App

* Display all blogs
* Create blog placeholder
* Dynamic blog routes
* Edit and delete blog placeholders

### Surveys App

* Display surveys placeholder
* Create survey placeholder

### Users App

* Register placeholder
* Login placeholder
* Users list placeholder

---

## Technologies Used

* Python
* Django
* Django URL Routing
* Django Apps Architecture

---

## Project Structure

```id="s1"
multiple_apps/
│
├── blogs/
│   ├── views.py
│   ├── urls.py
│
├── surveys/
│   ├── views.py
│   ├── urls.py
│
├── users/
│   ├── views.py
│   ├── urls.py
│
├── multiple_apps/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## Routes

### Blogs Routes

| Route                     | Description             |
| ------------------------- | ----------------------- |
| `/blogs/`                 | Display all blogs       |
| `/blogs/new/`             | New blog placeholder    |
| `/blogs/create/`          | Redirect to blogs page  |
| `/blogs/<number>/`        | Display blog number     |
| `/blogs/<number>/edit/`   | Edit blog placeholder   |
| `/blogs/<number>/delete/` | Delete blog placeholder |

---

### Surveys Routes

| Route           | Description               |
| --------------- | ------------------------- |
| `/surveys/`     | Display all surveys       |
| `/surveys/new/` | Create survey placeholder |

---

### Users Routes

| Route        | Description               |
| ------------ | ------------------------- |
| `/register`  | Register placeholder      |
| `/login`     | Login placeholder         |
| `/users/new` | Same register method      |
| `/users`     | Display users placeholder |

---

## How to Run

### 1. Activate virtual environment

```bash id="s2"
.\env\Scripts\activate
```

### 2. Install Django

```bash id="s3"
pip install django
```

### 3. Run migrations

```bash id="s4"
python manage.py migrate
```

### 4. Start server

```bash id="s5"
python manage.py runserver
```
