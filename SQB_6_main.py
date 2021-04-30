# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:35:26 2021

@author: Sardor Mirzaev
"""

import SQB_6_functions as func3
import SQB_5_functions as func2
import SQB_6_adds as adds
import SQB_4_functions as func
import pandas as pd 
import numpy as np
import pickle 
import os
os.chdir('D:/ne_udal/11')

#%%
header_2=pd.read_excel('template_for_classification.xlsx','Sheet2', header=None)
header_3=pd.read_excel('template_for_classification.xlsx','Sheet3', header=None)
crops=pd.read_excel('risc_guar2.xlsx', header=None)
crops=crops.iloc[:,1:-1]
# calling binary object 
dataset=pickle.load(open('credit_portfel','rb'))

#%%

dat2=adds.builder_april_10(dataset,crops,header_2,header_3,0) 

 #%%
##Save File to Excel Sheet
name3='10_table_' +str(today)+'.xlsx'
func3.collect_excel(dat2,name3) 

#%%