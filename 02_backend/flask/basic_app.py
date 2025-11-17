"""
Basic Flask Application

This is a simple Flask app that demonstrates core concepts:
- Routing
- Request handling
- Response generation
- Error handling
"""

from flask import Flask, request, jsonify, render_template_string

# Create Flask application instance
app = Flask(__name__)

# In-memory data store (for demonstration)
# In production, you'd use a database
users = []
posts = []


# ============================================================================
# Basic Routes
# ============================================================================

@app.route('/')
def home():
    """Home page route."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Demo</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; }
            .endpoint { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
            code { background: #e8e8e8; padding: 2px 6px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <h1>Welcome to Flask Demo</h1>
        <p>This is a basic Flask application demonstrating core concepts.</p>
        
        <h2>Available Endpoints:</h2>
        <div class="endpoint">
            <strong>GET /</strong> - This page
        </div>
        <div class="endpoint">
            <strong>GET /api/users</strong> - Get all users
        </div>
        <div class="endpoint">
            <strong>POST /api/users</strong> - Create a user (send JSON: {"name": "...", "email": "..."})
        </div>
        <div class="endpoint">
            <strong>GET /api/users/&lt;id&gt;</strong> - Get user by ID
        </div>
        <div class="endpoint">
            <strong>GET /api/posts</strong> - Get all posts
        </div>
        <div class="endpoint">
            <strong>POST /api/posts</strong> - Create a post (send JSON: {"title": "...", "content": "...", "user_id": 1})
        </div>
    </body>
    </html>
    """
    return render_template_string(html)


# ============================================================================
# User API Endpoints
# ============================================================================

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get all users.
    
    Returns:
        JSON array of all users
    """
    return jsonify({
        'users': users,
        'count': len(users)
    })


@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    
    Expected JSON:
        {
            "name": "User Name",
            "email": "user@example.com"
        }
    
    Returns:
        JSON object of created user with 201 status code
    """
    # Get JSON data from request
    data = request.json
    
    # Validate required fields
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400
    
    if not data.get('email'):
        return jsonify({'error': 'Email is required'}), 400
    
    # Check if email already exists
    if any(user['email'] == data['email'] for user in users):
        return jsonify({'error': 'Email already exists'}), 409
    
    # Create new user
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    
    users.append(new_user)
    
    # Return created user with 201 status code
    return jsonify(new_user), 201


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a specific user by ID.
    
    Args:
        user_id: The ID of the user to retrieve
    
    Returns:
        JSON object of user, or 404 if not found
    """
    # Find user by ID
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by ID.
    
    Args:
        user_id: The ID of the user to delete
    
    Returns:
        204 No Content on success, 404 if not found
    """
    global users
    
    # Find and remove user
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user:
        users.remove(user)
        return '', 204  # 204 No Content for successful deletion
    else:
        return jsonify({'error': 'User not found'}), 404


# ============================================================================
# Post API Endpoints
# ============================================================================

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """
    Get all posts.
    
    Query Parameters:
        user_id (optional): Filter posts by user ID
    
    Returns:
        JSON array of posts
    """
    # Get query parameter
    user_id = request.args.get('user_id', type=int)
    
    # Filter posts if user_id provided
    filtered_posts = posts
    if user_id:
        filtered_posts = [p for p in posts if p['user_id'] == user_id]
    
    return jsonify({
        'posts': filtered_posts,
        'count': len(filtered_posts)
    })


@app.route('/api/posts', methods=['POST'])
def create_post():
    """
    Create a new post.
    
    Expected JSON:
        {
            "title": "Post Title",
            "content": "Post content...",
            "user_id": 1
        }
    
    Returns:
        JSON object of created post with 201 status code
    """
    data = request.json
    
    # Validate required fields
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    if not data.get('content'):
        return jsonify({'error': 'Content is required'}), 400
    
    if not data.get('user_id'):
        return jsonify({'error': 'user_id is required'}), 400
    
    # Verify user exists
    user = next((u for u in users if u['id'] == data['user_id']), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Create new post
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content'],
        'user_id': data['user_id'],
        'author': user['name']
    }
    
    posts.append(new_post)
    
    return jsonify(new_post), 201


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """
    Get a specific post by ID.
    
    Args:
        post_id: The ID of the post to retrieve
    
    Returns:
        JSON object of post, or 404 if not found
    """
    post = next((p for p in posts if p['id'] == post_id), None)
    
    if post:
        return jsonify(post)
    else:
        return jsonify({'error': 'Post not found'}), 404


# ============================================================================
# Error Handlers
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Flask Application Starting")
    print("=" * 60)
    print("\nAvailable endpoints:")
    print("  GET  /              - Home page")
    print("  GET  /api/users     - Get all users")
    print("  POST /api/users     - Create user")
    print("  GET  /api/users/<id> - Get user by ID")
    print("  DELETE /api/users/<id> - Delete user")
    print("  GET  /api/posts     - Get all posts")
    print("  POST /api/posts     - Create post")
    print("  GET  /api/posts/<id> - Get post by ID")
    print("\nServer running at http://localhost:5000")
    print("=" * 60)
    
    # Run development server
    # debug=True enables auto-reload and better error messages
    app.run(debug=True, host='0.0.0.0', port=5000)

