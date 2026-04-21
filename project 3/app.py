from flask import Flask, render_template, request
from mbta import find_stop_near, MAPBOX_TOKEN

app = Flask(__name__)


@app.get("/stop"
def stop_form():
    return render_template("stop.html")


@app.post("/stop")
def stop_submit():
    place = request.form.get("place")

    if not place:
        return render_template("stop.html", error="Please enter a location.")

    try:
        lat, lng, stop = find_stop_near(place)

        return render_template(
            "stop.html",
            place=place,
            lat=lat,
            lng=lng,
            stop=stop,
            mapbox_token=MAPBOX_TOKEN
        )

    except ValueError as e:
        return render_template("stop.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)