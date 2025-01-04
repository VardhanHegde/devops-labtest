# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/wise-cobra-50')
def wise_cobra():
    return jsonify(message="Everything is OK")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5093)
