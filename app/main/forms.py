from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required 

class ReviewForm(FlaskForm):
    title = StringField('Comment')
    comment = TextAreaField('Enter your comment')
    submit = SubmitField('submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Production','Production'),('Movie','Movie'),('Job','Job'),('Promotion','Promotion'),('Sales','Sales'),('Advertisement','Advertisement')],validators=[Required()])
    submit = SubmitField('Type / Copy and Paste Your Pitch Here')

# class CommentForm(FlaskForm):
#     title = StringField('Comment')
#     comment = TextAreaField('Enter your comment')
#     submit = SubmitField('submit')