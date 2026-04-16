from flask import Flask, render_template, request
from mbta import find_stop_near

app = Flask(__name__)

@app.get("/stop")
def stop_form():
    return render_template("stop.html")


@app.post("/stop")
def stop_post():
    place = request.form.get("place")

    if not place:
        return "Please enter a location."

    try:
        stop_name, accessible = find_stop_near(place)
        accessible_text = "Yes" if accessible else "No"

        return f"""
        <h2>Result</h2>
        <p>The nearest stop to <strong>{place.title()}</strong> is <strong>{stop_name}</strong>.</p>
        <p>Wheelchair accessible: <strong>{accessible_text}</strong></p>
        <a href="/stop">Search again</a>
        """

    except Exception:
        return f"This location '{place.title()}' is not valid. Please try again."


@app.route('/stop/<place>')
def stop(place):
    try:
        stop_name, accessible = find_stop_near(place)
        accessible_text = "Yes" if accessible else "No"

        return f"The nearest stop to {place.title()} is {stop_name}. Wheelchair accessible: {accessible_text}."

    except Exception:
        return f"Could not find a stop near '{place.title()}'."


if __name__ == '__main__':
    app.run(debug=True)