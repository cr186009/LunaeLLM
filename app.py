from flask import Flask, request, render_template
from gpt_service import ask_gpt
from forms import PromptForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '069ce78e5344f901c7314305ffbab6f1f525d6ec105f8bcdb08dc20371f66206'  # Example: 'mydevsecret123'

@app.route("/", methods=["GET", "POST"])
def home():
    form = PromptForm()
    answer = None
    if form.validate_on_submit():
        prompt = form.prompt.data
        answer = ask_gpt(prompt)
    return render_template("index.html", form=form, answer=answer)

