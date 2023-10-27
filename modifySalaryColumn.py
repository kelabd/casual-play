# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 01:02:42 2023

@author: karam
"""

import pandas as pd

data = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}

employees = pd.DataFrame(data)
#print(employees)

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    #employees['salary'] *= 2
    return employees

modifySalaryColumn(employees)