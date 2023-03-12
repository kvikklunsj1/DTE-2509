from flask import Blueprint, render_template, request

views = Blueprint(__name__, "/")

@views.route("/")
def index():
    name = request.args.get("name", "onanym Ape")
    return render_template("index.html", placeholder=name)
