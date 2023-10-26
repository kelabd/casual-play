# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:18:10 2023

@author: karam
"""

import pandas as pd

def createDataFrameFromList(student_data: List[List[int]]) -> pd.DataFrame:

    column_names = ['student_id', 'age']
    
    student_data_df = pd.DataFrame(student_data, columns = column_names)
    
    return student_data_df

    
    # There is room for improving this code by making it more robust to invalid entries
    
    
student_data = [
    [0, 1],
    [1, 5],
    [2, 5],
    [3, 8],
    [4, 10]]
    
result = createDataFrameFromList(student_data)
result.head()