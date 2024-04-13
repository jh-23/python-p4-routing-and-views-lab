#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    output = f''
    for i in range(parameter):
        output += f'{i}\n'
    return output
    
@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if operation == '+':
        result = num1 + num2
        return str(result)
    elif operation == '-':
        result = num1 - num2
        return str(result)
    elif operation == '*':
        result = num1 * num2
        return str(result)
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
            return str(result)
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2 
            return str(result)
    else: 
        return None

if __name__ == '__main__':
    app.run(port=5555, debug=True)
