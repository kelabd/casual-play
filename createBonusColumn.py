# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:35:47 2023

@author: karam
"""

import pandas as pd

data = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

employees = pd.DataFrame(data)


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:

    # working solution
    #employees = employees.assign(bonus = lambda x: x.salary*2)
    
    # alternative solution
    employees = employees.assign(bonus = employees.salary*2)
    
    return employees

createBonusColumn(employees)
    