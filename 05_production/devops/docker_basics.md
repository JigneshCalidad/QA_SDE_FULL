# Docker Basics: Containerization

## 🌱 Conceptual Overview

**The Big Picture**: Docker packages your application and all its dependencies into a container. This ensures your application runs the same way everywhere — on your laptop, in testing, and in production.

**Why Docker Matters**:
- **Consistency**: Same environment everywhere
- **Isolation**: Applications don't interfere with each other
- **Portability**: Run anywhere Docker runs
- **Scalability**: Easy to scale containers
- **Simplicity**: One command to run your app

**Key Concepts**:
- **Image**: Blueprint for a container
- **Container**: Running instance of an image
- **Dockerfile**: Instructions for building an image
- **Docker Compose**: Orchestrate multiple containers

---

## 🛠️ Hands-On: Dockerizing a Flask App

### Step 1: Create a Dockerfile

**File**: `Dockerfile`
```dockerfile
# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

### Step 2: Build the Image

```bash
docker build -t my-flask-app .
```

### Step 3: Run the Container

```bash
docker run -p 5000:5000 my-flask-app
```

**What This Does**:
- Builds an image from your Dockerfile
- Runs a container from that image
- Maps port 5000 from container to host

---

## 📚 Key Takeaways

1. **Docker packages applications**: Everything needed to run
2. **Containers are isolated**: Don't interfere with each other
3. **Dockerfiles define images**: Instructions for building
4. **Docker Compose orchestrates**: Multiple containers together

---

*"Docker makes deployment simple: build once, run anywhere."*

