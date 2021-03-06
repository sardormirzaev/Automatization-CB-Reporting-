# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:38:41 2021

@author: Sardor Mirzaev
"""
rows=['Кассовая наличность и другие платежные документы',
        'К получению из ЦБРУ',
        'К получению из других банков',
        'Ценные бумаги для купли и продажи',
        'Инвестиции в ценные бумаги, имеющиеся в наличии для продажи',
        'Драгоценные металлы, камни и монеты для купли и продажи',
        'Купленные дебиторские задолженности - Факторинг',
        'Купленные векселя',
        'Обязательства клиентов по траттам под аккредитив и/или трастовые документы',
        'Обязательства клиентов по непогашенным акцептам банка',
        'Купленные по сделкам РЕПО ценные бумаги',
        'Краткосрочные кредиты, предоставленные ЦБРУ',
        'Краткосрочные кредиты, предоставленные другим банкам',
        'Краткосрочные кредиты, предоставленные правительству',
        'Краткосрочные кредиты, предоставленные бюджетным организациям',
        'Краткосрочные кредиты, предоставленные физическим лицам',
        'Краткосрочные кредиты, предоставленные индивидуальным предпринимателям',
        'Краткосрочные кредиты, предоставленные государственным предприятиям, организациям и учреждениям',
        'Краткосрочные кредиты, предоставленные при содействии Государственного фонда поддержки развития предпринимательской деятельности',
        'Краткосрочные кредиты, предоставленные предприятиям с участием иностранного капитала',
        'Краткосрочные кредиты, предоставленные негосударственным некоммерческим организациям',
        'Краткосрочные кредиты, предоставленные частным предприятиям, хозяйственным товариществам и обществам',
        'Краткосрочные кредиты, предоставленные небанковским финансовым институтам',
        'Краткосрочные кредиты, предоставленные для производства сельскохозяйственной продукции, закупаемой для государственных нужд',
        'Долгосрочные кредиты, предоставленные для производства сельскохозяйственной продукции, закупаемой для государственных нужд',
        'Долгосрочные кредиты, предоставленные при содействии Государственного фонда поддержки развития предпринимательской деятельности',
        'Долгосрочные кредиты, предоставленные другим банкам',
        'Долгосрочные кредиты, предоставленные правительству ',
        'Долгосрочные кредиты, предоставленные бюджетным организациям',
        'Долгосрочные кредиты, предоставленные физическим лицам',
        'Долгосрочные кредиты, предоставленные индивидуальным предпринимателям',
        'Долгосрочные кредиты, предоставленные государственным предприятиям, организациям и учреждениям',
        'Долгосрочные кредиты, предоставленные негосударственным некоммерческим организациям',
        'Долгосрочные кредиты, предоставленные предприятиям с участием иностранного капитала',
        'Долгосрочные кредиты, предоставленные небанковским финансовым институтам',
        'Долгосрочные кредиты, предоставленные частным предприятиям, хозяйственным товариществам и обществам',
        'Лизинг (Финансовая аренда)',
        'Кредиты и лизинг, находящиеся в процессе судебного разбирательства']


def two_to_excel(dataframe,name):
    import pandas as pd
    writer = pd.ExcelWriter(name, engine='xlsxwriter')
    #dataframe=dataframe.fillna(0)
    #dataframe.replace(0,'0')
    dataframe.to_excel(writer, index=False, header=False,startcol=1,\
                    startrow=3, sheet_name='Sheet1')
    
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    #Add a header format.
    header_format = workbook.add_format({
        'bold': True,
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
            'bold': 'True',
            'font_size': 8})                               
    worksheet.set_column('E:E', 30, cellFormat2)
    worksheet.set_column('C:C', 18, cellFormat)
    worksheet.set_column('F:K', 18, cellFormat)
    worksheet.set_column('M:R', 18, cellFormat)
    worksheet.set_column('U:U', 18, cellFormat)
    workbook.close() 
    print('---- Table has been saved with .xlsx format ----' )

def main():
   rows
   two_to_excel()
if __name__=="__main__":
    main()
print("Completed")
#%%