"""Script to see database."""

import os
import json
import crud
import model
import server

os.system('dropdb hmongmentalhealthtoday')
os.system('createdb hmongmentalhealthtoday')

model.connect_to_db(server.app)
model.db.create_all()

therapist_in_db = []

# Load data from data/hmongtherapists.csv
# Have DictReader turn hmongtherapists.csv into readable dictionary
# Save readable dictionary to therapist_data
#with open('data/therapists.csv', encoding='utf-8-sig') as csvFile:
 # fieldnames = ['name', 'clinic', 'website', 'email', 'specialty', 'lat', 'long', 'img']
  #therapist_data = csv.DictReader(csvFile, fieldnames=fieldnames, skipinitialspace=True)

with open('data/therapists.json') as f:
  therapist_data = json.loads(f.read())


# Loop through each dictionary in therapist_data
  for therapist in therapist_data:
    name, clinic, website, email, specialty, lat, long, img, county = (
                                                  therapist['name'],
                                                  therapist['clinic'],
                                                  therapist['website'],
                                                  therapist['email'],
                                                  therapist['specialty'],
                                                  therapist['lat'],
                                                  therapist['long'],
                                                  therapist['img'],
                                                  therapist['county'])
                                                  
    #Supply arguments to crud.py
    db_therapist = crud.create_therapist(
                                      name, 
                                      clinic,
                                      website, 
                                      email, 
                                      specialty, 
                                      lat,
                                      long,
                                      img,
                                      county)
    #Add each new therapist to db_therapist list
    therapist_in_db.append(db_therapist) 




