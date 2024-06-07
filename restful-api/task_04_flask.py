from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = request.get_json()
        users[user['username']] = user
        return jsonify({"message": "User added", "user" : user})

@app.route('/users/<username>')
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()