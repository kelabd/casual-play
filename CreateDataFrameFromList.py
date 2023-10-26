# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:18:10 2023

@author: karam
"""

import pandas as pd

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

student_data_df = pd.DataFrame(student_data)

student_data_df = student_data_df.rename(columns = {0: "student_id", 1: "age"})