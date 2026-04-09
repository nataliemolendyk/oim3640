from distro import name
from flask import Flask, render_template
from stocks import get_price

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name):
#   return f'Hello, {name}!'

    return render_template('hello.html', name=name)

@app.route('/square/<int:n>')
def square(n):
    return f'{n} squared is {n**2}'

@app.route('/stock/<ticker>')
def stock(ticker):
    price = get_price(ticker)
    return f'The current price of {ticker.upper()} is ${price: 2f}.'


if __name__ == '__main__':
    app.run(debug=True)

