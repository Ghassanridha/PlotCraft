import os
from flask import Flask, render_template, request, jsonify
from config import init_firebase

app = Flask(__name__)

db = init_firebase()

@app.route('/')
def home():
    # render_template يبحث تلقائياً داخل مجلد templates
    return render_template('home.html')

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
