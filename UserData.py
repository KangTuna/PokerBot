import pandas as pd

class User():
    def __init__(self,user):
        self.user = user
        self.hands = []

    def drow_hands(self,card: int) -> None:
        self.hands.append(card)
    
    def get_hands(self) -> list:
        return self.hands
    
    def get_user_class(self):
        return self.user