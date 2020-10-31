from flask import Flask, render_template, request

from packages.Calculator import Calculator

app = Flask(__name__)
# test private

@app.route("/")
def index():
    return render_template("index.html", subtitle="Home")


@app.route("/test", methods=["GET", "POST"])
def test():
    try:
        c = Calculator.Calculator()
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        sum = c.add(num1, num2)
        return render_template("test.html", subtitle="Test", sum=sum)
    except:
        return render_template("test.html", subtitle="Test", sum="N/A")


if __name__ == "__main__":
    app.run(debug=True)
