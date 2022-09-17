from redis_om import (Field, HashModel)

class Adoptable(HashModel):
    name: str = Field(index=True)
    species: str = Field(index=True)
    age: int = Field(index=True)
    weight: float = Field(index=True)
    sex: str = Field(index=True)
    fee: float = Field(index=True)
    children: str = Field(index=True)
    other_animals: str = Field(index=True)
    description: str = Field(index=True, full_text_search=True)

    # Extra configuration to specify how to generate key
    # names when saving an instance of the model in Redis.
    class Meta:
        global_key_prefix="demo"
        model_key_prefix="adoptable"
