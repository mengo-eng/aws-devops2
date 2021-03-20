from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first condition"
    return render_template("index.html", message = first)

@app.route("/mammadov")
def elnur():
    name = ["Samir", "Esed", "Nizami"]
    return render_template("body.html", object = name)
    developer_name = "Elnur"


if __name__ == "__main__":
    app.run(debug=True)