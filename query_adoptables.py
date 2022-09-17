from adoptable import Adoptable

def show_results(results):
    for adoptable in results:
        print(adoptable)
        print("")

def find_by_name():
    print("find_by_name:")
    return Adoptable.find(Adoptable.name == "Luna").all()

def find_male_dogs():
    print("find_male_dogs:")
    return Adoptable.find(
        (Adoptable.species == "dog") &
        (Adoptable.sex == "m")
    ).all()

def find_dogs_in_age_range():
    print("find_dogs_in_age_range:")
    return Adoptable.find(
        (Adoptable.species == "dog") & 
        (Adoptable.age > 8) & 
        (Adoptable.age < 11)
    ).sort_by("age")

def find_cats_good_with_children():
    print("find_cats_good_with_children:")
    return Adoptable.find(
        (Adoptable.species == "cat") &
        (Adoptable.children == "y") & 
        (Adoptable.description % "play") &
        ~(Adoptable.description % "anxious") &
        ~(Adoptable.description % "nervous")
    ).all()


show_results(find_by_name())
#show_results(find_male_dogs())
#show_results(find_dogs_in_age_range())
#show_results(find_cats_good_with_children())
