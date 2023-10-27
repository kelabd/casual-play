# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 02:07:14 2023

@author: karam
"""

import pandas as pd

data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}

weather = pd.DataFrame(data)

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')

pivotTable(weather)