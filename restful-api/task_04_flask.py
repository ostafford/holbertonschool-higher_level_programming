from flask import Flask, jsonify

# Create Flask app instance
# starting the "server" instance
app = Flask(__name__)

# Store users in memory (like a simple database)
# Python Dictionary
user_database = {}

# Decorator '@' is like a receptionist delegating the incoming call
@app.route('/')
def home():
    try:
        return "Welcome to the Flask API!"
    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500
    
@app.route('/data')

@app.route('/status')
def status():
    try:
        return "OK"
    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500
    
@app.route('/users/<username>')

@app.route('/add_user')

if __name__ == "__main__":
    app.run()
