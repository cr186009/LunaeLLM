# filepath: /workspaces/LunaeLLM/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PromptForm(FlaskForm):
    prompt = StringField('Prompt', validators=[DataRequired()])
    submit = SubmitField('Submit')