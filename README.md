# 📝 Blog Project Using Django
- (First Project of Django after learning at BigBasket)

A fully functional **Django Blog Application** built using **Django** and **MySQL**.  
This project demonstrates role-based access control, custom error handling, and CRUD operations through both web interface and REST APIs.

---

## 🚀 Features

### 👑 Admin (Superuser)
- Can **create**, **edit**, and **delete** any user’s posts.  
- Can **view** all posts created by any user.  
- Can **change permissions** of other users — for example, restrict a user so they can **only create posts** but not edit or delete them.  
- Has access to the **Django Administration Panel**.  

### 👤 Common User (Non-superadmin)
- Can **register** through a public registration page.  
- Can **log in** using the same **Django Administration page** (common login for both user types).  
- Can **create**, **edit**, and **delete** **only their own posts**.  
- Can **view all other users' posts** (read-only access).  

---

## ⚙️ Technical Details

- **Framework:** Django (Python)
- **Database:** MySQL
- **Frontend:** Django Templates (HTML, CSS)
- **Error Pages:** Custom 404 and 500 error pages for better user experience.
- **APIs:** Django REST Framework-based APIs for CRUD operations on posts.
- **Authentication:** Django’s built-in authentication system with extended user permissions.

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | List all posts |
| `/create/` | POST | Create a new post |
| `/edit/<id>/` | POST | Edit a post |
| `/delete/<id>/` | DELETE | Delete a post |
| `/sql/` |  | Execute the sql queries |
| `/register/` |  | Create a new non-admin login |
| `/db-check/` |  | Checks if db is connected or not |
| `/trigger-error/` |  | Sample view of 500 page |
| `/non-found/` |  | 404 page view type any thing |
| `/admin/login/` |  | Any user can login |
---

## 🧠 Role-Based Access Control Summary

| Role | Create | Edit | Delete | View Others' Posts | Change Others' Permissions |
|------|--------|------|--------|--------------------|-----------------------------|
| Admin | ✅ | ✅ | ✅ | ✅ | ✅ |
| Common User | ✅ | ✅ (own only) | ✅ (own only) | ✅ | ❌ |

---

## 🧩 Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Setup MySQL Database
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3️⃣ Run migrations and create a superuser
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser
```

### 4️⃣ Run the development server
Create a new MySQL database and update your `settings.py` file:
```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🎨 Custom Error Pages

- **404 Page:** Displays when a page is not found.
- **500 Page:** Displays when an internal server error occurs.  
Both pages are fully customized to match the blog’s theme.

---
