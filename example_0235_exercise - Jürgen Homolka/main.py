# modify the solution to the last exercise, such that
# the about() function handles both the GET and POST requests
# don't forget to change "action" in the about.html page

from flask import Flask, render_template, request

app = Flask(__name__)
''' will be handlet in about() funktion
@app.route("/contact", methods=["POST"])
def contact():
    contact_email = request.form.get("contact-email")
    contact_password = request.form.get("contact-password")

    print(contact_email)
    print(contact_password)

    return render_template("success.html")
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")
    elif request.method == "POST":
        contact_name = request.form.get("contact-email")
        contact_email = request.form.get("contact-password")

        print(contact_name)
        print(contact_email)

    return render_template("success.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(use_reloader=True)