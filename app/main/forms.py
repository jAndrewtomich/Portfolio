from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class CreateTopicForm(FlaskForm):
    title = StringField("Topic Title", validators=[DataRequired()])
    content = CKEditorField("Topic Content", validators=[DataRequired()])
    submit = SubmitField("Submit Topic")