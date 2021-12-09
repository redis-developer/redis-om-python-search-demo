from redis_om import HashModel

class Adoptable(HashModel):
    name: str
    species: str
    age: int
    weight: float
    sex: str
    fee: float
    children: str
    other_animals: str
    location: str
    description: str
