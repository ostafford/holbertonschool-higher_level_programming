from flask import Flask, jsonify, request

# Create Flask app instance
# starting the "server" instance
app = Flask(__name__)

# Store users in memory (like a simple database)
# Python Dictionary
user_database = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }

# Decorator '@' is like a receptionist delegating the incoming call
@app.route('/')
def home():
    try:
        return "Welcome to the Flask API!"
    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500
    
@app.route('/data')
def get_data():
    try:
        # get list of usernames from 'user_database'
        return jsonify(list(user_database.keys()))
        # jsonify -> converter (Python to JSON)
        # list() -> convert user_database to python 'list' format
        # dict_name.keys() -> extracting keys only and storing them in list format
    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500
    
@app.route('/status')
def status():
    try:
        return "OK"
    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500
    
@app.route('/users/<username>')
# username condition is used because that is getting parsed
def user_username(username):
# The variable name must match what's in the <...> in the route
    try:
        # check if username exists
        if username in user_database:
            return jsonify(user_database[username])
        # jsonify -> converter (Python to JSON)
        # user_database[] -> show converted data with parsing [argument]
        else:
            return jsonify({"error": "user not found"}), 404
        
    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500

@app.route('/add_user', methods=['POST'])
# methods=[] -> indicates what methods this endpoint accepts
def add_user():
    try:
        # Converts incoming JSON data to Python dictionary
        user_data = request.get_json()

        # Check if username field exists with data in it
        # Did the user fill out the field.
        if 'username' not in user_data:
            return jsonify({"error": "Username is required"}), 400

        # Get username data from username field
        username = user_data['username']
        # Storing all (POST) form data to 'user_database'
        # 'username' will be the data that changes
        # everything else will stay the same (if any)
        user_database[username] = user_data

        # Return success response to client (browser)
        return jsonify({
            "message": "User added",
            "user": user_data
        }), 201

    except Exception as dry_error:
        return jsonify({"error": str(dry_error)}), 500

if __name__ == "__main__":
    app.run()
