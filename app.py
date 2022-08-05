"""Flask app for adopt app."""

from flask import Flask, redirect, request, flash, render_template

# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

# toolbar = DebugToolbarExtension(app)


@app.get('/')
def root():
    """Homepage that shows list of pets."""

    pets = Pet.query.all()
    return render_template('pet_list.html', pets = pets)


@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Add Pet Form"""

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



@app.route("/<int:pid>/", methods=["GET", "POST"])
def edit_user(pid):
    """Show pets profiles and edit form and handle edit."""

    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Pet {pid} updated!")
        return redirect("/")

    else:
        return render_template("pet_detail.html", form=form, pet = pet)