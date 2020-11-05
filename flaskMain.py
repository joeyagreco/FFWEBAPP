from flask import Flask, render_template, request, redirect, url_for
from controllers.MainController import MainController

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("indexHomepage.html")


@app.route("/testHomepage", methods=["GET"])
def testHomepage():
    return render_template("testHomepage.html", subtitle="Test Home Page")


@app.route("/addleague")
def addLeague():
    mainController = MainController()
    newLeague = mainController.addLeague()
    if newLeague:
        return redirect(url_for("leagueHomepage", league_id=int(newLeague.inserted_id)))
    else:
        return render_template("indexHomepage.html", errorMessage="ERROR: Could not add league.")


@app.route("/leaguehomepage", methods=["GET"])
def leagueHomepage():
    league_id = request.args.get("league_id")
    mainController = MainController()
    league = mainController.getLeague(int(league_id))
    if league:
        return league
    else:
        return render_template("indexHomepage.html",
                               errorMessage=f"ERROR: Cannot find a league with the ID {league_id}.")


if __name__ == "__main__":
    app.run(debug=True)
