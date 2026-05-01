from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route('/')
def home():
    return "Backend running"

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json

    for user in users:
        if user["email"] == data.get("email"):
            return jsonify({"success": False, "message": "Email already exists"})

    users.append(data)

    return jsonify({"success": True})

if __name__ == '__main__':
    print("Server starting...")
    app.run(port=5000, debug=True)