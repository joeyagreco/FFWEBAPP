from flask import redirect, url_for, request, render_template

from app import app
from controllers.MainController import MainController
from packages.Exceptions.LeagueNotFoundError import LeagueNotFoundError


@app.route('/favicon.ico')
def favicon():
    """
    This is for the browser icon.
    """
    return redirect(url_for('static', filename='icons/football_icon.ico'))


@app.route("/")
def index():
    errorMessage = request.args.get("error_message")
    return render_template("indexHomepage.html", error_message=errorMessage)


@app.route("/about/<int:leagueId>", methods=["GET"])
def about(leagueId):
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except LeagueNotFoundError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("aboutPage.html", league=league)


@app.route("/feedback/<int:leagueId>", methods=["GET"])
def feedback(leagueId):
    errorMessage = request.args.get("error_message")
    mainController = MainController()
    try:
        league = mainController.getLeague(leagueId)
    except LeagueNotFoundError as e:
        return render_template("indexHomepage.html", error_message=str(e))
    return render_template("feedbackPage.html", league=league, error_message=errorMessage)
