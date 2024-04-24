import pandas as pd
import numpy as np
import cv2

import os

# 0 ~ 12 spade, 13 ~ 25 diamond, 26 ~ 38 heart, 49 ~ 51 clubs

def enter_user(names: list, members: int) -> None:
    users = []
    for name in names:
        try:
            df = pd.read_csv(f'./user/{name}.csv',encoding='utf-8-sig')
            users.append(df)
        except:
            print('NO DATA')
            df = pd.DataFrame()
            users.append(df)
