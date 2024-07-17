from flask import Flask, render_template
import json
import os

app = Flask(__name__)

app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get('items', [])
            return render_template('items.html', items = items)
    except FileNotFoundError:
        return "Items file not found", 404
    except json.JSONDecodeError:
        return "Error decoding JSON", 500
        
    

if __name__ == '__main__':
    app.run(debug=True)