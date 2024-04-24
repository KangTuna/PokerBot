import cv2
import numpy as np

import os

# spades = os.listdir('./images/Cards/spades')
# spades_list = [f'./images/Cards/spades/{i}' for i in spades]

# img = None

# for i in spades_list:
#     if img is None:
#         img = cv2.imread(i)
#     else:
#         temp = cv2.imread(i)
#         img = np.hstack((img,temp))
#         break
        
# path = './images/temp/temp.png'
# cv2.imwrite(path,img)

clubs = os.listdir('./images/Cards/clubs')
diamonds = os.listdir('./images/Cards/diamonds')
hearts = os.listdir('./images/Cards/hearts')
spades = os.listdir('./images/Cards/spades')

clubs_list = [f'./images/Cards/clubs/{i}' for i in clubs]
diamonds_list = [f'./images/Cards/diamonds/{i}' for i in diamonds]
hearts_list = [f'./images/Cards/hearts/{i}' for i in hearts]
spades_list = [f'./images/Cards/spades/{i}' for i in spades]

cardsImg = [spades_list, diamonds_list, hearts_list, clubs_list]

for types in cardsImg:
    for card in types:
        img = cv2.imread(card)
        dst = cv2.resize(img,None,fx=0.7,fy=0.7,interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(card,dst)
        