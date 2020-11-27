# ----- dataclass -----
from dataclasses import dataclass


@dataclass
class DataClassCard:
    name:str
    age:int


queen_of_hearts = DataClassCard("Lisa", 25)
print("\ndataclasses :")
print(queen_of_hearts.name)
print(queen_of_hearts)
print(queen_of_hearts == DataClassCard("Lisa", 25))