import pandas as pd
import numpy as np
import cv2

import os
import random as ran

class PokerGame():
    def __init__(self):
        clubs = os.listdir('./images/Cards/clubs')
        diamonds = os.listdir('./images/Cards/diamonds')
        hearts = os.listdir('./images/Cards/hearts')
        spades = os.listdir('./images/Cards/spades')

        clubs_list = [f'./images/Cards/clubs/{i}' for i in clubs]
        diamonds_list = [f'./images/Cards/diamonds/{i}' for i in diamonds]
        hearts_list = [f'./images/Cards/hearts/{i}' for i in hearts]
        spades_list = [f'./images/Cards/spades/{i}' for i in spades]

        self.cardsImg = [spades_list, diamonds_list, hearts_list, clubs_list]
        self.cards = [x for x in range(52)]
        self.community_card = []

    def pre_flop(self,users: dict):
        for _ in range(2):
            for user in users.values():
                card = ran.choice(self.cards)
                user.drow_hands(card)
                self.cards.pop(self.cards.index(card))

    def flop(self):
        for _ in range(3):
            card = ran.choice(self.cards)
            self.community_card.append(card)
            self.cards.pop(self.cards.index(card))
            
    def turn(self):
        card = ran.choice(self.cards)
        self.community_card.append(card)
        self.cards.pop(self.cards.index(card))

    def river(self):
        card = ran.choice(self.cards)
        self.community_card.append(card)
        self.cards.pop(card)

    def get_cards_image(self,num: int) -> str:
        card_type = num//13 # 카드별로 13장 있음
        card_num = num%13 # 카드 숫자
        return self.cardsImg[card_type][card_num]
    
    def get_community_card(self) -> list:
        return self.community_card
    
    def merge_image(self,card: list) -> str:
        img = None
        for i in card:
            card_path = self.get_cards_image(i)
            if img is None:
                img = cv2.imread(card_path)
            else:
                temp = cv2.imread(card_path)
                img = np.hstack((img,temp))
        
        path = './images/temp/temp.png'
        cv2.imwrite(path,img)
        return path