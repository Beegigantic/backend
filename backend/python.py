from flask import Flask, request, render_template
import sys

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "fred" and password == "password":
        return "Access granted"

    return render_template("index.html", error='Try "fred" and "password".')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
