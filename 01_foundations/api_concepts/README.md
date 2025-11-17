# API Concepts: Contracts Between Systems

## 🌱 Conceptual Overview

**The Big Picture**: APIs (Application Programming Interfaces) are contracts that define how different systems communicate. They're the bridges that connect:
- Frontend to backend
- Mobile apps to servers
- Microservices to each other
- Your application to third-party services

**Why This Matters**: As a full-stack developer, you'll spend much of your time:
- Building APIs (backend)
- Consuming APIs (frontend)
- Testing APIs (your QA expertise)
- Integrating with third-party APIs

Understanding API design principles helps you build better, more maintainable systems.

---

## 🎯 Core Concepts

### 1. What is an API?

**Concept**: An API is a contract that defines:
- **What** operations are available
- **How** to request them (endpoints, methods, parameters)
- **What** responses to expect (data format, status codes)

**Real-World Analogy**: Like a restaurant menu:
- **Menu items** = Available operations
- **How to order** = Request format
- **What you get** = Response format

**Why APIs Exist**:
- **Separation of Concerns**: Frontend and backend can be developed independently
- **Reusability**: One API can serve web, mobile, and other clients
- **Scalability**: Different parts can scale independently
- **Integration**: Connect different systems easily

---

### 2. REST: Representational State Transfer

**Concept**: REST is an architectural style for designing APIs. It's based on a few key principles:

**Core Principles**:
1. **Resources**: Everything is a resource (users, posts, comments)
2. **HTTP Methods**: Use HTTP methods correctly (GET, POST, PUT, DELETE)
3. **Stateless**: Each request contains all information needed
4. **Uniform Interface**: Consistent way to interact with resources

**RESTful URL Design**:
```
GET    /users           # Get all users
GET    /users/123       # Get user with ID 123
POST   /users           # Create a new user
PUT    /users/123       # Update user 123 completely
PATCH  /users/123       # Partially update user 123
DELETE /users/123       # Delete user 123
```

**Why REST Matters**:
- **Predictable**: Once you understand one endpoint, you understand them all
- **Standard**: Uses HTTP methods correctly
- **Cacheable**: GET requests can be cached
- **Scalable**: Stateless design scales well

**QA Insight**: RESTful APIs are easier to test because they follow predictable patterns.

---

### 3. HTTP Methods: The Verbs of APIs

**Concept**: HTTP methods define what action to perform.

**The Main Methods**:

**GET** — Retrieve data
- Safe: Doesn't change server state
- Idempotent: Same request = same result
- Cacheable: Responses can be cached
- Example: `GET /users/123`

**POST** — Create new resources
- Not safe: Changes server state
- Not idempotent: Same request can create multiple resources
- Example: `POST /users` (creates a new user)

**PUT** — Replace resource completely
- Not safe: Changes server state
- Idempotent: Same request = same result
- Example: `PUT /users/123` (replaces entire user)

**PATCH** — Partially update resource
- Not safe: Changes server state
- Idempotent: Same request = same result
- Example: `PATCH /users/123` (updates only specified fields)

**DELETE** — Remove resource
- Not safe: Changes server state
- Idempotent: Same request = same result
- Example: `DELETE /users/123`

