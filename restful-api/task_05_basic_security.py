#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'someSuperSuperSecretKey'
jwt = JWTManager(app)

users = {
        "user1": {"password": generate_password_hash("password"), "role": "user"},
        "admin1": {"password": generate_password_hash("adminpassword"), "role": "admin"}
        }


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username).get("password"), password):
        return username

@app.route("/signup", methods=["POST"])
def signup():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username:
        return jsonify({"error": "Missing username"}), 400
    if not password:
        return jsonify({"error": "Missing password"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {"username": username, "password": generate_password_hash(password), "role": "user"}
    return jsonify({"message": "User created", "user": users[username]})

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username:
        return jsonify({"error": "Missing username"}), 400
    if not password:
        return jsonify({"error": "Missing password"}), 400
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token})

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted"})

@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Forbidden"}), 403
    return jsonify({"message": "Admin Access: Granted"})

if __name__ == "__main__":
    app.run(debug=True)