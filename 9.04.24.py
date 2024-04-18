# 1
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    response = make_response("Cookie is set!")
    response.set_cookie("user_visit", "yes")
    return response


@app.route("/get_cookie")
def get_cookie():
    user_visit = request.cookies.get("user_visit")
    return f"User visited: {user_visit}"


if name == "__main__":
    app.run(debug=True)


# 2
@app.route("/set_cookie")
def set_cookie():
    response = make_response("Cookie is set!")
    response.set_cookie("user_visit", "yes")
    return response


# 3
@app.route("/language", methods=["GET", "POST"])
def language():
    if request.method == "POST":
        selected_language = request.form["language"]
        response = make_response("Language selected!")
        response.set_cookie("language", selected_language)
        return response
    return """
        <form method="post">
            <select name="language">
                <option value="english">English</option>
                <option value="russian">Russian</option>
            </select>
            <input type="submit" value="Select Language">
        </form>
    """


# 4
from flask import redirect, url_for


@app.route("/redirect_example")
def redirect_example():
    return """
        <form action="/redirect_target">
            <input type="submit" value="Redirect">
        </form>
    """


@app.route("/redirect_target")
def redirect_target():
    return "Redirected!"
