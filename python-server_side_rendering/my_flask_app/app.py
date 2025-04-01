# Import section - core libraries needed
from flask import Flask, render_template

# App initialization
app = Flask(__name__)

# Route definitions
@app.route('/')
def home():
    return render_template('index.html')

# Additional routes as needed
@app.route('/about')
def about():
    return render_template('about.html')

# App execution - this runs the application
if __name__ == '__main__':
    app.run(debug=True)