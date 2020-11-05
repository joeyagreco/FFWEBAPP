from flask import Flask, render_template, request, redirect, url_for
from controllers.MainController import MainController

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("indexHomepage.html")


@app.route("/testHomePage", methods=["GET"])
def testHomepage():
    return render_template("testHomepage.html", subtitle="Test Home Page")


@app.route("/addleague")
def addLeague():
    mainController = MainController()
    newLeague = mainController.addLeague()
    if newLeague:
        return redirect(url_for("leagueHomepage", league_id=int(newLeague.inserted_id)))
    else:
        return "league could not be added"


@app.route("/leaguehomepage", methods=["GET"])
def leagueHomepage():
    league_id = request.args.get("league_id")
    mainController = MainController()
    league = mainController.getLeague(int(league_id))
    if league:
        return league
    else:
        return f"league with id {league_id} not found"


if __name__ == "__main__":
    app.run(debug=True)
