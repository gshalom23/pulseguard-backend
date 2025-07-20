from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'API is running!'

@app.route('/api/rithmic/account', methods=['POST'])
def get_account():
    return jsonify({
        "account_id": "SIM123456",
        "balance": 54000.65,
        "equity": 50530.10,
        "liquidation_point": 2500,
        "realized_pnl": 1270.30,
        "unrealized_pnl": -35.80
    })

@app.route('/api/rithmic/trades', methods=['POST'])
def get_trades():
    return jsonify([
        {"symbol": "NQ", "side": "LONG", "qty": 1, "pnl": 75.5, "timestamp": "2024-07-20T09:15:00Z"},
        {"symbol": "GC", "side": "SHORT", "qty": 1, "pnl": -40.2, "timestamp": "2024-07-19T13:27:00Z"},
        {"symbol": "YM", "side": "LONG", "qty": 2, "pnl": 150, "timestamp": "2024-07-18T11:02:00Z"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
