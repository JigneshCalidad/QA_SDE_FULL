# Getting Started Guide

## 🚀 Quick Start

Welcome! This guide will help you get started with your full-stack web development journey.

---

## Step 1: Set Up Your Environment

### Install Python

Make sure you have Python 3.8+ installed:

```bash
python --version
# Should show Python 3.8 or higher
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### Install Git

Make sure Git is installed:

```bash
git --version
```

If not installed, download from [git-scm.com](https://git-scm.com/downloads)

---

## Step 2: Set Up Virtual Environment

**Why**: Virtual environments keep your project dependencies isolated.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all the packages you'll need for the projects.

---

## Step 4: Start Learning

### Recommended Learning Path

1. **Start with Foundations** (`01_foundations/`)
   - Read `web_fundamentals/README.md`
   - Run `web_fundamentals/http_demo.py`
   - Understand how HTTP works

2. **Learn Backend** (`02_backend/`)
   - Start with Flask (`flask/README.md`)
   - Run `flask/basic_app.py`
   - Complete Flask exercises

3. **Explore FastAPI** (`02_backend/fastapi/`)
   - Read the README
   - Run `fastapi/basic_app.py`
   - Compare with Flask

4. **Understand Databases** (`02_backend/databases/`)
   - Learn SQL basics
   - Try SQLAlchemy ORM
   - Build apps with databases

5. **Frontend Integration** (`03_frontend/integration/`)
   - Learn how frontend talks to backend
   - Build a simple full-stack app

6. **Build Projects** (`04_fullstack/projects/`)
   - Start with `project_01_basic_api/`
   - Build complete applications

7. **Testing** (`06_testing/`)
   - Write tests for your projects
   - Leverage your QA expertise

8. **Production** (`05_production/`)
   - Learn Docker
   - Deploy your applications

---

## Step 5: Your First Project

### Run the Flask Demo

```bash
cd 02_backend/flask
python basic_app.py
```

Visit `http://localhost:5000` in your browser.

### Run the FastAPI Demo

```bash
cd 02_backend/fastapi
python basic_app.py
```

Visit `http://localhost:8000/docs` to see automatic API documentation!

---

## 💡 Learning Tips

1. **Don't Rush**: Understanding depth is more valuable than speed
2. **Code Along**: Type out examples, don't just read them
3. **Experiment**: Change code, break things, learn from mistakes
4. **Build Projects**: Apply what you learn immediately
5. **Ask Questions**: If something doesn't make sense, dig deeper
6. **Use Your QA Background**: Test everything, think about edge cases

---

## 🐛 Troubleshooting

### Virtual Environment Issues

**Problem**: `python: command not found`
**Solution**: Use `python3` instead of `python`

**Problem**: `pip: command not found`
**Solution**: Use `python -m pip` instead

### Port Already in Use

**Problem**: `Address already in use`
**Solution**: 
- Change the port in your app
- Or stop the other process using that port

### Import Errors

**Problem**: `ModuleNotFoundError`
**Solution**: 
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

---

## 📚 Additional Resources

- **Python Docs**: [docs.python.org](https://docs.python.org/)
- **Flask Docs**: [flask.palletsprojects.com](https://flask.palletsprojects.com/)
- **FastAPI Docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
- **SQLAlchemy Docs**: [docs.sqlalchemy.org](https://docs.sqlalchemy.org/)

---

## 🎯 Next Steps

1. Complete the setup above
2. Read the main `README.md` for the learning philosophy
3. Start with `01_foundations/web_fundamentals/README.md`
4. Build your first project!

---

## 💬 Questions?

If you get stuck:
1. Re-read the relevant section
2. Check the code examples
3. Experiment and debug
4. Reflect on what you're trying to learn

---

*"Every expert was once a beginner. Start where you are, use what you have, do what you can."*

**Happy Learning! 🚀**

