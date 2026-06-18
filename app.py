from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data['choice']

    choices = ['stone', 'paper', 'scissor']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "Draw"
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        result = "Win"
    else:
        result = "Lose"

    return jsonify({
        'user': user_choice,
        'computer': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
