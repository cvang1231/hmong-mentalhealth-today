"""Script to see database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb hmongformentalhealth')
os.system('createdb hmongformentalhealth')

