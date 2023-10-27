# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 02:14:41 2023

@author: karam
"""

import pandas as pd

data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

df = pd.DataFrame(data)


def meltTable(report: pd.DataFrame) -> pd.DataFrame:

    # my solution
    
    # report = report.melt(id_vars = ['product'], value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])

    # report = report.rename(columns = {'value' : 'sales', 'variable' : 'quarter'})
    
    # return report
    
    # more elegant solution
    
    return report.melt(id_vars = ['product'], var_name = 'quarter', value_name = 'sales')
    

meltTable(df)
    