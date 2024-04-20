from flask import render_template, request

from db.funcs import get_all_meets, get_full_name_by_user_id


def anceta():
    if request.method == "GET":
        return render_template("anceta.html")

    elif request.method == "POST":
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        job_title = request.form['job_title']
        born_date = request.form['born_date']

        return render_template("anceta.html")


def statistics():
    meets = get_all_meets()

    for i in range(len(meets)):
        meets[i][1] = f"№{meets[i][1]}: {get_full_name_by_user_id(meets[i][1])}"

    return render_template("statistics.html", meets=meets)
