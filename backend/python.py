from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return open("index.html").read()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    print("Received login:")
    print("Name:", username)
    print("Password:", password)

    return "Access granted"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
