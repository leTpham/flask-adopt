"""Flask app for adopt app."""

from flask import Flask, redirect, request, flash, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)



"""
get request for route "/"
list pets:
query from database all the instances of the Pet class
Pet.query.all()???

name - NOTE: each name links to route of that /pet-id-number
photo(if avail)
display "Available" if available

return render_template of pets page html

"""

@app.get('/')
def root():
    """Homepage redirects to list of users."""

    pets = Pet.query.all()
    return render_template('pet_list.html', pets = pets)

"""




handler for add pet form
route /add (both POST and GET method)
        validate: (form validate on submit)
-grab data from form -> create new Pet instance for database
-> db add -> db commit -> THEN REDIRECT TO HOME

        else:
            RE-render the form

"""
@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data


        new_pet = Pet(name = name, species = species,
                        photo_url = photo_url,
                            age = age, notes = notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} the {species}!")
        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)









""" for route /[pet-id-number]
    query from database and then render to pet_detail.html

    form on page allows edit pet
"""


""" POST/GET request for route /[pet-id-number]
        def edit_pet..
        VALIDATE: edit pet
        connect to database -> db.commit after
        redirect to refresh?

        ELSE: Re_render the form
"""

