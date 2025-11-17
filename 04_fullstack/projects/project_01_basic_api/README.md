# Project 1: Basic REST API with Flask

## 🎯 Project Goal

Build a complete REST API for a blog platform with:
- User management
- Post creation and management
- Comments on posts
- Proper error handling
- API documentation

---

## 📋 Requirements

### User Endpoints
- `POST /api/users` - Create user
- `GET /api/users` - List all users
- `GET /api/users/<id>` - Get user by ID
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

### Post Endpoints
- `POST /api/posts` - Create post
- `GET /api/posts` - List all posts (with pagination)
- `GET /api/posts/<id>` - Get post by ID
- `PUT /api/posts/<id>` - Update post
- `DELETE /api/posts/<id>` - Delete post

### Comment Endpoints
- `POST /api/posts/<id>/comments` - Add comment to post
- `GET /api/posts/<id>/comments` - Get comments for post

---

## 🏗️ Project Structure

```
project_01_basic_api/
├── app.py                 # Main application
├── models.py              # Data models
├── requirements.txt       # Dependencies
├── README.md             # This file
└── tests/                # Test files
    └── test_api.py
```

---

## 🚀 Getting Started

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Test the API**:
   - Visit `http://localhost:5000/docs` (if using Flask-RESTX)
   - Or use curl/Postman to test endpoints

---

## ✅ Success Criteria

- [ ] All endpoints implemented
- [ ] Proper error handling (404, 400, 500)
- [ ] Input validation
- [ ] API returns JSON
- [ ] Status codes are correct
- [ ] Code is well-organized
- [ ] Basic tests written

---

## 💡 Learning Objectives

By completing this project, you'll understand:
- How to structure a Flask application
- How to design RESTful APIs
- How to handle errors
- How to validate input
- How to test APIs

---

## 🔍 Reflection

After completing the project:
1. What was the most challenging part?
2. How would you improve the API design?
3. What would you add for a production application?
4. How does this project connect to everything you've learned?

---

*"Building complete projects is where learning becomes understanding."*

