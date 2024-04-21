from web_app.services import views

from web_app.settings.constants import app


app.add_url_rule("/anceta", methods=["GET", "POST"], view_func=views.anceta)
app.add_url_rule("/statistics", methods=["GET"], view_func=views.statistics)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
