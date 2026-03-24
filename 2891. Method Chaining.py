import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals.sort_values(['weight'], ascending=False)
    data = animals[animals['weight'] > 100][['name']]
    return data
