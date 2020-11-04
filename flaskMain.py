from flask import Flask, render_template, request
from clients.DatabaseClient import DatabaseClient
from packages.Calculator import Calculator
from packages.TestDatabase.TestDatabase import TestDatabase

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("indexHomepage.html")


@app.route("/testHomePage")
def testHomePage():
    return render_template("testHomePage.html", subtitle="Test Home Page")


@app.route("/test", methods=["GET", "POST"])
def test():
    subtitle = "Test"
    try:
        c = Calculator.Calculator()
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        sum = c.add(num1, num2)
        # TEST DATABASE
        id = 1
        dbClient = DatabaseClient(id)
        dbClient.setLeague(id, {"_id": id, "num1": num1, "num2": num2})
        # END TEST
        return render_template("test.html", subtitle=subtitle, sum=sum)
    except:
        return render_template("test.html", subtitle=subtitle, sum="N/A")


@app.route("/test/getleague/<leagueId>")
def test_getLeague(leagueId):
    dbClient = DatabaseClient(int(leagueId))
    return dbClient.getLeague()


if __name__ == "__main__":
    app.run(debug=True)
