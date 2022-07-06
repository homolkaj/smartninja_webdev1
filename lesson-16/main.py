# Homework 16.1: Use Jinja in your Homepage web app

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    boogle_title = "One account. All of Boogle."
    boogle_text = "Sign in with your Boogle Account"
    account_text = "Create an account"
    current_year = datetime.datetime.now().year
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')

    return render_template("index.html", boogle_title=boogle_title, boogle_text=boogle_text, account_text=account_text,
                           current_year=current_year, current_date=current_date)


if __name__ == '__main__':
    app.run(port=5001, use_reloader=True)