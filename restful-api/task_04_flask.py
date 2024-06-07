#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

all_users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    usernames = list(all_users.keys())
    return jsonify(usernames)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = request.get_json()
        all_users[user['username']] = user
        return jsonify({"message": "User added", "user" : user})

@app.route('/users/<username>')
def user(username):
    if username in all_users:
        return jsonify(all_users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()