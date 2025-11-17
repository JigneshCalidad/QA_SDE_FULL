"""
Basic FastAPI Application

This demonstrates core FastAPI concepts:
- Async/await
- Pydantic models for validation
- Automatic API documentation
- Error handling
- Dependency injection
"""

from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Create FastAPI application
app = FastAPI(
    title="FastAPI Demo",
    description="A demonstration of FastAPI features",
    version="1.0.0"
)

# In-memory data stores
users = []
posts = []


# ============================================================================
# Pydantic Models
# ============================================================================

class UserCreate(BaseModel):
    """Model for creating a user."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)


class UserResponse(BaseModel):
    """Model for user response."""
    id: int
    name: str
    email: str
    age: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostCreate(BaseModel):
    """Model for creating a post."""
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    user_id: int


class PostResponse(BaseModel):
    """Model for post response."""
    id: int
    title: str
    content: str
    user_id: int
    author: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============================================================================
# Dependencies
# ============================================================================

def get_user_by_id(user_id: int) -> dict:
    """Dependency to get user by ID."""
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ============================================================================
# User Endpoints
# ============================================================================

@app.get("/", tags=["General"])
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to FastAPI Demo",
        "docs": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json"
    }


@app.get("/users", response_model=List[UserResponse], tags=["Users"])
async def get_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of users to return"),
    search: Optional[str] = Query(None, description="Search users by name")
):
    """
    Get all users with optional pagination and search.
    
    - **skip**: Number of users to skip (for pagination)
    - **limit**: Maximum number of users to return
    - **search**: Optional search term to filter by name
    """
    filtered_users = users
    
    # Apply search filter if provided
    if search:
        filtered_users = [
            u for u in filtered_users
            if search.lower() in u['name'].lower()
        ]
    
    # Apply pagination
    paginated_users = filtered_users[skip:skip + limit]
    
    return paginated_users


@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
async def get_user(user_id: int):
    """
    Get a specific user by ID.
    
    - **user_id**: The ID of the user to retrieve
    """
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", response_model=UserResponse, status_code=201, tags=["Users"])
async def create_user(user: UserCreate):
    """
    Create a new user.
    
    - **name**: User's full name (1-100 characters)
    - **email**: User's email address (must be valid email)
    - **age**: User's age (0-150)
    """
    # Check if email already exists
    if any(u['email'] == user.email for u in users):
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )
    
    # Create new user
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now()
    }
    
    users.append(new_user)
    return new_user


@app.delete("/users/{user_id}", status_code=204, tags=["Users"])
async def delete_user(user_id: int):
    """
    Delete a user by ID.
    
    - **user_id**: The ID of the user to delete
    """
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    users.remove(user)
    return None


# ============================================================================
# Post Endpoints
# ============================================================================

@app.get("/posts", response_model=List[PostResponse], tags=["Posts"])
async def get_posts(
    user_id: Optional[int] = Query(None, description="Filter posts by user ID"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """
    Get all posts with optional filtering and pagination.
    
    - **user_id**: Optional filter by user ID
    - **skip**: Number of posts to skip
    - **limit**: Maximum number of posts to return
    """
    filtered_posts = posts
    
    # Filter by user_id if provided
    if user_id:
        filtered_posts = [p for p in filtered_posts if p['user_id'] == user_id]
    
    # Apply pagination
    paginated_posts = filtered_posts[skip:skip + limit]
    
    return paginated_posts


@app.get("/posts/{post_id}", response_model=PostResponse, tags=["Posts"])
async def get_post(post_id: int):
    """
    Get a specific post by ID.
    
    - **post_id**: The ID of the post to retrieve
    """
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.post("/posts", response_model=PostResponse, status_code=201, tags=["Posts"])
async def create_post(post: PostCreate, user: dict = Depends(get_user_by_id)):
    """
    Create a new post.
    
    - **title**: Post title (1-200 characters)
    - **content**: Post content
    - **user_id**: ID of the user creating the post
    
    Note: The user_id is validated via dependency injection.
    """
    # User is already validated by dependency
    new_post = {
        "id": len(posts) + 1,
        "title": post.title,
        "content": post.content,
        "user_id": post.user_id,
        "author": user['name'],
        "created_at": datetime.now()
    }
    
    posts.append(new_post)
    return new_post


@app.delete("/posts/{post_id}", status_code=204, tags=["Posts"])
async def delete_post(post_id: int):
    """
    Delete a post by ID.
    
    - **post_id**: The ID of the post to delete
    """
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    posts.remove(post)
    return None


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """Handle value errors."""
    return HTTPException(status_code=400, detail=str(exc))


# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("FastAPI Application Starting")
    print("=" * 60)
    print("\nAvailable endpoints:")
    print("  GET  /              - API information")
    print("  GET  /docs          - Swagger UI documentation")
    print("  GET  /redoc         - ReDoc documentation")
    print("  GET  /users         - Get all users")
    print("  POST /users         - Create user")
    print("  GET  /users/{id}    - Get user by ID")
    print("  DELETE /users/{id}  - Delete user")
    print("  GET  /posts         - Get all posts")
    print("  POST /posts         - Create post")
    print("  GET  /posts/{id}    - Get post by ID")
    print("  DELETE /posts/{id}  - Delete post")
    print("\nServer running at http://localhost:8000")
    print("Documentation at http://localhost:8000/docs")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

