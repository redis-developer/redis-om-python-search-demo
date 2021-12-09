import csv

from adoptable import Adoptable
from redis_om import Migrator

with open('animal_data.csv') as csv_file:
    animal_reader = csv.DictReader(csv_file)

    for animal in animal_reader:
        adoptable = Adoptable(
            name = animal["name"],
            species = animal["species"],
            age = animal["age"],
            weight = animal["weight"],
            sex =  animal["sex"],
            fee =  animal["fee"],
            children =  animal["children"],
            other_animals =  animal["other_animals"],
            description = animal["description"]
        )
        
        print(f"{animal['name']} -> {adoptable.pk}")
        adoptable.save()

# Create a RediSearch index
Migrator().run()
