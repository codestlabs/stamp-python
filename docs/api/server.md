# Server API Reference

TCP, WebSocket, and HTTP server implementations.

## Import

```python
from stamp.server import run_server, run_ws, run_http
```

## Overview

Stamp provides three types of network servers:
- **TCP Server** - Basic TCP socket server
- **WebSocket Server** - Real-time bidirectional communication
- **HTTP Server** - HTTP request/response handling

## TCP Server

### run_server(host, port, callback=None, max_connections=5)

Run TCP server.

**Parameters:**
- `host` (str): Host to bind to (e.g., 'localhost', '0.0.0.0')
- `port` (int): Port to listen on
- `callback` (function): Callback function for handling connections (optional)
- `max_connections` (int): Maximum concurrent connections (default: 5)

**Returns:** None

```python
from stamp.server import run_server

def handle_client(client_socket, address):
    print(f"Connection from {address}")
    client_socket.send(b"Hello, Client!")
    client_socket.close()

# Start TCP server
run_server(
    host="localhost",
    port=8080,
    callback=handle_client,
    max_connections=10
)
```

### TCP Server Callback

The callback function receives:
- `client_socket`: Socket object for the client
- `address`: Client address tuple (host, port)

```python
def handle_client(client_socket, address):
    host, port = address
    print(f"Client connected: {host}:{port}")
    
    # Receive data
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    
    # Send response
    response = b"Message received"
    client_socket.send(response)
    
    # Close connection
    client_socket.close()
```

## WebSocket Server

### run_ws(host, port, callback=None, max_connections=5)

Run WebSocket server.

**Parameters:**
- `host` (str): Host to bind to
- `port` (int): Port to listen on
- `callback` (function): Callback for WebSocket messages
- `max_connections` (int): Maximum concurrent connections

**Returns:** None

```python
from stamp.server import run_ws

def handle_websocket(client, message):
    print(f"Received: {message}")
    
    # Send response
    client.send("Echo: " + message)

# Start WebSocket server
run_ws(
    host="localhost",
    port=9000,
    callback=handle_websocket,
    max_connections=10
)
```

### WebSocket Server Callback

The callback function receives:
- `client`: WebSocket client object
- `message`: Received message (string)

```python
def handle_websocket(client, message):
    # Process message
    print(f"Client sent: {message}")
    
    # Broadcast to all clients
    if hasattr(client, 'server'):
        for c in client.server.clients:
            c.send(f"Broadcast: {message}")
    
    # Send individual response
    client.send(f"Echo: {message}")
```

## HTTP Server

### run_http(host, port, routes=None, max_connections=5)

Run HTTP server.

**Parameters:**
- `host` (str): Host to bind to
- `port` (int): Port to listen on
- `routes` (dict): Route handlers (path -> callback)
- `max_connections` (int): Maximum concurrent connections

**Returns:** None

```python
from stamp.server import run_http

def home_page(request):
    return "Hello, World!"

def about_page(request):
    return "About Page"

# Define routes
routes = {
    "/": home_page,
    "/about": about_page
}

# Start HTTP server
run_http(
    host="localhost",
    port=8000,
    routes=routes,
    max_connections=10
)
```

### HTTP Routes

Routes are defined as a dictionary mapping paths to handler functions.

```python
def handle_get(request):
    method = request.get('method', 'GET')
    path = request.get('path', '/')
    
    return f"Method: {method}, Path: {path}"

# Route handlers
routes = {
    "/": lambda req: "Home Page",
    "/about": lambda req: "About Us",
    "/api/data": handle_get
}
```

### HTTP Request Object

The request object contains:
- `method`: HTTP method (GET, POST, etc.)
- `path`: Request path
- `headers`: HTTP headers
- `body`: Request body (for POST/PUT)

```python
def handle_request(request):
    method = request.get('method')
    path = request.get('path')
    
    if method == 'GET':
        return f"GET {path}"
    elif method == 'POST':
        return f"POST {path}"
    else:
        return "Method not allowed"
```

## Usage Examples

### Simple TCP Echo Server

```python
from stamp.server import run_server

def echo_handler(client_socket, address):
    print(f"Connection from {address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        
        # Echo back
        client_socket.send(data)
    
    client_socket.close()

run_server(host="localhost", port=8080, callback=echo_handler)
```

### WebSocket Chat Server

```python
from stamp.server import run_ws

clients = []

def chat_handler(client, message):
    print(f"Message: {message}")
    
    # Broadcast to all clients
    for c in clients:
        c.send(f"User: {message}")

run_ws(host="localhost", port=9000, callback=chat_handler)
```

### Simple HTTP Server

```python
from stamp.server import run_http

routes = {
    "/": lambda req: "<h1>Hello, World!</h1>",
    "/api": lambda req: '{"status": "ok"}'
}

run_http(host="localhost", port=8000, routes=routes)
```

### RESTful API

```python
from stamp.server import run_http
import json

def get_data(request):
    return json.dumps({"data": [1, 2, 3]})

def post_data(request):
    body = request.get('body', '')
    return json.dumps({"received": body})

routes = {
    "/api/data": lambda req: get_data(req) if req.get('method') == 'GET' else post_data(req)
}

run_http(host="localhost", port=8000, routes=routes)
```

### Multi-Route HTTP Server

```python
from stamp.server import run_http

def home(request):
    return "<h1>Home</h1><p>Welcome</p>"

def about(request):
    return "<h1>About</h1><p>Info</p>"

def contact(request):
    return "<h1>Contact</h1><p>Email us</p>"

routes = {
    "/": home,
    "/about": about,
    "/contact": contact
}

run_http(host="localhost", port=8000, routes=routes)
```

## Server Options

### Host Binding

```python
# Localhost only
run_server(host="localhost", port=8080)

# All interfaces
run_server(host="0.0.0.0", port=8080)

# Specific IP
run_server(host="192.168.1.100", port=8080)
```

### Port Selection

```python
# Different ports
run_server(host="localhost", port=8080)  # TCP
run_ws(host="localhost", port=9000)      # WebSocket
run_http(host="localhost", port=8000)    # HTTP
```

### Connection Limits

```python
# Limit concurrent connections
run_server(host="localhost", port=8080, max_connections=5)
run_ws(host="localhost", port=9000, max_connections=10)
run_http(host="localhost", port=8000, max_connections=20)
```

## Error Handling

```python
from stamp.server import run_server

def safe_handler(client_socket, address):
    try:
        # Handle connection
        data = client_socket.recv(1024)
        client_socket.send(b"Response")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

run_server(host="localhost", port=8080, callback=safe_handler)
```

## Notes

- Servers run until interrupted (Ctrl+C)
- TCP server is basic - for production, consider dedicated server libraries
- WebSocket server supports bidirectional communication
- HTTP server supports GET, POST, PUT, DELETE methods
- All servers support concurrent connections
- Use `0.0.0.0` to bind to all network interfaces
- Default ports: TCP 8080, WebSocket 9000, HTTP 8000

---

See [Server Demo](../examples/server-demo.md) for complete examples.
See [Networking Guide](../guides/networking-guide.md) for detailed guide.
