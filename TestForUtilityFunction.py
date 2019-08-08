# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:00:00 2019

@author: t-takizawa
"""
#%%

## NEXT STEP : MADE easier to insert function

# Choose choices that has highest efficient function
class ChooseBestChoice():
    def ___init__(self):
        self.choice = {}
        
    
    def ChooseOne(self):
        choice = self.choice
        choice_sorted = sorted(choice.items(), key = lambda x: x[1])
        print(choice_sorted)
        num = choice_sorted[-1][0]
        print(num)
        return num
    
K = ChooseBestChoice()
K.choice = {"1":21,"2":32,"3":12}
T = K.ChooseOne()

        
        

