# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:50:16 2019

@author: bk
"""

import logging, pandas as pd
from openpyxl import load_workbook

def _write_frame_to_new_sheet(path_to_file=None, sheet_name='sheet', data_frame=None):
    book = None
    try:
        book = load_workbook(path_to_file)
    except Exception:
        logging.debug('Creating new workbook at %s', path_to_file)
    with pd.ExcelWriter(path_to_file, engine='openpyxl') as writer:
        if book is not None:
            writer.book = book
        data_frame.to_excel(writer, sheet_name, index=False)

df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

dfObj = pd.DataFrame( columns = ['Field Name' , 'DIff Count', 'Diff %' ])

#print(df1)

#print(df2)

#new = pd.merge(df1,df2,on=['APPL_NBR','FIELD1','FIELD2'], how='inner' )

#print(new)

#df3 = df2[~df2['APPL_NBR'].isin(new['APPL_NBR'])]

col = list(df1.columns.values)

length = len(col) 
i = 2
#while i < length: 
#    print(col[i]) 
#    i += 1 

#df = (df1.merge(df2, on=['APPL_NBR','FIELD2'], how='outer', indicator=True, suffixes=('_','')).query("_merge == 'right_only'")[df2.columns])
while i < length:
    df = (df1.merge(df2, on=['APPL_NBR',col[i]], how='outer', indicator=True, suffixes=('_','')).query("_merge == 'right_only'")[df2.columns])
    dfObj = dfObj.append({'Field Name' : col[i] , 'DIff Count' : df.shape[0], 'Diff %' : df.shape[0]/df1.shape[0] } , ignore_index=True)
    # print (df[['APPL_NBR',col[i]]])
    df_xls = df[['APPL_NBR',col[i]]]
    #print(df_xls)
    _write_frame_to_new_sheet('output.xlsx',col[i],df_xls)
    
    i += 1 
    
print(dfObj)    
#print (df[['APPL_NBR',col[2]]])