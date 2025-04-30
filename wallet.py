from flask import Blueprint, jsonify

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = [
        {"date": "2025-04-01", "type": "Fund", "amount": 2500, "status": "Success"},
        {"date": "2025-04-02", "type": "Withdraw", "amount": 1500, "status": "Pending"},
    ]
    return jsonify(transactions)
