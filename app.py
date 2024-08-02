from flask import Flask, render_template, request
import pyshorteners
from pyshorteners.exceptions import BadURLException

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        link_recieved = request.form["input_link"]
        print(link_recieved)
       
        link_short = pyshorteners.Shortener().tinyurl.short(link_recieved)
        return render_template("index.html", link_out=link_short, link_in=link_recieved)


        
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run() 