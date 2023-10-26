# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:21:24 2023

@author: karam elabd
"""    

import pandas as pd
from typing import List

data = [
    {"player_id": 846, "name": "Mason", "age": 21, "position": "Forward", "team": "RealMadrid"},
    {"player_id": 749, "name": "Riley", "age": 30, "position": "Winger", "team": "Barcelona"},
    {"player_id": 155, "name": "Bob", "age": 28, "position": "Striker", "team": "ManchesterUnited"},
    {"player_id": 583, "name": "Isabella", "age": 32, "position": "Goalkeeper", "team": "Liverpool"},
    {"player_id": 388, "name": "Zachary", "age": 24, "position": "Midfielder", "team": "BayernMunich"},
    {"player_id": 883, "name": "Ava", "age": 23, "position": "Defender", "team": "Chelsea"},
    {"player_id": 355, "name": "Violet", "age": 18, "position": "Striker", "team": "Juventus"},
    {"player_id": 247, "name": "Thomas", "age": 27, "position": "Striker", "team": "ParisSaint-Germain"},
    {"player_id": 761, "name": "Jack", "age": 33, "position": "Midfielder", "team": "ManchesterCity"},
    {"player_id": 642, "name": "Charlie", "age": 36, "position": "Center-back", "team": "Arsenal"},
]

df = pd.DataFrame(data)
print(df)

def getDataframeSize(players: pd.DataFrame) -> List[int]:

    return list(players.shape)


result = getDataframeSize(df)
print(result)