from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello World"

@app.route("/elnur")
def message():
    return "Elnur's page"

@app.route("/third/sub")
def third():
    return "This is third subpage"

@app.route("/forth/<string:id>")
def forth(id):
    return f"ID of this page is {id}"

if __name__ =="__main__":
    app.run(debug=True)