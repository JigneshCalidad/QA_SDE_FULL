"""
HTTP Fundamentals Demonstration

This script demonstrates how HTTP requests work at a fundamental level.
Understanding this helps you see what frameworks like Flask and FastAPI do under the hood.
"""

import socket
import ssl
from urllib.parse import urlparse


def make_http_request(url: str, method: str = "GET", headers: dict = None, body: str = None):
    """
    Make a raw HTTP request without using libraries like requests.
    
    This shows you what's happening at the lowest level.
    
    Args:
        url: The URL to request
        method: HTTP method (GET, POST, etc.)
        headers: Additional headers to send
        body: Request body (for POST/PUT)
    
    Returns:
        The raw HTTP response
    """
    # Parse the URL
    parsed = urlparse(url)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == 'https' else 80)
    path = parsed.path or '/'
    
    # Create socket connection
    if parsed.scheme == 'https':
        # For HTTPS, we need SSL
        context = ssl.create_default_context()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = context.wrap_socket(sock, server_hostname=host)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to server
        sock.connect((host, port))
        
        # Build HTTP request
        request_lines = [
            f"{method} {path} HTTP/1.1",
            f"Host: {host}",
            "Connection: close",
        ]
        
        # Add custom headers
        if headers:
            for key, value in headers.items():
                request_lines.append(f"{key}: {value}")
        
        # Add body if present
        if body:
            request_lines.append(f"Content-Length: {len(body)}")
            request_lines.append("")  # Empty line before body
            request_lines.append(body)
        else:
            request_lines.append("")  # Empty line to end headers
        
        # Send request
        request = "\r\n".join(request_lines)
        sock.sendall(request.encode())
        
        # Receive response
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
        
        return response.decode('utf-8', errors='ignore')
    
    finally:
        sock.close()


def parse_http_response(response: str):
    """
    Parse an HTTP response into its components.
    
    This shows you the structure of HTTP responses.
    """
    lines = response.split('\r\n')
    
    # First line is status line
    status_line = lines[0]
    protocol, status_code, status_message = status_line.split(' ', 2)
    
    # Headers are until first empty line
    headers = {}
    body_start = 0
    for i, line in enumerate(lines[1:], 1):
        if not line:
            body_start = i + 1
            break
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    
    # Body is everything after headers
    body = '\r\n'.join(lines[body_start:])
    
    return {
        'protocol': protocol,
        'status_code': int(status_code),
        'status_message': status_message,
        'headers': headers,
        'body': body
    }


def demonstrate_http():
    """
    Demonstrate making HTTP requests and parsing responses.
    """
    print("=" * 60)
    print("HTTP Fundamentals Demonstration")
    print("=" * 60)
    print()
    
    # Example 1: Simple GET request
    print("Example 1: Making a GET request to httpbin.org")
    print("-" * 60)
    try:
        response = make_http_request("http://httpbin.org/get")
        parsed = parse_http_response(response)
        
        print(f"Status: {parsed['status_code']} {parsed['status_message']}")
        print(f"Headers: {len(parsed['headers'])} headers received")
        print(f"Body length: {len(parsed['body'])} characters")
        print()
        print("Response body (first 200 chars):")
        print(parsed['body'][:200])
        print()
    except Exception as e:
        print(f"Error: {e}")
        print("(This might fail if httpbin.org is not accessible)")
        print()
    
    # Example 2: POST request with body
    print("Example 2: Making a POST request with data")
    print("-" * 60)
    try:
        post_data = '{"name": "Test User", "email": "test@example.com"}'
        headers = {
            "Content-Type": "application/json"
        }
        response = make_http_request(
            "http://httpbin.org/post",
            method="POST",
            headers=headers,
            body=post_data
        )
        parsed = parse_http_response(response)
        
        print(f"Status: {parsed['status_code']} {parsed['status_message']}")
        print(f"Content-Type: {parsed['headers'].get('Content-Type', 'N/A')}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()
    
    print("=" * 60)
    print("Key Insights:")
    print("=" * 60)
    print("1. HTTP is just text sent over a socket connection")
    print("2. Requests have: method, path, headers, optional body")
    print("3. Responses have: status line, headers, body")
    print("4. Libraries like 'requests' do this for you, but")
    print("   understanding the fundamentals helps you debug")
    print("   and understand what's happening under the hood.")
    print()


if __name__ == "__main__":
    demonstrate_http()

