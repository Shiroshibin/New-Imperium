from services import views

from settings.constants import app


app.add_url_rule("/anceta", methods=["GET", "POST"], view_func=views.anceta)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')