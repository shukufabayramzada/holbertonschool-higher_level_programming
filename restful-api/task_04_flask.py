#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

all_users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    usernames = list(all_users)
    return jsonify(usernames)


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = request.get_json()
        if data is None or data.get('username') is None:
            return jsonify({'error': 'Username is required'}), 400
        if "username" not in user or user["username"] == "":
            return jsonify({"error": "Invalid username"}), 400
        if user['username'] in all_users:
            return jsonify({"error": "User already exists"}), 400
        all_users[user['username']] = user
        return jsonify({"message": "User added", "user": user})


@app.route('/users/<username>')
def user(username):
    if username is None:
        return jsonify({'error': 'Username is required'}), 400
    if username not in all_users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(all_users[username])


@app.route('/status')
def status():
    return "OK"


if __name__ == "__main__":
    app.run()