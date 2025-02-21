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

@app.route('/add_user')
pass

if __name__ == "__main__":
    app.run()

