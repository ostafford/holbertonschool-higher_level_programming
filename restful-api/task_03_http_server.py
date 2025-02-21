# Imports
# Import pre-built classes from Python's standard library
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


# Our API Class (like a instruction manual for handling requests)
class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
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
        self.wfile.write("Hello, this is a simple GET API!".encode())
        # `self.wfile` is the phone line (output stream)
        # `.write()` is speaking into the phone (sending data)
        # `"message"` is what you want to say (the content)
        # `.encode()` is translating your words into HTTP language (bytes)


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
    httpd.serve_forever()  # Like putting up an "Open" sign and waiting for customers

# Run the server when this file is run directly (not when imported as a module)
if __name__ == "__main__":
    run_server()
