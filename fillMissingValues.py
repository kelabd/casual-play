# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 01:47:13 2023

@author: karam
"""

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:

    products['quantity'] = products['quantity'].fillna(0)
    return products
    