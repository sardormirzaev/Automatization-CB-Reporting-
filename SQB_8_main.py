# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:07:54 2021

@author: Sardor Mirzaev
"""

import pandas as pd 
import pickle 
import SQB_8_adds as adds8
import SQB_8_functions as func8
from datetime import date
today=str(date.today()) 
########################################################
dataset=pickle.load(open('credit_portfel','rb'))

helper=pd.read_csv('helper_table_2.txt',header=None, dtype=str)
helper0=pd.read_excel('Баланс_Стандарт.xlsx',header=None, dtype=str)


# Choose the name of the table 
exp2='2_table_'+str(today)+'.xlsx'
########################################################

dat_2tab=adds8.builder_2_table(dataset,helper,helper0)
#%%

func8.two_to_excel(dat_2tab,exp2)
#%%
