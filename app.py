from flask import Flask, request, render_template
from gpt_service import ask_gpt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        answer = ask_gpt(prompt)
    return render_template("index.html", answer=answer)