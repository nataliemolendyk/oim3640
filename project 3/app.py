from distro import name
from flask import Flask, render_template
from mbta import find_stop_near

app = Flask(__name__)

@app.route('/station/<place_name>')
def station(place_name):
    stop_name, accessible = find_stop_near(place_name)

    return render_template(
        "station.html",
        place=place_name,
        stop=stop_name,
        accessible=accessible
    )

@app.route('/')
def home():
    return """
    <h1>MBTA Finder</h1>
    <p>Try visiting:</p>
    <p>/station/Boston%20Common</p>
    """

if __name__ == '__main__':
    app.run(debug=True)