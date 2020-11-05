from flask import Flask, render_template, request, redirect, url_for
from controllers.MainController import MainController

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            league_id = request.form["league_id"]
            return redirect(url_for("leagueHomepage", league_id=league_id))
        else:
            return render_template("indexHomepage.html")
    except Exception as e:
        print("except", e)
        return render_template("indexHomepage.html")


@app.route("/testHomePage", methods=["GET"])
def testHomepage():
    return render_template("testHomepage.html", subtitle="Test Home Page")


@app.route("/addleague", methods=["GET", "POST"])
def addLeague():
    print("in add league")
    mainController = MainController()
    newLeague = mainController.addLeague()
    if newLeague:
        print(newLeague.inserted_id)
        return redirect(url_for("leagueHomepage", league_id=int(newLeague.inserted_id)))
    else:
        return "league could not be added"


@app.route("/leaguehomepage/<league_id>")
def leagueHomepage(league_id):
    mainController = MainController()
    league = mainController.getLeague(int(league_id))
    if league:
        return league
    else:
        return f"league with id {league_id} not found"


if __name__ == "__main__":
    app.run(debug=True)
