"""Script to see database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb hmongmentalhealthtoday')
os.system('createdb hmongmentalhealthtoday')

model.connect_to_db(server.app)
model.db.create_all()

# Load data from data/hmongtherapists.json and save it to variable
with open('data/hmongtherapists.json') as f:
    therapist_data = json.loads(f.read())

# Create therapists, store them in list
therapist_in_db = []

# Loop through each dictionary in therapist_data
for therapist in therapist_data:

    name, clinic, website, email, specialty, lat, long, img = (
      therapist['name'],
      therapist['clinic'],
      therapist['website'],
      therapist['email'],
      therapist['specialty'],
      therapist['lat'],
      therapist['long'],
      therapist['img']  
    )
    # Supply arguments to crud.py
    db_therapist = crud.add_therapist(name, 
                                    email,
                                    clinic, 
                                    website, 
                                    lat, 
                                    long, 
                                    specialty, 
                                    img)
    # Add each new therapist to db_therapist list
    therapist_in_db.append(db_therapist)