**Why This Matters**: Using methods correctly makes APIs:
- More intuitive
- Easier to cache
- More secure (GET requests shouldn't change data)
- Easier to test

---

### 4. Status Codes: The Response Language

**Concept**: Status codes communicate what happened with the request.

**Key Status Codes**:

**2xx Success**:
- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `204 No Content`: Success, but no content to return

**3xx Redirection**:
- `301 Moved Permanently`: Resource moved
- `304 Not Modified`: Resource hasn't changed (caching)

**4xx Client Error**:
- `400 Bad Request`: Invalid request format
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Not allowed (even if authenticated)
- `404 Not Found`: Resource doesn't exist
- `422 Unprocessable Entity`: Valid format, but invalid data

**5xx Server Error**:
- `500 Internal Server Error`: Server error
- `502 Bad Gateway`: Upstream server error
- `503 Service Unavailable`: Server temporarily unavailable

**Why This Matters**: Status codes are contracts. They tell clients:
- What happened
- What to do next
- How to handle errors

**QA Insight**: Status codes are test cases. Test for:
- Success cases (2xx)
- Error cases (4xx, 5xx)
- Edge cases (404, 422)

---

### 5. Request and Response Formats

**Concept**: APIs need to agree on data formats.

**Common Formats**:

**JSON** (JavaScript Object Notation):
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```
- Human-readable
- Easy to parse
- Most common for REST APIs

**XML** (eXtensible Markup Language):
```xml
<user>
  <id>123</id>
  <name>John Doe</name>
  <email>john@example.com</email>
</user>
```
- More verbose
- Less common in modern APIs

**Why JSON Dominates**:
- Simpler than XML
- Native to JavaScript (frontend)
- Easy to parse in all languages
- Smaller payload size

---

### 6. API Design Best Practices

**Concept**: Good API design follows consistent patterns.

**Key Principles**:

1. **Consistent Naming**: Use consistent conventions
   - Good: `/users`, `/posts`, `/comments`
   - Bad: `/users`, `/getPosts`, `/comment_list`

2. **Versioning**: Plan for changes
   - `/api/v1/users`
   - `/api/v2/users`

3. **Filtering, Sorting, Pagination**: For list endpoints
   - `GET /users?page=1&limit=10&sort=name&filter=active`

4. **Error Handling**: Consistent error format
   ```json
   {
     "error": {
       "code": "VALIDATION_ERROR",
       "message": "Email is required",
       "field": "email"
     }
   }
   ```

5. **Documentation**: Clear, complete documentation
   - Endpoints
   - Parameters
   - Responses
   - Examples

**Why This Matters**: Well-designed APIs are:
- Easier to use
- Easier to maintain
- Easier to test
- Less error-prone

---

## 🛠️ Hands-On: Building Your First API

### Exercise 1: Design an API

**Goal**: Design a RESTful API for a blog platform.

**Requirements**:
- Users can create, read, update, delete posts
- Users can comment on posts
- Users can like posts

**Your Task**: Design the endpoints:
- What URLs?
- What HTTP methods?
- What request/response formats?
- What status codes?

**Example Design**:
```
GET    /posts              # List all posts
GET    /posts/123          # Get post 123
POST   /posts              # Create post
PUT    /posts/123          # Update post 123
DELETE /posts/123          # Delete post 123

GET    /posts/123/comments # Get comments for post 123
POST   /posts/123/comments # Add comment to post 123

POST   /posts/123/like     # Like post 123
DELETE /posts/123/like     # Unlike post 123
```

**Reflection**: Why did you choose these endpoints? Are they RESTful?

---

### Exercise 2: Test an API

**Goal**: Use Python to interact with a real API.

**Code**:
```python
import requests

# Get all users
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()
print(f"Found {len(users)} users")

# Get specific user
user = requests.get('https://jsonplaceholder.typicode.com/users/1').json()
print(f"User: {user['name']}")

# Create a post
new_post = {
    "title": "My First Post",
    "body": "This is the content",
    "userId": 1
}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=new_post
)
print(f"Created post with ID: {response.json()['id']}")
```

**What This Shows**:
- How to make GET requests
- How to make POST requests
- How to parse JSON responses
- How to send JSON data

**Try This**:
- Update a post (PUT)
- Delete a post (DELETE)
- Handle errors (try invalid IDs)

---

## 🔍 Deep Dive: API Design Patterns

### 1. Resource-Based Design

**Concept**: Design APIs around resources, not actions.

**Bad Design** (Action-based):
```
POST /createUser
POST /updateUser
POST /deleteUser
GET /getUser
```

**Good Design** (Resource-based):
```
POST /users      # Create user
PUT  /users/123  # Update user
DELETE /users/123 # Delete user
GET  /users/123  # Get user
```

**Why Resource-Based is Better**:
- More intuitive
- Follows REST principles
- Easier to cache
- More scalable

---

### 2. Nested Resources

**Concept**: Represent relationships through URL structure.

**Example**: Comments belong to posts
```
GET /posts/123/comments        # Get comments for post 123
POST /posts/123/comments       # Add comment to post 123
GET /posts/123/comments/456    # Get specific comment
```

**When to Nest**:
- If resource only exists in context of parent
- If it makes sense semantically

**When Not to Nest**:
- If resource can exist independently
- If nesting gets too deep (more than 2-3 levels)

---

### 3. Pagination

**Concept**: Limit results to manageable chunks.

**Common Patterns**:
```
# Offset-based
GET /users?page=1&limit=10

# Cursor-based (better for large datasets)
GET /users?cursor=abc123&limit=10
```

**Why Pagination Matters**:
- Performance (don't load millions of records)
- User experience (manageable chunks)
- Server resources (less memory, faster queries)

---

## 📚 Key Takeaways

1. **APIs are contracts**: They define how systems communicate
2. **REST is a style**: Based on resources and HTTP methods
3. **HTTP methods have meaning**: Use them correctly
4. **Status codes communicate**: They tell clients what happened
5. **Consistency matters**: Well-designed APIs follow patterns
6. **Documentation is essential**: APIs are useless without docs

---

## 🎯 Next Steps

1. Complete the hands-on exercises
2. Move to `02_backend/` to start building APIs with Python
3. Practice designing APIs for different scenarios

---

## 💡 Reflection

- How does understanding API design help you as a full-stack developer?
- Why is REST popular? What problems does it solve?
- How does your QA background help you design testable APIs?
- What makes an API "good"? What makes one "bad"?

---

*"APIs are the contracts that make the web work. Understanding how to design them well is understanding how to build systems that scale."*

