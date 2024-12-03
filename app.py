# app.py
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    guess = data.get('guess')
    secret = random.randint(1, 10)
    correct = guess == secret
    return jsonify({
        'correct': correct,
        'secret': secret
    })

if __name__ == '__main__':
    app.run(debug=True)
