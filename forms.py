"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, InputRequired, Optional, Email

"""
class for Add pet form
pet name: stringf
species: string
photo_url: string
age: selectfield
notes: textareafield

will be connected to /add both get and post
"""

class AddPetForm(FlaskForm):
    """Form for pets."""

    name = StringField("Pet Name",
                        validators=[InputRequired()] )
    species = StringField("Species")
