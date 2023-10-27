# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 01:35:26 2023

@author: karam
"""

import pandas as pd

data = {
    'student_id': [1, 2],
    'name': ['Ava', 'Kate'],
    'age': [6, 15],
    'grade': [73.0, 87.0]
}

students = pd.DataFrame(data)

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:

    students['grade'] = students['grade'].astype(int)
    return students

changeDatatype(students)