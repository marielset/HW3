from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

myVariable = 0

@app.route('/')
def index():
    global myVariable
    myVariable += 1
    if myVariable > 2:
        return render_template('two_plus.html', number=myVariable)
    return render_template('blank_template.html', number=myVariable)

@app.route('/refresh-amount')
def refresh():
    if request.method == 'GET':
        result = request.args
        number = result.get('number')
        if int(number) < 60:
            return render_template('thirty.html', number=number)
        elif int(number) < 500:
            return render_template('sixty.html', number=number)
        elif int(number) < 1000:
            return render_template('seven_hundred.html', number=number)
        else:
            return "Seriously, find a better way to spend your time."


if __name__ == '__main__':
    app.run(debug = True)

