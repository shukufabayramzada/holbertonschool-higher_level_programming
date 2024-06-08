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
    data = request.json
    if data is None or data.get('username') is None:
        return jsonify({'error': 'Username is required'}), 400
    user = {
        'username': data.get('username'),
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    all_users[user.get('username')] = user
    return jsonify({'message': 'User added', 'user': user}), 201


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