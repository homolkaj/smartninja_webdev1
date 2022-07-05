from flask import Flask, render_template

app = Flask(__name__)

# Using jinja and what we have learned so far, create three websites: "home", "about me" and "contact"
# also create a base.html from which all of these website inherit their general format
# Each website should have the same main heading <h1></h1>, same CSS file, but a different title <title></title>
# and a different text <p></p>

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-me")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def portfolio_fakebook():
    return render_template("Fakebook-Maxi_02.html")

@app.route("/portfolio/boogle")
def portfolio_boogle():
    return render_template("Boogle_Login.html")

@app.route("/portfolio/hair-salon")
def portfolio_hairsalon():
    return render_template("Hair-Salon.html")

if __name__ == '__main__':
    app.run(port=5005, use_reloader=True)