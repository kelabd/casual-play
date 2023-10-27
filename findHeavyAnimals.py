# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 02:28:42 2023

@author: karam
"""

import pandas as pd

data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}

animals = pd.DataFrame(data)

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    return pd.DataFrame(animals[(animals['weight'] > 100)].sort_values(by = 'weight', ascending = False)['name'])

findHeavyAnimals(animals)