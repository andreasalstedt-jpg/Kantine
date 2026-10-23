from flask import Flask, render_template
from data import varer, meny

app = Flask(__name__)

@app.route('/')
def hjem():
    return render_template("index.html")

@app.route('/meny')
def vis_meny():
    return render_template("meny.html", liste = meny)

@app.route('/varer')
def vis_varer():
    return render_template("varer.html", liste = varer)

@app.route('/kontaktinfo')
def kontakt():
    return render_template("kontakt.html")


if __name__ == "__main__":
    app.run()

