import json
import csv

csvFilePath = 'hmongtherapists.csv'
jsonFilePath = 'hmongtherapists.json'

# Read the CSV and add data to dictionary
data = {}
with open(csvFilePath) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Write data to a JSON file
with open(jsonFilePath, 'w') as f:
    json.dump(rows, f, indent = 4)