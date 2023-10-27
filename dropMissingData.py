# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:08:43 2023

@author: karam
"""

import pandas as pd

data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

students = pd.DataFrame(data)

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    return students.dropna(subset = 'name')

dropMissingData(students)

