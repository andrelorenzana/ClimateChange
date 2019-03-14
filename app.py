from flask import Flask, jsonify, render_template
from flask import request
import urllib.request

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

app = Flask(__name__)



@app.route("/api/justice-league")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)

@app.route("/api/justice-league")


@app.route('/')
def index():
    ip = request.remote_addr
    return render_template('index.html', user_ip=ip)

if __name__ == "__main__":
    app.run(debug=True)
