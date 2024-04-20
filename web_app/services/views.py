from flask import render_template, request


def anceta():
    if request.method == "GET":
        return render_template("anceta.html")

    elif request.method == "POST":
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        job_title = request.form['job_title']
        born_date = request.form['born_date']

        return render_template("anceta.html")
