import pandas as pd
import random as rd
import re

excel = input("Ingrese el nombre del archivo Excel: ")

df  = pd.read_excel(excel, sheet_name = 'Sheet1')
dfd = pd.read_excel(excel, sheet_name = 'dominios')

df['NUMERO'] = df['NUMERO'].fillna(0)

for i in range(len(df)): 
    
    calle = str(df.loc[i,'CALLE'])
    
    calle_list = calle.split(' ')    
    
    if df.loc[i,'NUMERO'] == 0:
        df.loc[i,'NUMERO'] = rd.randint(100,200)
    
    if 'S/N' in calle_list:
        calle_list.remove('S/N')
        df.loc[i,'CALLE'] = ' '.join(calle_list)
        
with pd.ExcelWriter('numero-asignado.xlsx') as writer:  

    dfd.to_excel(writer, sheet_name = 'dominios', index = False)

    df.to_excel(writer, sheet_name = 'Sheet1', index = False)