from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user = data['choice']

    choices = ['stone', 'paper', 'scissor']
    cpu = random.choice(choices)

    if user == cpu:
        result = "draw"
    elif (user == 'stone' and cpu == 'scissor') or \
         (user == 'paper' and cpu == 'stone') or \
         (user == 'scissor' and cpu == 'paper'):
        result = "win"
    else:
        result = "lose"

    return jsonify({
        "user": user,
        "cpu": cpu,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
