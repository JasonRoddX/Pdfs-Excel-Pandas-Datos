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

    if calle_list[-1].isnumeric() and df.loc[i,'NUMERO'] == 0:
        df.loc[i,'NUMERO'] = int(calle_list[-1])
        calle_list.pop(-1)  
        df.loc[i,'CALLE'] = ' '.join(calle_list)

    elif df.loc[i,'NUMERO'] == 0:
        df.loc[i,'NUMERO'] = rd.randint(100,200)
    z
with pd.ExcelWriter('revisar-SUGIT-camila.xlsx') as writer:  

    dfd.to_excel(writer, sheet_name = 'dominios', index = False)

    df.to_excel(writer, sheet_name = 'Sheet1', index = False)