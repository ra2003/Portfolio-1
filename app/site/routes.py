from flask import render_template
from . import site
from resume import Resume

resume = Resume()


@site.route("/", methods=["GET"])
def index():
    return render_template("index.html", resume=resume)
