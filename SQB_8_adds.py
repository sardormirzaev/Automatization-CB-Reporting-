"""
Created on Thu Apr 22 12:55:09 2021

@author: Sardor Mirzaev
"""

'Asset Quality'


def builder_2_table(dataframe,helper,helper0):
    import numpy as np
    import pandas as pd 
    import SQB_6_functions as func3
    import SQB_8_functions as func8
    helper1=helper0.iloc[:,2]
    helper1.index=helper0.iloc[:,1]
    helper11=helper0.iloc[:,2]
    helper11.index=helper0.iloc[:,0]
    dataset=dataframe
    tab=dataset.iloc[5:,:]
    tab.columns=dataset.iloc[4,:]
    
    #%%
    tal_zadol=dict()
    for iz in tab['Баланс х/р'].unique():
        #axc[iz]=tab[tab['Баланс х/р']==str(iz)]
        axx2=tab[tab['Баланс х/р']==str(iz)]
        tal_zadol[iz]=axx2.ВсегоЗадолженность.sum()
    
    
    tal_reserv=dict()
    for iz in tab['Баланс х/р'].unique():
        #axc[iz]=tab[tab['Баланс х/р']==str(iz)]
        axx2=tab[tab['Баланс х/р']==str(iz)]
        tal_reserv[iz]=axx2.ОстатокРезерв.sum()
    
    

    axc=pd.DataFrame()
    axc=pd.DataFrame() 
    for iz in tab['Баланс х/р'].unique():
        axx2=tab[tab['Баланс х/р']==str(iz)]
        #toal[i]=axx2.ВсегоЗадолженность.sum()
        axc[iz]=axx2.groupby(['ракам клас']).ВсегоЗадолженность.sum()
        
    po_zadol=axc.T
    po_zadol['0']=tal_zadol.values()
    
    axc=pd.DataFrame()
    axc=pd.DataFrame() 
    for iz in tab['Баланс х/р'].unique():
        axx2=tab[tab['Баланс х/р']==str(iz)]
        #toal[i]=axx2.ВсегоЗадолженность.sum()
        axc[iz]=axx2.groupby(['ракам клас']).ОстатокРезерв.sum()
        
    po_reserv=axc.T
    po_reserv['0']=tal_reserv.values()
    #%%
    zad=pd.DataFrame(columns=range(0,6),index=helper[0].astype(str))           
    
    ### po zadol
    azs=po_zadol.combine_first(zad)            
    prod=azs.iloc[:,6:]
    prod['Schet']=prod.index
    
    #### po reserv
    
    azs_reserv=po_reserv.combine_first(zad)
    resv=azs_reserv.iloc[:,6:]
    resv['Schett']=resv.index
    resv['Schet2']=resv.Schett.str[:3]+'99'
    
    #%%%
    ##Balans 
    pz=dict()
    for i in prod.index:
        for  z in helper1.index:
            if z==i:
                pz[z]=helper1[i]
    ser1=pd.Series(pz)
    ser1.index=ser1.index.str[:3]+'00'
    prod['balans_pros']=ser1.astype(float)
    prod.index=func8.rows[6:]
    prod.loc['ВСЕГО']=prod.iloc[:,:6].sum(axis=0)
    pl=dict()
    for i in resv.Schet2:
        for  z in helper11.index:
            if z==i:
                pl[z]=helper11[i]
    ser=pd.Series(pl)
    ser.index=ser.index.str[:3]+'00'
    
    resv['balans_resv']=ser.astype(float)
    resv.index=func8.rows[6:]
    resv.loc['ВСЕГО']=resv.iloc[:,:6].sum(axis=0)
    #%%
    als=pd.concat([prod,resv],axis=1)
    als.loc['ВСЕГО']=als.iloc[0:32,:6].sum(axis=0)
    als['Состав активов*']=als.index
    als.insert(0, 'Состав активов*', als.pop('Состав активов*'))
    als.index=range(7,len(als)+7)
    als['ind']=als.index
    als.insert(0, 'ind', als.pop('ind'))
    als.insert(0, 'balans_pros', als.pop('balans_pros'))
    als.insert(0, 'Schet', als.pop('Schet'))
    als['Blank']=np.nan
    als.insert(10, 'Blank', als.pop('Blank'))
    als = func3.insert_row(0, als,als.loc[39])
    als=als.iloc[:-1,:]
    
    return als
    
def main():
   builder_2_table()
if __name__=="__main__":
    main()
print("Completed")















