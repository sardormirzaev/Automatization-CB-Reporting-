# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:34:50 2021

@author: Sardor Mirzaev
"""
import os
from datetime import date
today=str(date.today()) 
###############################################
#os.chdir("d:/SQB_val_prog/Script/") # Choose  the directory
import_1= 'fin_26.xlsx' # Choose  the data 
import_2='key interest_for_table_lgot.xlsx'
export_1= 'export_' +str(today)+'.xlsx' # Choose name to save the file 

################################################
import pandas as pd
import SQB_4_adds as sqb
import SQB_4_functions as func

corporates=pd.read_csv('corp2.txt',header=None, dtype=str) # Choose from for Corporates
##################################################
#%%
## Importing the data
LC_data,FC_data,df=sqb.import_data(import_2,import_1)
#%%
#### Execute the funtions and create a complete dataset
ad=pd.concat([sqb.datetrim(df),\
              sqb.df_builder(df,LC_data,FC_data,  corporates)],axis=1)
dataset=sqb.add_top_rows(df,ad)

#serialization of the object  
import pickle 
pickle_out=open('credit_portfel','wb')
pickle.dump(dataset,pickle_out)
pickle_out.close
          
#%%
##Export results to excell
func.export_to_excel(dataset,export_1)
#%%
