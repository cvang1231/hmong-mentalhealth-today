"""Script to see database."""

import os
import csv
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
with open('data/hmongtherapists.csv') as csvFile:
  fieldnames = ['name', 'clinic', 'website', 'email', 'specialty','img']
  therapist_data = csv.DictReader(csvFile, fieldnames=fieldnames, skipinitialspace=True)
    


# Loop through each dictionary in therapist_data
  for therapist in therapist_data:
    name, clinic, website, email, specialty, img = (
                                                  therapist['name'],
                                                  therapist['clinic'],
                                                  therapist['website'],
                                                  therapist['email'],
                                                  therapist['specialty'],
                                                  therapist['img'])
                                                  
    #Supply arguments to crud.py
    db_therapist = crud.add_therapist(
                                      name, 
                                      clinic,
                                      website, 
                                      email, 
                                      specialty, 
                                      img)
    #Add each new therapist to db_therapist list
    therapist_in_db.append(db_therapist) 






