from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 DevOps Backend is Running!"

@app.route('/users')
def users():
    return jsonify([
        {"id": 1, "name": "Aman"},
        {"id": 2, "name": "Raj"}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)