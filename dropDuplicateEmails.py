# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:48:01 2023

@author: karam
"""

import pandas as pd

data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

df = pd.DataFrame(data)
print(df)

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset = ['email'])
    return customers

dropDuplicateEmails(df)