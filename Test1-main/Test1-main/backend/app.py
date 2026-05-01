from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.before_request
def handle_options():
    if request.method == "OPTIONS":
        return '', 200


users = []
reset_tokens = {}
opportunities = []


@app.route('/')
def home():
    return "Backend running"


@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True) or {}

    user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password")
    }

    for u in users:
        if u["email"] == user["email"]:
            return jsonify({"success": False, "message": "Email already exists"})

    users.append(user)
    return jsonify({"success": True})


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json(force=True) or {}

    email = data.get("email")
    password = data.get("password")

    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({"success": True})

    return jsonify({"success": False, "message": "Invalid credentials"})




@app.route('/api/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json(force=True) or {}
    email = data.get("email")

    message = "If this email exists, a reset link has been sent."

    if any(u["email"] == email for u in users):
        token = str(uuid.uuid4())
        expiry = datetime.now() + timedelta(hours=1)

        reset_tokens[token] = {"email": email, "expiry": expiry}

        print(f"RESET LINK: http://127.0.0.1:5500/reset.html?token={token}")

    return jsonify({"success": True, "message": message})


@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json(force=True) or {}

    token = data.get("token")
    new_password = data.get("password")

    if token not in reset_tokens:
        return jsonify({"success": False, "message": "Invalid or expired link"})

    token_data = reset_tokens[token]

    if datetime.now() > token_data["expiry"]:
        del reset_tokens[token]
        return jsonify({"success": False, "message": "Link expired"})

    email = token_data["email"]

    for user in users:
        if user["email"] == email:
            user["password"] = new_password

    del reset_tokens[token]

    return jsonify({"success": True, "message": "Password reset successful"})




@app.route('/api/opportunities', methods=['POST'])
def create_opportunity():
    data = request.get_json(force=True) or {}

    required = ["name", "duration", "start_date", "description", "skills", "category", "future_opportunities", "admin_email"]

    for field in required:
        if not data.get(field):
            return jsonify({"success": False, "message": f"{field} is required"})

    opportunity = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "duration": data.get("duration"),
        "start_date": data.get("start_date"),
        "description": data.get("description"),
        "skills": data.get("skills"),
        "category": data.get("category"),
        "future_opportunities": data.get("future_opportunities"),
        "max_applicants": data.get("max_applicants"),
        "admin_email": data.get("admin_email")
    }

    opportunities.append(opportunity)

    return jsonify({"success": True, "data": opportunity})



@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    email = request.args.get("email")

    data = [op for op in opportunities if op["admin_email"] == email]

    return jsonify({"success": True, "data": data})



@app.route('/api/opportunities/<op_id>', methods=['GET'])
def get_one(op_id):
    email = request.args.get("email")

    for op in opportunities:
        if op["id"] == op_id and op["admin_email"] == email:
            return jsonify({"success": True, "data": op})

    return jsonify({"success": False, "message": "Not found"})


@app.route('/api/opportunities/<op_id>', methods=['PUT'])
def update_opportunity(op_id):
    data = request.get_json(force=True) or {}
    email = data.get("admin_email")

    for op in opportunities:
        if op["id"] == op_id and op["admin_email"] == email:

            op.update({
                "name": data.get("name"),
                "duration": data.get("duration"),
                "start_date": data.get("start_date"),
                "description": data.get("description"),
                "skills": data.get("skills"),
                "category": data.get("category"),
                "future_opportunities": data.get("future_opportunities"),
                "max_applicants": data.get("max_applicants")
            })

            return jsonify({"success": True, "data": op})

    return jsonify({"success": False, "message": "Update failed"})


@app.route('/api/opportunities/<op_id>', methods=['DELETE'])
def delete_opportunity(op_id):
    email = request.args.get("email")

    for i, op in enumerate(opportunities):
        if op["id"] == op_id and op["admin_email"] == email:
            del opportunities[i]
            return jsonify({"success": True})

    return jsonify({"success": False, "message": "Delete failed"})



if __name__ == '__main__':
    print("Server starting...")
    app.run(port=5000, debug=True)