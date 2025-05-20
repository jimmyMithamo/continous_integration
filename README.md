# 🛒 Django E-Commerce CI Project

A Django-based e-commerce web application demonstrating best practices in development and deployment, including **Continuous Integration** using **GitHub Actions**.

---

## 🚀 Features

- User authentication (login, logout, register)
- Product catalog with categories
- Shopping cart functionality
- Order processing system
- Media and static file handling
- Continuous Integration setup using GitHub Actions

---

## 🛠 Technologies Used

### Backend
- Python 3.8+
- Django 4.x
- SQLite (default, replaceable with PostgreSQL)

### Frontend
- HTML5, CSS3, Bootstrap
- JavaScript

### DevOps & CI/CD
- GitHub Actions (CI workflows)
- Docker (optional for deployment)
- Gunicorn & Nginx (for production)
- WhiteNoise for static files

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jimmyMithamo/continous_integration.git
cd continous_integration
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🤖 Continuous Integration

This project uses **GitHub Actions** for automated testing and linting on every push and pull request. The workflow file is located at `.github/workflows/deployment.yml`.

---

## 📦 Deployment

For production deployment, consider using Docker, Gunicorn, and Nginx. Update environment variables and static/media file settings as needed.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Bootstrap](https://getbootstrap.com/)
