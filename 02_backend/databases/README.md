# Databases: Storing and Retrieving Data

## 🌱 Conceptual Overview

**The Big Picture**: Web applications need to store data persistently. Databases provide structured, efficient ways to store, retrieve, and manage data.

**Why Databases Matter**:
- **Persistence**: Data survives server restarts
- **Structure**: Organized, queryable data
- **Relationships**: Connect related data
- **Performance**: Optimized for fast queries
- **Concurrency**: Handle multiple users simultaneously

**Types of Databases**:
1. **SQL (Relational)**: Structured data with relationships (PostgreSQL, MySQL, SQLite)
2. **NoSQL (Document)**: Flexible, document-based (MongoDB, CouchDB)
3. **NoSQL (Key-Value)**: Simple key-value pairs (Redis, Memcached)

**This Section Covers**:
- SQL fundamentals
- Working with databases in Python
- ORMs (Object-Relational Mappers)
- Database design
- Migrations

---

## 🎯 Core Concepts

### 1. SQL: The Language of Databases

**Concept**: SQL (Structured Query Language) is how you interact with relational databases.

**Basic Operations** (CRUD):
- **CREATE**: `INSERT INTO users (name, email) VALUES ('John', 'john@example.com')`
- **READ**: `SELECT * FROM users WHERE id = 1`
- **UPDATE**: `UPDATE users SET email = 'new@example.com' WHERE id = 1`
- **DELETE**: `DELETE FROM users WHERE id = 1`

**Why SQL Matters**:
- Standard language (works with most databases)
- Powerful querying (filter, join, aggregate)
- Efficient (databases optimize queries)
- Relational (connect data across tables)

---

### 2. Relational Databases: Tables and Relationships

**Concept**: Relational databases organize data into tables with relationships.

**Key Concepts**:
- **Tables**: Collections of rows (records)
- **Rows**: Individual records
- **Columns**: Fields/attributes
- **Primary Key**: Unique identifier for each row
- **Foreign Key**: Reference to another table
- **Relationships**: One-to-many, many-to-many, one-to-one

**Example Schema**:
```sql
-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- Posts table
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**Why Relationships Matter**:
- **Data Integrity**: Enforce valid relationships
- **Avoid Duplication**: Store data once, reference it
- **Query Power**: Join tables to get related data
- **Normalization**: Organize data efficiently

---

### 3. ORMs: Object-Relational Mappers

**Concept**: ORMs let you work with databases using Python objects instead of SQL.

**Why ORMs Exist**:
- **Productivity**: Write Python instead of SQL
- **Type Safety**: Catch errors at development time
- **Database Agnostic**: Switch databases easily
- **Security**: Prevent SQL injection attacks

**Popular Python ORMs**:
- **SQLAlchemy**: Most popular, very flexible
- **Django ORM**: Built into Django
- **Peewee**: Lightweight, simple
- **Tortoise ORM**: Async ORM for FastAPI

**Example (SQLAlchemy)**:
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
```

**When to Use ORMs**:
- Most web applications
- Rapid development
- When you need database portability

**When to Use Raw SQL**:
- Complex queries
- Performance-critical operations
- Database-specific features

---

### 4. Database Migrations

**Concept**: Migrations track and apply changes to your database schema.

**Why Migrations Matter**:
- **Version Control**: Track schema changes
- **Team Collaboration**: Everyone has same schema
- **Deployment**: Apply changes to production safely
- **Rollback**: Undo changes if needed

**Migration Tools**:
- **Alembic**: For SQLAlchemy
- **Django Migrations**: Built into Django
- **Flask-Migrate**: For Flask

**Example Migration**:
```python
# Migration: Add email column to users table
def upgrade():
    op.add_column('users', sa.Column('email', sa.String(100)))

def downgrade():
    op.drop_column('users', 'email')
```

---

## 🛠️ Hands-On: Working with Databases

### Exercise 1: SQLite Basics

**SQLite** is perfect for learning — it's a file-based database, no server needed.

**File**: `database_demo.py`
```python
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert data
cursor.execute('''
    INSERT INTO users (name, email) VALUES (?, ?)
''', ('John Doe', 'john@example.com'))

# Query data
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print(users)

# Commit and close
conn.commit()
conn.close()
```

**What You Learned**:
- How to connect to a database
- How to create tables
- How to insert data
- How to query data

---

### Exercise 2: Using SQLAlchemy ORM

**File**: `orm_demo.py`
```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

# Create engine and tables
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create user
user = User(name="John Doe", email="john@example.com")
session.add(user)
session.commit()

# Query users
users = session.query(User).all()
print(users)

# Create post
post = Post(title="My First Post", content="Hello!", user_id=user.id)
session.add(post)
session.commit()

# Query with relationship
user = session.query(User).filter(User.id == 1).first()
print(f"User: {user.name}")
print(f"Posts: {[p.title for p in user.posts]}")
```

**What You Learned**:
- How to define models with SQLAlchemy
- How to create relationships
- How to query data
- How to use relationships

---

### Exercise 3: Database with Flask

**File**: `flask_db_app.py`
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**What You Learned**:
- How to integrate databases with Flask
- How to use Flask-SQLAlchemy
- How to create and query models

---

## 🔍 Deep Dive: Database Design

### Normalization

**Concept**: Normalization organizes data to reduce redundancy and improve integrity.

**First Normal Form (1NF)**:
- Each column contains atomic values
- No repeating groups

**Second Normal Form (2NF)**:
- In 1NF
- All non-key columns depend on the full primary key

**Third Normal Form (3NF)**:
- In 2NF
- No transitive dependencies (columns depend only on primary key)

**Why Normalization Matters**:
- Reduces data duplication
- Prevents update anomalies
- Improves data integrity
- Makes queries more efficient

---

### Indexes

**Concept**: Indexes speed up queries by creating lookup structures.

**When to Index**:
- Foreign keys
- Frequently queried columns
- Columns used in WHERE clauses
- Columns used for sorting

**Trade-offs**:
- **Pros**: Faster queries
- **Cons**: Slower inserts/updates, more storage

---

## 📚 Key Takeaways

1. **Databases provide persistence**: Data survives restarts
2. **SQL is the standard**: Works with most databases
3. **ORMs simplify development**: Write Python instead of SQL
4. **Relationships connect data**: Design schemas carefully
5. **Migrations track changes**: Essential for team development
6. **Choose the right tool**: SQL for structure, NoSQL for flexibility

---

## 🎯 Next Steps

1. Complete the hands-on exercises
2. Design a database schema for a blog platform
3. Build a Flask/FastAPI app with a database
4. Learn about database optimization
5. Explore NoSQL databases (MongoDB)

---

## 💡 Reflection

- How does understanding databases help you build better applications?
- When would you choose SQL vs NoSQL?
- How do ORMs simplify development?
- How does your QA background help you test database operations?

---

*"Databases are the memory of your application. Understanding how to store and retrieve data efficiently is fundamental to building great applications."*

