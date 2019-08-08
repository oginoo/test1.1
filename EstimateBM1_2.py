# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:22:37 2019

@author: takiz
"""
#%%
import json
import pandas as pd
import numpy as np

class EstimateBM:
    def __init__(self,File,Type2,Type1="管理体制"):
        with open(File,"r") as f:
            data = json.load(f)
        self.jsonData = data 
        self.Type2 = Type2
        self.Type1 = "管理体制"
        
    def Json2DFrame(self):
        t = 0
        
        data = self.jsonData
        Type2 = self.Type2
        for i in data:
            
            list1 = [i,Type2]
            list2 = []
            for j in data[i][self.Type1][self.Type2]:
                cont = data[i][self.Type1][self.Type2][j]
                if isinstance(cont,dict) == False:
                    list1.append(cont)
                    list2.append(j)
            t = t + 1
            print(t)
            if t == 1:
                columnsIN = ["Project","Type2",list2[0],list2[1],list2[2]]
                listM = np.array(list1).reshape(1,5)
                listM = pd.DataFrame(listM,columns = columnsIN)
            else:
                listM.loc[t - 1] = list1
        self.list1 = list1
        self.listM = listM
        
        return listM
    
    def Json2DFrameTotal(self):
        n_member = ["設備","警備","ゲート立哨","オフィス受付"]
        len_m = len(n_member)
        
        self.Tupe2 = n_member[0]
        listM = self.Json2DFrame()
        
        #n_len -1 because 0 is already conducted
        for i in range(1, len_m - 1):
            self.Type2 = n_member[i]
            listT = self.Json2DFrame()
            listM = listM.append(listT)
            
        self.listM = listM
            
        
                
import EstimateBM1_2 as EBM

K = EBM.EstimateBM("output.json","設備")
K.Json2DFrameTotal()
T = K.listM
print(K.listM)

T.to_csv('Post2Ninku.csv', index = True, header = True)

