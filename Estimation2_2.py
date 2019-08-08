# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:55:02 2019

@author: t-takizawa
"""
#%%
import pandas as pd
import numpy as np
from  scipy import linalg as LA
import os

class EstimateData():
    def __init__(self,name):
        data_ex = pd.read_csv(name)
        df1 = data_ex.dropna(how = 'all')
        df1 = df1.dropna(how = 'all',axis = 1)
        Ldf1_col = len(df1.columns)
        Tcol = []
        
        # Add column name
        for i in range(Ldf1_col):
            text = 'c' + str(i+1)
            Tcol.append(text)
        df1.columns = Tcol
        self.df1 = df1
    
    def ShowDf1(self):
        print(self.df1)
    
    def EstimateData(self,Dx,Dy):
        Ldy = len(Dy)
        Ldx = len(Dx)
        
        My = np.array(Dy,dtype = float).reshape(Ldy,1)
        # Need T, depends on the data you use
        print("Ldx:",Ldx,"\n")
        Mx = np.array(Dx,dtype = float).T.reshape(Ldy,1)
        
        
        Lmi = len(Mx)
        Mx_ad = np.ones([Lmi,1],dtype = float)
        Mx = np.append(Mx,Mx_ad,axis=1)
        
        
        
        Mxy = np.dot(Mx.T,My)
        Mxx = np.dot(Mx.T,Mx)
        Mxx01 = LA.inv(Mxx)
        
        a = np.dot(Mxx01,Mxy)  
        
        Mxa = np.dot(Mx,a)
        
        # Calculate Mean My
        Mmy = np.mean(My)
        
        Rf = np.dot(My.T,My) - 2 * np.dot(Mxa.T, My) + \
             np.dot(Mxa.T,Mxa)
             
        Tf = np.dot((My-Mmy).T,(My-Mmy))
        
        n = len(Mx[:,1]) #Sample size
        k = len(Mx[1,:]) #Variable size
        
        R2R = 1 - Rf/Tf
        R2 = 1 - ( Rf/(n-k - 1) )  /  (Tf / (n - 1))
        self.R2R = R2R
        self.R2 = R2
        self.a = a
        
        pa = "Results--------------------------------------\nVariables:\n" + str(a[:,:-1])
        pa2 = "Constants:" + str(a[-1])
        pb = "Regression degree:         " + str(R2R)
        pc = "Multiple Regression degree:" + str(R2)
        print(pa)
        print(pa2)
        print(pb)
        print(pc)
        print("---------------------------------------------")
        return a

os.chdir('C:/Users/t-takizawa/Documents/Python Scripts')
import Estimation2_2 as ES
#os.chdir('C:/Users/takiz/Documents/Python/EstimationBM')
K = ES.EstimateData('Post2Ninku.csv')

df1 = K.df1
Dy = df1.loc[1:10,'c6']
Dx = df1.loc[1:10,'c5']
a = K.EstimateData(Dx,Dy)

