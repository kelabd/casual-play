# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 01:58:55 2023

@author: karam
"""

import pandas as pd

# sample data borrowed from previous problem with players and not employees
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

players = pd.DataFrame(data)

# The following command words but was commented out in favor of a more elegant solution
# df.loc[df['player_id']==846, ['name', 'age']]


def selectData(players: pd.DataFrame) -> pd.DataFrame:

    return players[players.player_id == 846][['name', 'age']]

selectData(players)
