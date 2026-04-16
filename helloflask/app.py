from flask import Flask, render_template, request
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
    return f'The current price of {ticker.upper()} is ${price:.2f}.'

@app.get("/ticker")
def ticker():
    return render_template("ticker.html")

@app.post("/ticker")
def ticker_post():
    ticker = request.form.get("symbol")
    try:
        price = get_price(ticker)
        return f"The current price of {ticker.upper()} is ${price:.2f}."
    except Exception as e:
        return f"This ticker symbol {ticker.upper()} is not valid. Please try again."

if __name__ == '__main__':
    app.run(debug=True)

