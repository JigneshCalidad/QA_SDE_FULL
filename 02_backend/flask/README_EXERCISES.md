# Flask Exercises: Hands-On Practice

## 🎯 Purpose

These exercises help you practice Flask concepts through hands-on coding. Complete them in order, as each builds on the previous one.

---

## Exercise 1: Basic Routing

**Goal**: Create routes for a simple blog.

**Requirements**:
- `GET /` - Home page with welcome message
- `GET /about` - About page
- `GET /contact` - Contact page

**Stretch Goal**: Add a navigation menu that links between pages.

---

## Exercise 2: Dynamic Routes

**Goal**: Create routes that accept parameters.

**Requirements**:
- `GET /user/<username>` - Display user profile
- `GET /post/<int:post_id>` - Display specific post
- `GET /category/<category_name>` - Display posts in category

**Stretch Goal**: Handle invalid IDs gracefully (return 404).

---

## Exercise 3: HTTP Methods

**Goal**: Handle different HTTP methods for the same resource.

**Requirements**:
- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create a new todo
- `GET /api/todos/<id>` - Get specific todo
- `PUT /api/todos/<id>` - Update todo
- `DELETE /api/todos/<id>` - Delete todo

**Data Structure**:
```python
{
    "id": 1,
    "title": "Learn Flask",
    "completed": False
}
```

**Stretch Goal**: Add validation (title required, max length 200 characters).

---

## Exercise 4: Request Data Handling

**Goal**: Extract and use data from requests.

**Requirements**:
- Accept JSON data in POST requests
- Accept query parameters in GET requests
- Accept form data
- Handle missing/invalid data gracefully

**Example**:
```python
# POST /api/users with JSON
{
    "name": "John",
    "email": "john@example.com"
}

# GET /api/users?limit=10&offset=0
```

**Stretch Goal**: Add input validation and return appropriate error messages.

---

## Exercise 5: Error Handling

**Goal**: Handle errors gracefully.

**Requirements**:
- Return appropriate status codes (400, 404, 500)
- Return JSON error messages
- Log errors (use print for now)
- Handle edge cases (empty data, invalid IDs, etc.)

**Example Error Response**:
```json
{
    "error": "User not found",
    "code": "NOT_FOUND",
    "status": 404
}
```

---

## Exercise 6: Templates

**Goal**: Use templates to generate HTML.

**Requirements**:
- Create a base template
- Create templates for different pages
- Pass data to templates
- Use template inheritance

**Template Structure**:
```
templates/
├── base.html      # Base template with navigation
├── home.html      # Home page
├── user.html      # User profile
└── post.html      # Post detail
```

**Stretch Goal**: Add CSS styling and make it responsive.

---

## Exercise 7: Complete CRUD Application

**Goal**: Build a complete todo application.

**Requirements**:
- Create, Read, Update, Delete todos
- List all todos
- Filter todos (completed, pending)
- Search todos
- Use templates for the UI
- Use JSON API for programmatic access

**Features**:
- Add a todo
- Mark todo as complete
- Delete todo
- Edit todo
- Filter by status
- Search by title

**Stretch Goal**: Add categories/tags to todos.

---

## Exercise 8: API Design

**Goal**: Design and implement a RESTful API.

**Requirements**:
- Design API for a blog platform
- Implement all CRUD operations
- Use proper HTTP methods
- Return appropriate status codes
- Include error handling
- Document your API

**Resources**:
- Posts (title, content, author, date)
- Comments (content, post_id, author)
- Users (name, email)

**API Endpoints**:
```
GET    /api/posts
POST   /api/posts
GET    /api/posts/<id>
PUT    /api/posts/<id>
DELETE /api/posts/<id>

GET    /api/posts/<id>/comments
POST   /api/posts/<id>/comments

GET    /api/users
POST   /api/users
GET    /api/users/<id>
```

**Stretch Goal**: Add pagination, filtering, and sorting.

---

## Exercise 9: Testing

**Goal**: Write tests for your Flask application.

**Requirements**:
- Test all routes
- Test error cases
- Test with different HTTP methods
- Test request/response data

**Use pytest-flask**:
```python
import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert 'users' in response.json
```

**Stretch Goal**: Achieve 80%+ code coverage.

---

## Exercise 10: Project — Personal Blog API

**Goal**: Build a complete blog API with all features.

**Requirements**:
- User authentication (basic)
- Create, read, update, delete posts
- Add comments to posts
- Like/unlike posts
- User profiles
- Error handling
- Input validation
- API documentation

**Bonus Features**:
- Pagination
- Search
- Categories/tags
- Image uploads
- Rate limiting

---

## 💡 Reflection Questions

After completing exercises:

1. What patterns did you notice across different exercises?
2. How did error handling improve your code?
3. What was the most challenging part?
4. How does understanding Flask help you understand other frameworks?
5. How would you test each feature you built?

---

## 🚀 Next Steps

Once you've completed these exercises:

1. Build a real project (choose something you're interested in)
2. Learn about Flask extensions (SQLAlchemy, Flask-Login, etc.)
3. Move to FastAPI to learn async/await
4. Explore Django to see a full-featured framework

---

*"Practice builds intuition. The more you code, the more patterns you'll recognize."*

