from flask import Flask, render_template, request

app = Flask(__name__)


def millisecondsapp(milli):
    hours = divmod(milli,3600000)
    h = hours[0]
    mins = divmod(hours[1],60000)
    m = mins[0]
    seconds = divmod(mins[1],1000)
    s = seconds[0]
    return h, m, s
    
@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        if request.form["number"].isdigit() == True:
            milliseconds = int(request.form["number"]) 
            h, m, s = millisecondsapp(milliseconds)
            return render_template("result.html", h = f"{h} hours"* (h !=0), m = f"{m} minutes" * (m !=0), \
            s = f"{s} seconds"* (s !=0), ms = f"just {milliseconds} milliseconds" * (milliseconds < 1000), \
                milliseconds = milliseconds, developer_name = "Elnur")
        else:
            return render_template("index.html", not_valid = True, developer_name = "Elnur")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host = "0.0.0.0", port = 80)