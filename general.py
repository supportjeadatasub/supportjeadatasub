from flask import Blueprint, request, jsonify

general_bp = Blueprint('general', __name__)

@general_bp.route('/contact', methods=['POST'])
def contact():
    data = request.json
    print(f"Contact from {data['name']} ({data['email']}): {data['message']}")
    return jsonify({"message": "Message received"}), 200
