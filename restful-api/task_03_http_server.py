# Imports
# Import pre-built classes from Python's standard library
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


# Our API Class (like a instruction manual for handling requests)
class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
        # Step 1: Send HTTP status code 200 (means "OK/Success")
                self.send_response(200)   

        # Step 2: Tell the client what type of data we're sending
        # Structure: self.send_header('Header-Name', 'Header-Value')
                self.send_header('content-type', 'text/plain')
        # Content types we can send:
        # 'application/json' -> JSON Data
        # 'text/html' -> HTML pages

        # Step 3: Signal we're done sending headers (like saying "end of instructions")
                self.end_headers()

        # Step 4: Send the actual message (must be converted to bytes with encode())
        # Structure: self.wfile.write("insert_string_message_here".encode())
                self.wfile.write("Hello, this is a simple GET API call!".encode())
        # `self.wfile` is the phone line (output stream)
        # `.write()` is speaking into the phone (sending data)
        # `"message"` is what you want to say (the content)
        # `.encode()` is translating your words into HTTP language (bytes)
            elif self.path == '/data':
        # Handle data endpoint
                self.send_response(200)
        # Telling client/recipient to expect JSON data
                self.send_header('content-type', 'application/json')
                self.end_headers()
        # Python dictionary structure
                data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
        # Need to convert Python to JSON (serialized) (jason.dumps())
                self.wfile.write(json.dumps(data).encode())
        # Multiple steps happening in one line:
        # 1. json.dumps(data) -> Convert Python dict to JSON string
        # 2. .encode() -> Convert JSON string to bytes for HTTP
        # 3. self.wfile.write() -> Send bytes to client

        # Handle Status endpoint
            elif self.path == '/status':
                self.send_response(200)
                self.send_header('content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("OK".encode())

        # Handle undefined endpoints and error requests
            else:
                self.send_response(404)
                self.send_header('content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("404 Not Found: Endpoint not found".encode())

        except Exception as DRY_error:
        # Central Place to handle ALL errors
            self.send_response(500)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Server Error: {str(DRY_error)}".encode())


# Server startup code (like opening a store)
def run_server():
    # Define where our server will run (localhost means "this computer")
    # Tuple (address, port) - like a full address with street (localhost)and apartment number (8000)
    server_address = ('localhost', 8000)

    # Create server instance using our API handler
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    # HTTPServer = the pre-built server class from Python
    # server_address = where to set up shop (location)
    # SimpleAPIHandler = our instruction manual for handling customers (requests)

    # Start the server (it will run until we stop it with Ctrl+C)
    print("Server running on port 8000...")
    httpd.serve_forever()

# Run the server when this file is run directly (not when imported as a module)
if __name__ == "__main__":
    run_server()
