import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, send_file, request, jsonify

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# --- اتصال Firebase ---
db = None
try:
    firebase_json = os.environ.get("FIREBASE_CREDENTIALS")
    if firebase_json and not firebase_admin._apps:
        cred = credentials.Certificate(json.loads(firebase_json))
        firebase_admin.initialize_app(cred)
        db = firestore.client()
except Exception as e:
    print("Firebase error:", e)


@app.route('/')
def home():
    return send_file(os.path.join(base_dir, 'index.html'))


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
