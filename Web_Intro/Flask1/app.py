from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static", static_url_path="/")

@app.route("/")
def home():
    return render_template("/home.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/list")
def list():
    my_list = ["Elkedel", "Nissehue", "Ostepops", "Flaske"]
    return render_template("list.html", items=my_list)

@app.route("/querystring")
def querystring():
    name = request.args.get("name")
    return render_template("querystring.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
