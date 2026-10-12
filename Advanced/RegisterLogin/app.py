from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user = {
    "fn": "",
    "ln": "",
    "un": "",
    "pwd": ""
}


@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["un"]
        password = request.form["pwd"]

        if username != user["un"]:
            message = "Wrong username"

        elif password != user["pwd"]:
            message = "Wrong password"

        else:
            return redirect(url_for("welcome"))

    return render_template("Login.html", message=message)


@app.route("/register", methods=["GET", "POST"])
def register():

    message = ""

    if request.method == "POST":

        first_name = request.form["fn"]
        last_name = request.form["ln"]
        username = request.form["un"]
        password = request.form["pwd"]

        if not first_name or not last_name or not username or not password:
            message = "All fields are required"

        else:
            user["fn"] = first_name
            user["ln"] = last_name
            user["un"] = username
            user["pwd"] = password

            return redirect(url_for("login"))

    return render_template("Register.html", message=message)


@app.route("/welcome")
def welcome():

    return render_template(
        "Welcome.html",
        fn=user["fn"],
        ln=user["ln"]
    )


if __name__ == "__main__":
    app.run(debug=True)
