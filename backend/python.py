from flask import Flask, request, render_template
import sys

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    print(request.form, file=sys.stderr)
    print("Received login:", file=sys.stderr)

    username = request.form.get("username")
    password = request.form.get("password")

    print("Name:", username, file=sys.stderr)
    print("Password:", password, file=sys.stderr)
    
    if username == "fred" and password == "password":
        return "Access granted"
    return 'Try "fred" and "password".'
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
