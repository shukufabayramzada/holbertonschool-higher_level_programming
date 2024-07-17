from flask import Flask, render_template, request
import sqlite3
import json
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
        items = data.get('items', [])
        return render_template('items.html', items=items)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def fetch_data_from_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        products.append(product)

    print(products)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    file_path = ''

    if source == 'json':
        file_path = 'products.json'
    elif source == 'csv':
        file_path = 'products.csv'
    elif source == 'sql':
        products = fetch_data_from_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source")

    if source != 'sql' and not os.path.exists(file_path):
        return render_template('product_display.html', error="File not found")

    if source == 'json':
        products = read_json(file_path)
    elif source == 'csv':
        products = read_csv(file_path)

    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid id")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
