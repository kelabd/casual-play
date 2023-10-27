# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 01:17:15 2023

@author: karam
"""

import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}

students = pd.DataFrame(data)

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    
    renamer = {
        'id':'student_id', 
        'first':'first_name',
               'last':'last_name',
               'age':'age_in_years'
               }
    
    students = students.rename(columns = renamer)
    return students

print(students)
renameColumns(students)