from flask import Flask, render_template
from app import app
from flask import redirect, render_template, request, session
import user
import parking_lot


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username,password):
            return redirect("/home")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/new_user")
def new_user():
    return render_template("create.html")

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.create(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Tilin luonti ei onnistunut")

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/")

@app.route("/add_parkinglot")
def add_parkinglot():
    return render_template("new_park.html")

@app.route("/new_park", methods=["POST"])
def new_park():
    description = request.form["description"]
    price = request.form["price"]
    city = request.form["city"]
    address = request.form["address"]
    if parking_lot.add_new(description, price, city, address):
        return redirect("/home")
    else:
        return render_template("error.html", message="Parkkipaikan lisäys ei onnistunut")

@app.route("/home")
def home():
    return render_template("home.html", lots = parking_lot.get_all())

@app.route("/delete_parking_lot/<int:id>")
def delete_parking_lot(id):
    if parking_lot.delete(id):
        return redirect("/home")
    else:
        return render_template("error.html", message="Jokin meni vikaan")

@app.route("/control")
def control():
    return render_template("my_parking_lots.html", lots = user.get_own_parking_lots())

@app.route("/book/<int:id>")
def book(id):
    if parking_lot.book(id):
        return render_template("home.html", lots = parking_lot.get_all())
    else:
        return render_template("error.html", message = "Jokin meni vikaan")

@app.route("/stop_using/<int:id>")
def stop_using(id):
    parking_lot.stop_using(id)
    return redirect("/home")

@app.route("/city_results")
def city_result():
    city = request.args["city"]
    return render_template("home.html", lots = parking_lot.city_results(city))

@app.route("/comment/<int:id>")
def comment(id):
    return render_template("new_comment.html", parkking_lot_id = id)

@app.route("/new_comment/<int:id>", methods=["POST"])
def new_comment(id):
    comment = request.form["comment"]
    if parking_lot.give_comment(id, comment):
        return redirect("/home")
    else:
        return render_template("error.html", message = "Kommentin antaminen ei onnistunut")

@app.route("/read_comments/<int:id>")
def read_comments(id):
    comments = parking_lot.get_comment(id)
    lot = parking_lot.get_lot(id)
    return render_template("comments.html",lot = lot, comments = comments, id = id)

# @app.route("/new_stars/<int:id>")
# def new_stars(id):
#     return render_template("give_stars.html", id = id)

# @app.route("/give_stars/<int:id>", methods=["POST"])
# def give_stars(id):
#     stars = request.form["stars"]
#     parking_lot.give_stars(id, stars)
#     return redirect("/home")