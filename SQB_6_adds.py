# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:21:01 2021
@author: Sardor Mirzaev
"""

def builder_sum_credit(dataframe,w_average):
    import pandas as pd
    import SQB_6_functions as func3
    new_dd=dataframe
    
    #new_dd['otr']=new_dd['СекторКлиентаДляОтчетов'].str[2:]
    if w_average==0:
        s1=pd.DataFrame()
        s=pd.DataFrame()
        for  i in new_dd['тип клиента'].unique():
            stand2=new_dd[new_dd['тип клиента']==str(i)]
            s[i]=stand2.groupby(by=['СекторКлиентаДляОтчетов']).ВсегоЗадолженность.sum()
        sv11=s.T
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str(i)]
            s1[i]=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
            sv1=s1
        svav=sv11.combine_first(sv1)
        svav.sum()
        
        ss=pd.DataFrame()
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str('2-Сельское хозяйство')]
            ss['2-Сельское хозяйство']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav2=ssv1.combine_first(svav)
        svav2.sum()
        
        ss=pd.DataFrame()
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str('6-Материально-техническое снабжение и сбыт')]
            ss['6-Материально-техническое снабжение и сбыт']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav2=ssv1.combine_first(svav2)
        svav2.sum()
        
        ss=pd.DataFrame()
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str('1-Промышленность')]
            ss['1-Промышленность']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        
        svav3=ssv1.combine_first(svav2)
        ss=pd.DataFrame()
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str('3-Транспорт и коммуникации')]
            ss['3-Транспорт и коммуникации']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav4=ssv1.combine_first(svav3)
        
        ss=pd.DataFrame()
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str('4-Строительство')]
            ss['4-Строительство']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav5=ssv1.combine_first(svav4)
        svav5.sum()
        ss=pd.DataFrame()
        for  i in new_dd['СекторКлиентаДляОтчетов'].unique():
            stand2=new_dd[new_dd['СекторКлиентаДляОтчетов']==str('8-Другие отрасли')]
            ss['8-Другие отрасли']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav6=svav5.combine_first(ssv1)
        svav6.sum()
        
        sv=svav6
        sv.columns=['Промышленность', 'Сельское хозяйство',
           'Транспорт и коммуникации', 'Строительство',
           'Торговля и общественное питание',
           'Материально-техническое снабжение и сбыт',
           'Жилищно-коммунальные услуги', 'Другие отрасли']        
        
    if w_average==1:
        s=pd.DataFrame()
        s1=pd.DataFrame()
        for  i in new_dd['тип клиента'].unique():
            stand2=new_dd[new_dd['тип клиента']==str(i)]
            s[i]=stand2.groupby(by=['otr']).средневзвеш.sum()
        sv11=s.T
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str(i)]
            s1[i]=stand2.groupby(by=['тип клиента']).средневзвеш.sum()
        sv1=s1
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Сельское хозяйство')]
            ss['Сельское хозяйство']=stand2.groupby(by=['тип клиента']).средневзвеш.sum()
        ssv1=pd.DataFrame(ss)
        
        sv2=ssv1.combine_first(sv1)
        sv=sv11.combine_first(sv2)
        
    list1=['Промышленность','Транспорт и коммуникации','Строительство',\
           'Торговля и общественное питание',\
          'Материально-техническое снабжение и сбыт']
    v_mat=pd.DataFrame(columns=list1,index=sv.index)
    for i in v_mat.index:
        for s in sv.index:
            if i==s:
                v_mat.loc[i] = sv.loc[s,:]
    v_mat=v_mat.fillna(0)
    try: 
        vob=sv[['Промышленность','Транспорт и коммуникации','Строительство',\
               'Торговля и общественное питание',\
               'Материально-техническое снабжение и сбыт']]
    except KeyError:
        sq1=sv.combine_first(v_mat)
        vob=sq1[list1]
    s2=pd.DataFrame()
    for i in vob:   
        s2[[i]]=func3.for_types_1(vob[i])
    s2.loc['Итого']=s2.sum()  
    s2['by_client']=s2.sum(axis=1)  
    
    s3=pd.DataFrame()
    try: 
        s3[["Сельское хозяйство"]]=func3.for_types_agro(sv['Сельское хозяйство'])
    except KeyError:
        s3=pd.DataFrame(columns=range(0,1),index=range(0,7))
        s3.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                  'Фермерское хозяйство','Правительство','Прочие']
        s3=s3.fillna(0)
        s3=s3.rename(columns={0: "Сельское хозяйство"})
    s3.loc['Итого']=s3.sum(axis=0) 
    s3['by_client']=s3.sum(axis=1)  
    
    h1=pd.DataFrame()
    stand2=new_dd[new_dd['тип клиента']==str\
                      ('Негосударственные некоммерческие организации')]
    if w_average==0:
        h1['Негосударственные некоммерческие организации']=stand2\
            .groupby(by=['otr']).ВсегоЗадолженность.sum()
        sv1=h1.T   
          
    if w_average==1:
        h1['Негосударственные некоммерческие организации']=stand2\
            .groupby(by=['otr']).средневзвеш.sum()
        sv1=h1.T   
    
    s4=pd.DataFrame()         
    try:
        s4[["Жилищно-коммунальные услуги"]]=func3\
        .for_types_util(sv1['Жилищно-коммунальные услуги']) 
    except KeyError:
        s4=pd.DataFrame(columns=range(0,1),index=range(0,7))
        s4.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                  'Правительство',\
                  'Негосударственные некоммерческие организации','Прочие']
        s4=s4.fillna(0)
        s4=s4.rename(columns={0: "Жилищно-коммунальные услуги"})
    s4.loc['Итого']=s4.sum(axis=0) 
    s4['by_client']=s4.sum(axis=1)  
    
    s5=pd.DataFrame()
    try:
        s5[["Другие отрасли"]]=func3\
        .for_types_others(sv['Другие отрасли'])
    except KeyError:
        s5=pd.DataFrame(columns=range(0,1),index=range(0,11))
        s5.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                 'Центральный банк', 'Другие банки',\
                  'Правительство','Небанковские финансовые институты',\
                  'Негосударственные некоммерческие организации',
                  'Бюджетные организации','Прочие']
        s5=s5.fillna(0)
        s5=s5.rename(columns={0: "Другие отрасли"})
    s5.loc['Итого']=s5.sum(axis=0) 
    s5['by_client']=s5.sum(axis=1)  
    
    
    lov1=pd.concat([s2.Промышленность,s3['Сельское хозяйство'],\
                    s2['Транспорт и коммуникации'],\
                    s2.Строительство,s2['Торговля и общественное питание'],\
                    s2['Материально-техническое снабжение и сбыт'],\
                  s4['Жилищно-коммунальные услуги'],s5['Другие отрасли'] ],axis=0)
    
    
    lov2=pd.concat([s2.by_client,s3.by_client,s4.by_client,s5.by_client],axis=1)
    lov2=lov2.drop(['Итого'])
    lov2['sum']=lov2.sum(axis=1)
    
    s6=pd.DataFrame()   
    s6=func3.for_types_total(lov2['sum'])
    s6.loc['Итого кредита и лизинга']=s6.sum()
    lov3=pd.concat([lov1,s6],axis=0)
    lov3['Сумма']=lov3[0].combine_first(lov3['sum'])
    #return sv
    return lov3['Сумма']

def builder_sum_credit_new(dataframe,w_average,summer):
    import pandas as pd
    import SQB_6_functions as func3
    new_dd=dataframe
    new_dd['ВсегоЗадолженность']=summer
    if w_average==0:
        s=pd.DataFrame()
        s1=pd.DataFrame()
        for  i in new_dd['тип клиента'].unique():
            stand2=new_dd[new_dd['тип клиента']==str(i)]
            s[i]=stand2.groupby(by=['otr']).ВсегоЗадолженность.sum()
        sv1=s.T
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str(i)]
            s1[i]=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        sv1=s1
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Сельское хозяйство')]
            ss['Сельское хозяйство']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        
        svav=ssv1.combine_first(sv1)
        #svav=sv2.combine_first(ssv1)

        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Материально-техническое снабжение и сбыт')]
            ss['Материально-техническое снабжение и сбыт']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav2=svav.combine_first(ssv1)
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Промышленность')]
            ss['Промышленность']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        
        svav3=svav2.combine_first(ssv1)
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Транспорт и коммуникации')]
            ss['Транспорт и коммуникации']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav4=svav3.combine_first(ssv1)
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Строительство')]
            ss['Строительство']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav5=svav4.combine_first(ssv1)
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Другие отрасли')]
            ss['Другие отрасли']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav6=svav5.combine_first(ssv1)
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Торговля и общественное питание')]
            ss['Торговля и общественное питание']=stand2.groupby(by=['тип клиента']).ВсегоЗадолженность.sum()
        ssv1=pd.DataFrame(ss)
        svav7=svav6.combine_first(ssv1)
        
        sv=svav7.combine_first(ssv1)
        

    if w_average==1:
        s=pd.DataFrame()
        s1=pd.DataFrame()
        for  i in new_dd['тип клиента'].unique():
            stand2=new_dd[new_dd['тип клиента']==str(i)]
            s[i]=stand2.groupby(by=['otr']).средневзвеш.sum()
        sv11=s.T
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str(i)]
            s1[i]=stand2.groupby(by=['тип клиента']).средневзвеш.sum()
        sv1=s1
        ss=pd.DataFrame()
        for  i in new_dd['otr'].unique():
            stand2=new_dd[new_dd['otr']==str('Сельское хозяйство')]
            ss['Сельское хозяйство']=stand2.groupby(by=['тип клиента']).средневзвеш.sum()
        ssv1=pd.DataFrame(ss)
        
        sv2=ssv1.combine_first(sv1)
        sv=sv11.combine_first(sv2)
    list1=['Промышленность','Транспорт и коммуникации','Строительство',\
           'Торговля и общественное питание',\
          'Материально-техническое снабжение и сбыт']
    v_mat=pd.DataFrame(columns=list1,index=sv.index)
    for i in v_mat.index:
        for s in sv.index:
            if i==s:
                v_mat.loc[i] = sv.loc[s,:]
    v_mat=v_mat.fillna(0)
    try: 
        vob=sv[['Промышленность','Транспорт и коммуникации','Строительство',\
               'Торговля и общественное питание',\
               'Материально-техническое снабжение и сбыт']]
    except KeyError:
        sq1=sv.combine_first(v_mat)
        vob=sq1[list1]
    s2=pd.DataFrame()
    for i in vob:   
        s2[[i]]=func3.for_types_1(vob[i])
    s2.loc['Итого']=s2.sum(axis=0)  
    s2['by_client']=s2.sum(axis=1)  
    
    s3=pd.DataFrame()
    try: 
        s3[["Сельское хозяйство"]]=func3.for_types_agro(sv['Сельское хозяйство'])
    except KeyError:
        s3=pd.DataFrame(columns=range(0,1),index=range(0,7))
        s3.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                  'Фермерское хозяйство','Правительство','Прочие']
        s3=s3.fillna(0)
        s3=s3.rename(columns={0: "Сельское хозяйство"})
    s3.loc['Итого']=s3.sum(axis=0) 
    s3['by_client']=s3.sum(axis=1)  
    
    h1=pd.DataFrame()
    stand2=new_dd[new_dd['тип клиента']==str\
                      ('Негосударственные некоммерческие организации')]
    if w_average==0:
        h1['Негосударственные некоммерческие организации']=stand2\
            .groupby(by=['otr']).ВсегоЗадолженность.sum()
        sv1=h1.T   
          
    if w_average==1:
        h1['Негосударственные некоммерческие организации']=stand2\
            .groupby(by=['otr']).средневзвеш.sum()
        sv1=h1.T   
    
    s4=pd.DataFrame()         
    try:
        s4[["Жилищно-коммунальные услуги"]]=func3\
        .for_types_util(sv1['Жилищно-коммунальные услуги']) 
    except KeyError:
        s4=pd.DataFrame(columns=range(0,1),index=range(0,7))
        s4.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                  'Правительство',\
                  'Негосударственные некоммерческие организации','Прочие']
        s4=s4.fillna(0)
        s4=s4.rename(columns={0: "Жилищно-коммунальные услуги"})
    s4.loc['Итого']=s4.sum(axis=0) 
    s4['by_client']=s4.sum(axis=1)  
    
    s5=pd.DataFrame()
    try:
        s5[["Другие отрасли"]]=func3\
        .for_types_others(sv['Другие отрасли'])
    except KeyError:
        s5=pd.DataFrame(columns=range(0,1),index=range(0,11))
        s5.index=["Физические лица","Государственные предприятия",\
                  "Совместные и иностранные предприятия",\
                  "Частные товарищества и корпорации",\
                 'Центральный банк', 'Другие банки',\
                  'Правительство','Небанковские финансовые институты',\
                  'Негосударственные некоммерческие организации',
                  'Бюджетные организации','Прочие']
        s5=s5.fillna(0)
        s5=s5.rename(columns={0: "Другие отрасли"})
    s5.loc['Итого']=s5.sum(axis=0) 
    s5['by_client']=s5.sum(axis=1)  
    
    
    lov1=pd.concat([s2.Промышленность,s3['Сельское хозяйство'],\
                    s2['Транспорт и коммуникации'],\
                    s2.Строительство,s2['Торговля и общественное питание'],\
                    s2['Материально-техническое снабжение и сбыт'],\
                  s4['Жилищно-коммунальные услуги'],s5['Другие отрасли'] ],axis=0)
    
    
    lov2=pd.concat([s2.by_client,s3.by_client,s4.by_client,s5.by_client],axis=1)
    lov2=lov2.drop(['Итого'])
    lov2['sum']=lov2.sum(axis=1)
    
    s6=pd.DataFrame()   
    s6=func3.for_types_total(lov2['sum'])
    s6.loc['Итого кредита и лизинга']=s6.sum()
    lov3=pd.concat([lov1,s6],axis=0)
    lov3['Сумма']=lov3[0].combine_first(lov3['sum'])
    #return sv
    return lov3['Сумма']

    
def builder_special(df_from_cat_all,dataframe,header_2,header_3):
    import pandas as pd 
    import numpy as np
    import SQB_4_functions as func
    import SQB_6_functions as func3
    a_=df_from_cat_all/1000
    aa_oborud=a_[[26,24]].sum(axis=1)
    aa_garant=a_[[43,76]].sum(axis=1)
    aa_poruch=a_[[44,41]].sum(axis=1)
    aa_neobes=a_[[35,61]].sum(axis=1)
    aa_realest=a_[[76,21,22]].sum(axis=1)
    realest_fiz=pd.Series(np.where(aa_realest.index=='Физические лица',aa_realest,0))
    realest_fiz[75]=realest_fiz[63]
    realest_fiz.index=aa_realest.index
    realest_comm=pd.Series(np.where(aa_realest.index!='Физические лица',aa_realest,0))
    realest_comm[75]=realest_comm[64:75].sum()
    realest_comm.index=aa_realest.index 
    aaa_=a_[[33,37,39,73,74]].sum(axis=1)

    new_dd=dataframe
    new_dd=new_dd.fillna(0)
    new_dd2=new_dd[new_dd['КодВал']=='000']
    new_dd3=new_dd[new_dd['КодВал']!='000']
    look_nacval=builder_sum_credit(new_dd2,0)/1000
    look_fc=builder_sum_credit(new_dd3,0)/1000
    look_tot=(look_fc+look_nacval)
    #sred szveshanniy
    #prom=builder_sum_credit(new_dd,1)
    prom2=builder_sum_credit(new_dd2,1)/1000
    prom3=builder_sum_credit(new_dd3,1)/1000
    
    in_sum=prom2/look_nacval
    in_foreign=prom3/look_fc
    
    new_a=new_dd[new_dd['ОстатокВнебПроцентов']>0]
    new_b=new_dd[new_dd['ОстатокВнебПроцентов']==0]
    
    look_a=builder_sum_credit(new_a,0)/1000 
    look_b=builder_sum_credit(new_b,0)/1000
    try:
        a_42_fc=func3.types_provision(new_dd,42,True)/1000
    except KeyError:
        a_42_fc=np.zeros(76)
    ##preparing table to export 
    dataset2=pd.concat([look_tot,look_nacval,in_sum,look_fc,in_foreign,\
                        look_b,look_a,a_[25],a_[42],a_42_fc,\
                        a_[23],a_[27],aa_realest,realest_fiz,realest_comm,\
                        aa_oborud,a_[30],a_[29],\
                        aa_garant,aa_poruch,a_[51],aa_neobes,aaa_] ,axis=1)
    
    
    dataset2=dataset2.fillna(0)
    sz=list(dataset2.index)
    dataset2.index=range(0,len(dataset2))
    dataset2.loc[6]=dataset2.iloc[0:6,0:24].sum(axis=0)
    dataset2.loc[14]=dataset2.iloc[7:14,0:24].sum(axis=0)
    dataset2.loc[21]=dataset2.iloc[15:21,0:24].sum(axis=0)
    dataset2.loc[28]=dataset2.iloc[21:28,0:24].sum(axis=0)
    dataset2.loc[35]=dataset2.iloc[29:35,0:24].sum(axis=0)
    dataset2.loc[42]=dataset2.iloc[36:42,0:24].sum(axis=0)
    dataset2.loc[50]=dataset2.iloc[43:50,0:24].sum(axis=0)
    dataset2.loc[62]=dataset2.iloc[51:62,0:24].sum(axis=0)
    dataset2.loc[75]=dataset2.iloc[63:75,0:24].sum(axis=0)
    dataset2.index=sz
    col_names=['Сумма кредита','Сумма в нац. валюте',\
               'средне-взвешенные процентные ставки1' ,'Сумма в ин.валюте(экв.в сумах)',\
              'средне-взвешенные процентные ставки2','Начисляемые кредиты',\
              'Кредиты переведённые в статус ненаращивания процентов',\
              'Депозиты','Гарантированные Прав. РУ',\
              'Гарантированные Прав. РУ в ин.валюте(экв.в сумах)',\
              'Транспортные средства','Инвентарь','Недвижимость',\
              'жилая недвижимость','коммерческая недвижимость',\
              'Оборудование','Векселя (облигации)','Акции',\
              'Гарантия третьей стороны','Поручительства третьей стороны ',\
              'Страховой полис','Необеспеченные','Другое обеспечение']
    dataset2.columns=col_names
    dataset2['средне-взвешенные процентные ставки1']=in_sum
    dataset2['средне-взвешенные процентные ставки2']=in_foreign
    dataset2=dataset2.rename(columns={'средне-взвешенные процентные ставки1': \
                                      'средне-взвешенные процентные ставки',\
                                     'средне-взвешенные процентные ставки2':\
                                     'средне-взвешенные процентные ставки'})

    dataset2['index']=dataset2.index
    dataset2.insert(0, 'index', dataset2.pop('index'))
    dataset2.index=range(0,len(dataset2))
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Промышленность'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Сельское хозяйство'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Транспорт и коммуникации'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Строительство'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Торговля и общественное питание'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Материально-техническое снабжение и сбыт'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Жилищно-коммунальные услуги'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Другие отрасли'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Кредитные и лизинговые операции'
    dataset2.iloc[0,1:]= ''
    dataset2 = func3.insert_row(16, dataset2,dataset2.loc[7])
    dataset2 = func3.insert_row(25, dataset2,dataset2.loc[6])
    dataset2 = func3.insert_row(33, dataset2,dataset2.loc[5])
    dataset2 = func3.insert_row(41, dataset2,dataset2.loc[4])
    dataset2 = func3.insert_row(49, dataset2,dataset2.loc[3])
    dataset2 = func3.insert_row(57, dataset2,dataset2.loc[2])
    dataset2 = func3.insert_row(66, dataset2,dataset2.loc[1])
    dataset2 = func3.insert_row(79, dataset2,dataset2.loc[0])
    dataset2=dataset2.iloc[8:,:]

    es=list(header_3[1][4:])
    dataset2['Код']=es
    dataset2.insert(0,'Код', dataset2.pop('Код'))
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True)
    dataset2.iloc[0,1:]=[(i) for i in header_2.iloc[6,2:]]
    #dataset2.iloc[0,1:]=header_2.iloc[6,2:]
    return dataset2 

def builder_april_10(dataset,crops,header_2,header_3,category_column):
    import pandas as pd 
    import numpy as np
    import SQB_6_functions as func3
    new_dd1=selected_dataframe(dataset)
    sx=pd.Series(np.where(new_dd1['MFO_schet']=='0044015101840600117836012',0,new_dd1['КодОбес']))
    sx.replace(0,25)
    new_dd1['КодОбес']=sx
    
    #ax['MFO_schet']=ax["МФО"].astype(str) + ax["Кредит счёт"].astype(str)
    if category_column== 1: 
        
        ax=crops.iloc[3:,:]
        ax.columns=crops.iloc[2,:]
        ax['MFO_schet']=ax["МФО"].astype(str) + ax["Кредит счёт"].astype(str)
        axx=ax[['MFO_schet','Всего задолженность','Сумма обеспечения', '21-Недвижимость',
               '22-Недвижимость (ипотека)', '23-Транспортные средства',
               '24-Оборудование', '25-Депозит',
               '26-Товарно-материальные ценности(инвентарь)', '27-Товары в обороте',
               '29-Акции', '33 тип', '35-Не оплаченные счета (дебит.задолж.)',
               '37 тип', '38 тип', 
        '39 тип', '41-Поручительство третьих лиц',
               '42-Гарантия Правительства', '43-Гарантия третьей стороны',
               '44-Поручительство третьих лиц (2)', '51-Страховой полис',
               '61-Без обеспечения', '62 тип', '71-Транспортные средства (2)',
               '72 тип', '73-Имущественные права', '74-Денежные средства в обороте',
               '75-Недвижимость(индивидуадьные жилые дома',
               '76-Гарантия хокимиятов районов (городов)']]
    
    
        axx=axx.fillna(0)
        sss1=axx[(axx['Сумма обеспечения']==0.0) | (axx['Сумма обеспечения']==0)]
        sxx=[]
        for k, i in axx[['MFO_schet','74-Денежные средства в обороте','25-Депозит']].iterrows():
            if i[0]=='0044015101840600117836012':
                sxx.append(i[1]) 
            else:
                sxx.append(0) 
        axx['25-Депозит']=axx['25-Депозит']+sxx
        axx['74-Денежные средства в обороте']=axx['74-Денежные средства в обороте']-sxx
        
        azs=pd.DataFrame()
        for col  in axx:
            if col !='Сумма обеспечения' \
            and col !='MFO_schet' and\
            col !='Всего задолженность':
                azs[col]=axx[col]/axx['Сумма обеспечения']*\
                    axx['Всего задолженность']
            if col=='MFO_schet':
                azs[col]=axx[col]
              
        azs['61-Без обеспечения2']=sss1['Всего задолженность']
        azs['61-Без обеспечения']=azs['61-Без обеспечения2'].combine_first(azs['61-Без обеспечения'])
        sss1['Всего задолженность'].sum()
        del  azs['61-Без обеспечения2']
        
    if category_column==0:
        ax=crops.iloc[4:,:]
        sx=crops.iloc[3,:].astype(str)
        ax.columns=sx
        sx[6:]=sx[6:].str[:2]
        ax.columns=sx
        ax['MFO_schet']=ax['МФО'].astype(str) + ax["Кредит счёт"].astype(str)
        #ax.columns[7:]=ax
#        
#        new_cols=[]
#        for z in ax.columns[6:]:
#            new_cols.append(str(z)[:2])         
#        crops.iloc[1,6:]=[i for i  in new_cols]
#        ax.columns=crops.iloc[1,:]
        #ax['MFO_schet']=ax['МФО'].astype(str) + ax["Кредит счёт"].astype(str)
        axx=ax[['MFO_schet','Всего задолженность','Сумма обеспечения', '21',
               '22', '23',
               '24', '25',
               '26', '27',
               '29', '33', '35',
               '37', '38', 
               '39', '41',
               '42', '43',
               '44', '51',
               '61', '62', '71',
               '72', '73', '74',
               '75',
               '76']]
        axx=axx.fillna(0)
        sss1=axx[(axx['Сумма обеспечения']==0.0) | (axx['Сумма обеспечения']==0)]
        sxx=[]
        for k, i in axx[['MFO_schet','74','25']].iterrows():
            if i[0]=='0044015101840600117836012':
                sxx.append(i[1]) 
            else:
                sxx.append(0) 
            
        axx['25']=axx['25']+sxx
        axx['74']=axx['74']-sxx
        
        azs=pd.DataFrame()
        for col  in axx:
            if col !='Сумма обеспечения' \
            and col !='MFO_schet' and\
            col !='Всего задолженность':
                
                azs[col]=axx[col]/axx['Сумма обеспечения']*\
                    axx['Всего задолженность']
            if col=='MFO_schet':
                azs[col]=axx[col]
           
        azs['61-Без обеспечения2']=sss1['Всего задолженность']
        azs['61']=azs['61-Без обеспечения2'].combine_first(azs['61'])
        sss1['Всего задолженность'].sum()
        del  azs['61-Без обеспечения2']
        
    
    azz=azs.set_index('MFO_schet').join(new_dd1.set_index('MFO_schet'),how='inner')
    
    azz1=azz

    #%%credit_new(loz2,0,azz1['21-Недвижимость'])
    loz2=pd.DataFrame()
    az=pd.DataFrame()
    for i in azz1.iloc[:,:26]:
        loz2=pd.concat([azz1[i],azz1.iloc[:,26:]],axis=1)
        az[i]=builder_sum_credit_new(loz2,0,azz1[i])
    
    col_names=[]
    for i in az.columns:
        col_names.append(i[:2])
        
    az.columns=[int(i) for i in col_names]
    ##%%
     ###### Work on the decoration of the final table #####
     ###### the zaac az,  in line 104  
    a_=az/1000
    aa_oborud=a_[[26,24]].sum(axis=1)
    aa_garant=a_[[43,76]].sum(axis=1)
    aa_poruch=a_[[44,41]].sum(axis=1)
    aa_neobes=a_[[35,61]].sum(axis=1)
    aa_realest=a_[[75,21,22]].sum(axis=1)
    realest_fiz=pd.Series(np.where(aa_realest.index=='Физические лица',aa_realest,0))
    realest_fiz[75]=realest_fiz[63]
    realest_fiz.index=aa_realest.index
    realest_comm=pd.Series(np.where(aa_realest.index!='Физические лица',aa_realest,0))
    realest_comm[75]=realest_comm[64:75].sum()
    realest_comm.index=aa_realest.index 
    aaa_=pd.Series(a_[[33,37,39,73,74]].sum(axis=1))
    new_dd=azz1
    new_dd=new_dd.fillna(0)
    new_dd2=new_dd1[new_dd1['КодВал']=='000']
    new_dd3=new_dd1[new_dd1['КодВал']!='000']
    look_nacval=builder_sum_credit(new_dd2,0)/1000
    #look_fc=builder_sum_credit(new_dd3,0)/1000
    look_tot=builder_sum_credit(new_dd1,0)/1000
    look_fc=pd.Series(look_tot-look_nacval)
    #sred szveshanniy
    prom2=builder_sum_credit(new_dd2,1)/1000
    prom3=builder_sum_credit(new_dd3,1)/1000
    in_sum=prom2/look_nacval
    in_foreign=prom3/look_fc
    
    new_a=new_dd1[new_dd1['ОстатокВнебПроцентов']>0]
    new_b=new_dd1[new_dd1['ОстатокВнебПроцентов']==0]
    
    look_a=builder_sum_credit(new_a,0)/1000 
    look_b=builder_sum_credit(new_b,0)/1000
    
    
    if category_column==1:
        try:
            a_42_fc=builder_sum_credit_new(new_dd3,0,new_dd3['42-Гарантия Правительства'])/1000
        except KeyError:
            a_42_fc=pd.Series(np.zeros(76))
            a_42_fc.index=look_a.index
    if category_column==0:
        try:
            a_42_fc=builder_sum_credit_new(new_dd3,0,new_dd3['42'])/1000
        except KeyError:
            a_42_fc=pd.Series(np.zeros(76))
            a_42_fc.index=look_a.index        
    try:
        a_[30]=builder_sum_credit_new(new_dd3,0,new_dd3['30'])/1000
    except KeyError:
        a_[30]=pd.Series(np.zeros(76))
        a_[30].index=look_a.index
    ##preparing table to export 
    
    dataset2=pd.concat([look_tot,look_nacval,in_sum,look_fc,in_foreign,\
                                look_b,look_a,a_[25],a_[42],a_42_fc,\
                        a_[23],a_[27],aa_realest,realest_fiz,realest_comm,\
                        aa_oborud,a_[30],a_[29], aa_garant, aa_poruch,\
                        a_[51],aa_neobes,aaa_],axis=1)
       
        
    dataset2=dataset2.fillna(0)
    sz=list(dataset2.index)
    dataset2.index=range(0,len(dataset2))
    dataset2.loc[6]=dataset2.iloc[0:6,0:24].sum(axis=0)
    dataset2.loc[14]=dataset2.iloc[7:14,0:24].sum(axis=0)
    dataset2.loc[21]=dataset2.iloc[15:21,0:24].sum(axis=0)
    dataset2.loc[28]=dataset2.iloc[21:28,0:24].sum(axis=0)
    dataset2.loc[35]=dataset2.iloc[29:35,0:24].sum(axis=0)
    dataset2.loc[42]=dataset2.iloc[36:42,0:24].sum(axis=0)
    dataset2.loc[50]=dataset2.iloc[43:50,0:24].sum(axis=0)
    dataset2.loc[62]=dataset2.iloc[51:62,0:24].sum(axis=0)
    dataset2.loc[75]=dataset2.iloc[63:75,0:24].sum(axis=0)
    dataset2.index=sz
    col_names=['Сумма кредита','Сумма в нац. валюте',\
               'средне-взвешенные процентные ставки1' ,'Сумма в ин.валюте(экв.в сумах)',\
              'средне-взвешенные процентные ставки2','Начисляемые кредиты',\
              'Кредиты переведённые в статус ненаращивания процентов',\
              'Депозиты','Гарантированные Прав. РУ',\
              'Гарантированные Прав. РУ в ин.валюте(экв.в сумах)',\
              'Транспортные средства','Инвентарь','Недвижимость',\
              'жилая недвижимость','коммерческая недвижимость',\
              'Оборудование','Векселя (облигации)','Акции',\
              'Гарантия третьей стороны','Поручительства третьей стороны ',\
              'Страховой полис','Необеспеченные','Другое обеспечение']
    dataset2.columns=col_names
    dataset2['средне-взвешенные процентные ставки1']=in_sum
    dataset2['средне-взвешенные процентные ставки2']=in_foreign
    dataset2=dataset2.rename(columns={'средне-взвешенные процентные ставки1': \
                                      'средне-взвешенные процентные ставки',\
                                     'средне-взвешенные процентные ставки2':\
                                     'средне-взвешенные процентные ставки'})
    
    dataset2['Отрасль экономики']=dataset2.index
    dataset2.insert(0, 'Отрасль экономики', dataset2.pop('Отрасль экономики'))
    dataset2.index=range(0,len(dataset2))
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Промышленность'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Сельское хозяйство'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Транспорт и коммуникации'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Строительство'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Торговля и общественное питание'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Материально-техническое снабжение и сбыт'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Жилищно-коммунальные услуги'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Другие отрасли'
    dataset2.iloc[0,1:]= ''
    
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True) 
    dataset2.iloc[0,0]= 'Кредитные и лизинговые операции'
    dataset2.iloc[0,1:]= ''
    dataset2 = func3.insert_row(16, dataset2,dataset2.loc[7])
    dataset2 = func3.insert_row(25, dataset2,dataset2.loc[6])
    dataset2 = func3.insert_row(33, dataset2,dataset2.loc[5])
    dataset2 = func3.insert_row(41, dataset2,dataset2.loc[4])
    dataset2 = func3.insert_row(49, dataset2,dataset2.loc[3])
    dataset2 = func3.insert_row(57, dataset2,dataset2.loc[2])
    dataset2 = func3.insert_row(66, dataset2,dataset2.loc[1])
    dataset2 = func3.insert_row(79, dataset2,dataset2.loc[0])
    dataset2=dataset2.iloc[8:,:]
    
    es=list(header_3[1][4:])
    dataset2['Код']=es
    dataset2.insert(0,'Код', dataset2.pop('Код'))
    dataset2.loc[-1] = 0 # adding a row
    dataset2.index = dataset2.index + 1  # shifting index
    dataset2.sort_index(inplace=True)
    dataset2.iloc[0,1:]=[(i) for i in header_2.iloc[6,2:]]
    dataset2.index=range(len(dataset2))
    dataset2.iloc[33,2:]=dataset2.iloc[33,2:]-dataset2.iloc[25,2:]
    return dataset2



def selected_dataframe(df):
    import SQB_4_functions as func
    new_dd=df.iloc[5:,:] # run 4_main first!!!
    new_dd.columns=df.iloc[4,:]
    new_dd=new_dd.fillna(0)
    new_dd=new_dd[['MFO_schet','КодВал','БалансСчет','КодРег','ракам клас','СекторКлиентаДляОтчетов',\
                   'ОстатокВнебПроцентов','тип клиента','КодОбес','ВсегоЗадолженность',\
                   'ОстатокРезерв','средневзвеш']]
    new_dd['otr']=new_dd['СекторКлиентаДляОтчетов'].astype(str).str[2:]
    new_dd['region']=new_dd['КодРег'].apply(lambda x: func.put_names(x))
    return new_dd

def selected_dataframe_new(df):
    import SQB_4_functions as func
    new_dd=df.iloc[5:,:] # run 4_main first!!!
    new_dd.columns=df.iloc[4,:]
    new_dd=new_dd.fillna(0)
    new_dd=new_dd[['КодВал','КодРег','ракам клас','СекторКлиентаДляОтчетов',\
                   'ОстатокВнебПроцентов','тип клиента','КодОбес','ВсегоЗадолженность',\
                   'ОстатокРезерв','средневзвеш']]
    new_dd['otr']=new_dd['СекторКлиентаДляОтчетов'].astype(str).str[2:]
    new_dd['region']=new_dd['КодРег'].apply(lambda x: func.put_names(x))
    return new_dd
     
def main():
    builder_sum_credit()
    builder_special()
    selected_dataframe()
    selected_dataframe_new()
    builder_april_10()
if __name__=="__main__":
    main()
print("Completed")