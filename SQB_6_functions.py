# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:45:31 2021

@author: Sardor Mirzaev
"""

def for_types_1(measured):
    import pandas as pd
    sf6_trade=measured
    s1=pd.DataFrame(columns=range(0,1),index=range(0,6))
    s1.index=["Физические лица","Государственные предприятия",\
              "Совместные и иностранные предприятия",\
              "Частные товарищества и корпорации",'Правительство','Прочие']
    for i in s1.index:
        for s in sf6_trade.index:
            if i==s:
                s1.loc[i] =sf6_trade[s]
    s1=s1.fillna(0)
    s1=s1.rename(columns={0: sf6_trade.name})
    return s1

def for_types_agro(measured):
    import pandas as pd
    sf6_trade=measured
    s1=pd.DataFrame(columns=range(0,1),index=range(0,7))
    s1.index=["Физические лица","Государственные предприятия",\
              "Совместные и иностранные предприятия",\
              "Частные товарищества и корпорации",\
              'Фермерское хозяйство','Правительство','Прочие']
    for i in s1.index:
        for s in sf6_trade.index:
            if i==s:
                s1.loc[i] =sf6_trade[s]
    s1=s1.fillna(0)
    s1=s1.rename(columns={0: sf6_trade.name})
    return s1

def for_types_util(measured):
    import pandas as pd
    s1=pd.DataFrame(columns=range(0,1),index=range(0,7))
    s1.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                  'Правительство','Негосударственные некоммерческие организации',
                  'Прочие']
    if measured.empty:
        s1=s1.fillna(0)
        s1=s1.rename(columns={0: "Жилищно-коммунальные услуги"})
        return s1
    else:
        sf6_trade=measured
        for i in s1.index:
            for s in sf6_trade.index:
                if i==s:
                    s1.loc[i] =sf6_trade[s]
        s1=s1.fillna(0)
        s1=s1.rename(columns={0: sf6_trade.name})
        return s1
     
def for_types_others(measured):
    import pandas as pd
    sf6_trade=measured
    s1=pd.DataFrame(columns=range(0,1),index=range(0,11))
    s1.index=["Физические лица","Государственные предприятия",\
              "Совместные и иностранные предприятия",\
              "Частные товарищества и корпорации",\
             'Центральный банк', 'Другие банки',\
              'Правительство','Небанковские финансовые институты',\
              'Негосударственные некоммерческие организации',
              'Бюджетные организации','Прочие']
    for i in s1.index:
        for s in sf6_trade.index:
            if i==s:
                s1.loc[i] =sf6_trade[s]
    s1=s1.fillna(0)
    s1=s1.rename(columns={0: sf6_trade.name})
    return s1

def for_types_total(measured):
    import pandas as pd
    sf6_trade=measured
    s1=pd.DataFrame(columns=range(0,1),index=range(0,12))
    s1.index=["Физические лица","Государственные предприятия",\
              "Совместные и иностранные предприятия",\
              "Частные товарищества и корпорации",'Фермерское хозяйство',\
              'Другие банки','Центральный банк','Правительство',\
              'Небанковские финансовые институты',\
              'Негосударственные некоммерческие организации',
              'Бюджетные организации','Прочие']
    for i in s1.index:
        for s in sf6_trade.index:
            if i==s:
                s1.loc[i] =sf6_trade[s]
    s1=s1.fillna(0)
    s1=s1.rename(columns={0: sf6_trade.name})
    return s1


def types_provision(dataframe,number,include_foreign):
    import pandas as pd
    import SQB_6_adds as adds
    import SQB_4_functions as func
    new_dd=dataframe
    number=str(number)
    if include_foreign==False:
        new_2=new_dd[(new_dd['КодОбес']==number)]
        look_state=pd.DataFrame()
        for i in new_2['тип клиента'].unique():
            sz=new_2[(new_2['КодОбес']==number)&(new_2['тип клиента']==str(i))]
            look_state[i]=adds.builder_sum_credit(sz,0) 
            #sz=new_2[(new_2['КодОбес']==number)&(new_2['тип клиента']!=str(i))]
        look_state=look_state.replace(0,'')
        look_state['fin']=look_state.apply(lambda x : "".join([str(x[i])\
                  for i in range(len(x))]),axis=1) 
        look_state['fin']=look_state['fin'].apply(lambda x:\
                  func.int_float_none(x)).fillna(0)
        look_state.loc['Итого кредита и лизинга'][-1]=look_state['fin'][-13:-1].sum()
#        look_state['fin'][-1]=look_state['fin'][-13:-1].sum()
#        look_state['fin']=look_state['fin'].apply(lambda x: func.int_float_none(x))
        
        return look_state['fin']   
    
    if include_foreign==True:
        new_2=new_dd[(new_dd['КодОбес']==number)&(new_dd['КодВал']!='000')]
        look_state=pd.DataFrame()
        for i in new_2['тип клиента'].unique():
            sz=new_2[(new_2['КодОбес']==number)&(new_2['тип клиента']==str(i))]
            look_state[i]=adds.builder_sum_credit(sz,0) 
            #sz=new_2[(new_2['КодОбес']==number)&(new_2['тип клиента']!=str(i))]
        look_state=look_state.replace(0,'')
        look_state['fin']=look_state.apply(lambda x : "".join([str(x[i])\
                  for i in range(len(x))]),axis=1) 
        look_state['fin']=look_state['fin'].apply(lambda x: \
                  func.int_float_none(x)).fillna(0)
        look_state.loc['Итого кредита и лизинга'][-1]=look_state['fin'][-13:-1].sum()
        #look_state['fin'][-1]=look_state['fin'][-13:-1].sum()
        #look_state['fin']=look_state['fin'].apply(lambda x: func.int_float_none(x))
        return look_state['fin']
def cat_all(df):
    target= [25,21,22,43,76,44,24,26,42,23,27,29,\
             30,41,51,35,61,33,37,39,73,74]
    new_dd=df
    import time
    import pandas as pd 
    import numpy as np
    tic= time.time()
    a_=pd.DataFrame()
    print("------ Computing...------") 
    for i in target:
        try:
            a_[i]=types_provision(new_dd,i,False)
        except KeyError:
            a_[i]=np.zeros(76)
    a_=a_.fillna(0)
    print("------ Computation is completed ------") 
    toc = time.time()
    hours, rem = divmod(toc-tic,3600)
    minutes,seconds=divmod(rem,60)
    print("Computation time " +"{:0>2}:{:0>2}:{:05.2f}".\
          format(int(hours),int(minutes),seconds))          
    return a_
def collect_excel(dataframe,name):
    import pandas as pd
    writer = pd.ExcelWriter(name, engine='xlsxwriter')
    dataframe=dataframe.fillna(0)
    dataframe.replace(0,'0')
    dataframe.to_excel(writer, index=False, header=False,startcol=1,\
                    startrow=3, sheet_name='Sheet1')
    
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    #Add a header format.
    header_format = workbook.add_format({
        'bold': False,
        'text_wrap':True,
        'valign': 'center',
        'fg_color': '#D7E4BC',
        'border': 1})
    #header_format.set_rotation(90)
    header_format.set_text_wrap()
    
    # Write the column headers with the defined format.
    for col_num, value in enumerate(dataframe.columns[0:].values):
         worksheet.write(2, col_num + 1, value, header_format)
    cellFormat = workbook.add_format({
            'num_format': '### ### ### ### ##0'}) 
    cellFormat2= workbook.add_format({
            'bold': 'True','num_format': '### ### ### ### ##0',
            'fg_color': '#D7E4BC'})  
    cellFormat4= workbook.add_format({
            'num_format': '0.00%' })                              
#    worksheet.set_column('G:X', 20, cellFormat)
    worksheet.set_column('B:B', 8, cellFormat)
    worksheet.set_column('C:C', 40, cellFormat)
    worksheet.set_column('C:C', 40, cellFormat)
    worksheet.set_column('D:E', 20, cellFormat)
    worksheet.set_column('G:G', 20, cellFormat)
    worksheet.set_column('I:Z', 20, cellFormat)
    worksheet.set_column('F:F', 10, cellFormat4)
    worksheet.set_column('H:H', 10, cellFormat4)
    
    worksheet.set_row(2,15,header_format)   
    worksheet.set_row(4,15,cellFormat2)
    worksheet.set_row(11,15,cellFormat2)
    worksheet.set_row(12,15,cellFormat2)
    worksheet.set_row(20,15,cellFormat2)
    worksheet.set_row(21,15,cellFormat2)
    worksheet.set_row(28,15,cellFormat2)
    worksheet.set_row(29,15,cellFormat2)
    worksheet.set_row(36,18,cellFormat2)
    worksheet.set_row(37,18,cellFormat2)
    worksheet.set_row(44,18,cellFormat2)
    worksheet.set_row(45,18,cellFormat2)
    worksheet.set_row(52,18,cellFormat2)
    worksheet.set_row(53,18,cellFormat2)
    worksheet.set_row(61,18,cellFormat2)
    worksheet.set_row(62,18,cellFormat2)
    worksheet.set_row(74,18,cellFormat2)
    worksheet.set_row(75,18,cellFormat2)
    worksheet.set_row(88,18,cellFormat2)
    worksheet.conditional_format('F12:F89', {'type':'cell',\
                                'criteria':'!=', 'value':'0.00%',
                                    'format': cellFormat4})
    worksheet.conditional_format('H12:H89', {'type':'cell',\
                                'criteria':'!=', 'value':'0.00%',
                                    'format': cellFormat4})
    workbook.close()    
    print('---- Table has been saved with .xlsx format ----' )
          
def insert_row(row_number, df, row_value):
    	start_upper = 0
    	end_upper = row_number
    	start_lower = row_number
    	end_lower = df.shape[0]
    	upper_half = [*range(start_upper, end_upper, 1)]
    	lower_half = [*range(start_lower, end_lower, 1)]
    	lower_half = [x.__add__(1) for x in lower_half]
    	index_ = upper_half + lower_half
    	df.index = index_
    	df.loc[row_number] = row_value
    	df = df.sort_index()
    	return df


def main():
    for_types_1()
    for_types_agro()
    for_types_util()
    for_types_total()
    for_types_others()
    types_provision()
    insert_row()
    collect_excel()
    cat_all()
if __name__=="__main__":
    main()
print("Completed")