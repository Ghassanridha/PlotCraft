import os
from flask import Flask, send_file, request, jsonify
from config import init_firebase

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

db = init_firebase()


@app.route('/')
def home():
    return send_file(os.path.join(base_dir, 'home.html'))


@app.route('/save', methods=['POST'])
def save():
    if db is None:
        return jsonify({"error": "Firebase غير متصل"}), 500
    data = request.get_json(silent=True) or {}
    db.collection('users').add(data)
    return jsonify({"status": "saved"})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
