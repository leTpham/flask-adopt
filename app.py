"""Flask app for adopt app."""

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

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


"""
handler for add pet form
route /add (both POST and GET method)
        validate: (form validate on submit)
-grab data from form -> create new Pet instance for database
-> db add -> db commit -> THEN REDIRECT TO HOME

        else:
            RE-render the form

"""


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

