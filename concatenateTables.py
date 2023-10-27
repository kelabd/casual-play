# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 01:56:14 2023

@author: karam
"""

import pandas as pd

data = {
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
}

df1 = pd.DataFrame(data)

data = {
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
}

df2 = pd.DataFrame(data)

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    result = pd.concat([df1, df2], ignore_index=True)
    return result

concatenateTables(df1, df2)