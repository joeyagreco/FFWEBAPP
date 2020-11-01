from flask import Flask, render_template, request

from packages.Calculator import Calculator
from packages.TestDatabase.TestDatabase import TestDatabase

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", subtitle="Home")


@app.route("/test", methods=["GET", "POST"])
def test():
    subtitle = "Test"
    try:
        c = Calculator.Calculator()
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        sum = c.add(num1, num2)
        # TEST DATABASE
        testDatabase = TestDatabase()
        testDatabase.post(50, {"_id": 6, "num1": num1, "num2": num2})
        # END TEST
        return render_template("test.html", subtitle=subtitle, sum=sum)
    except:
        return render_template("test.html", subtitle=subtitle, sum="N/A")


if __name__ == "__main__":
    app.run(debug=True)
