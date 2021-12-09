import csv

from adoptable import Adoptable
from redis_om import Migrator

with open('animal_data.csv') as csv_file:
    animal_reader = csv.DictReader(csv_file)

    for animal in animal_reader:
        adoptable = Adoptable(**animal)
        
        print(f"{animal['name']} -> {adoptable.pk}")
        adoptable.save()

# Create a RediSearch index
Migrator().run()
