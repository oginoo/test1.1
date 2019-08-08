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

os.chdir('C:/Users/t-takizawa/Documents/Python Scripts')

#read Excel File as DataFrame
#data_ex = pd.read_excel('SampleData.xlsx','Sheet1')
data_ex = pd.read_csv('Post2Ninku.csv')

#Drop index and columns with all nan
df1 = data_ex.dropna(how = 'all')
df1 = df1.dropna(how = 'all',axis = 1)

Ldf1_col = len(df1.columns)
Tcol = []


for i in range(Ldf1_col):
    text = 'c' + str(i+1)
    Tcol.append(text)

df1.columns = Tcol

#%% Data Handling %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#Choose 
Dy = df1.loc[1:10,'c6']
Dx = df1.loc[1:10,'c5']
#Dy = df1.loc[6,'c3':]
#Dy = df1.loc[1:13,'c2']
#Dx = df1.loc[1:4,'c3':]
#Dx = df1.loc[1:13,'c3':'c4']

Ldy = len(Dy)
Ldx = len(Dx[:,:])

My = np.array(Dy,dtype = float).reshape(Ldy,1)
# Need T, depends on the data you use
Mx = np.array(Dx,dtype = float).T.reshape(Ldy,Ldx[0])


Lmi = len(Mx[:,1])
Mx_ad = np.ones([Lmi,1],dtype = float)
Mx = np.append(Mx,Mx_ad,axis=1)

#%%

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