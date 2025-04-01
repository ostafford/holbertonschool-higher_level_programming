from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read JSON data
def read_json_data():
    with open('products.json', 'r') as file:
        return json.load(file)

# Function to read CSV data
def read_csv_data():
    products = []
    with open('products.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convert id to integer and price to float
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Function to read SQLite data
def read_sql_data():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        
        for row in cursor.fetchall():
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        # Handle database errors
        print(f"Database error: {e}")
        return []

@app.route('/products')
def products():
    # Get query parameters
    source = request.args.get('source', '')
    product_id = request.args.get('id')
    
    # Initialize variables
    products_data = []
    error_message = None
    
    # Process based on source parameter
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    elif source == 'sql':
        products_data = read_sql_data()
    else:
        error_message = "Wrong source"
    
    # Filter by ID if provided
    if product_id and not error_message:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p['id'] == product_id]
            if filtered_products:
                products_data = filtered_products
            else:
                error_message = "Product not found"
        except ValueError:
            error_message = "Invalid ID format"
    
    # Render the template with the data
    return render_template('product_display.html', 
                          products=products_data, 
                          error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
