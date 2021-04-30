# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:57:15 2021

@author: 49151
"""


'Asset Classification'
import pandas as pd
import SQB_4_functions as func
import SQB_5_functions as func2
from datetime import date
today=str(date.today())
header=pd.read_excel('template_for_classification.xlsx','Sheet1', header=None)
standard=pd.read_excel('Стандарт.xlsx', header=None)
output_name= '8_table_' +str(today)+'.xlsx'
################################# ЧИТАТЬ ЧИТАТЬ ЧИТАТЬ ########################
############ ПЕРВЫМ ЗАПУСКАЙТЕ МОДУЛЬ SQB_4_MAIN.py ДО СТРОКИ 30 ###
dataset=pickle.load(open('credit_portfel.pickle','rb'))
frame=func2.calc_2(dataset,header,standard) #dataset is the result from SQB_4_main.py
func2.collect(frame,output_name)
#%%
