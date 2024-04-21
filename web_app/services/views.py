from datetime import datetime


from flask import render_template, request

from web_app.db.funcs import get_all_meets, get_full_name_by_user_id, create_profile, get_user_by_tg_id


def anceta():
    if request.method == "GET":
        return render_template("anceta.html")

    elif request.method == "POST":
        form_tg_id = int(request.form['form_tg_id'])
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        job_title = request.form['job_title']
        try:
            born_date = datetime.strptime(request.form['born_date'], "%d.%m.%Y")
        except ValueError as error:
            print(error)
            return "ERROR"

        print("form_tg_id:", [form_tg_id])
        user = get_user_by_tg_id(tg_id=form_tg_id)

        create_profile(
            user_id=user.id,
            last_name=last_name,
            first_name=first_name,
            job_title=job_title,
            born_date=born_date,
        )

        return render_template("anceta.html")


def statistics():
    meets = get_all_meets()

    for i in range(len(meets)):
        meets[i] = (
            meets[i],
            get_full_name_by_user_id(meets[i].first_user_id),
            get_full_name_by_user_id(meets[i].second_user_id),
            meets[i].meet_date.strftime("%d.%m.%Y")
        )

    return render_template("view_stats.html", meets=meets)
