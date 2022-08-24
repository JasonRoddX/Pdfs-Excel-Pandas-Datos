from curses.ascii import isdigit
import pandas as pd
import numpy as np
import re
import random as rd

df = pd.read_excel('panamhoy.xlsx', sheet_name = 'Sheet1')

#df = df['CALLE']
#df = df['NUMERO']

for i in ['º', '°', 'S/N']:
    df['CALLE'] = df['CALLE'].str.replace(i, '', regex = True)


df['NUMERO'] = df['CALLE'].str.extract(r'(\d+)$', expand = False)
if ['CALLE'].isnull().any().any():
    df['NUMERO'] = df['CALLE'].str.extract(r'(\d+)$', expand = False)

# df['CALLE'] = df['CALLE'].str.replace(r'(\d+)$', '', regex = True)

# df['NUMERO'] = df['CALLE'].str.extract(r'(\d{3})$', expand = False)





# lista_calle.pop()

# for i in len(df):
#     if isdigit(calle_list[-1]):
#         calle_list.pop()

# lista_calle = df.loc[i, 'CALLE'].str.split('')
# if lista_calle.str.contains('\d+').any():
#     df['CALLE'] = df['CALLE'].str.replace('\d+', '', regex = True)

df.to_excel('NUMEROSkm.xlsx', sheet_name = 'Sheet1')