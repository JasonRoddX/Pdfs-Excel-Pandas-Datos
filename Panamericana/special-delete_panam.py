import pandas as pd
import re

excel=input('Nombre del Excel: ')

df = pd.read_excel(excel, sheet_name = 'Sheet1')

dfd = pd.read_excel(excel, sheet_name = 'dominios')


for i in ['CIUDAD AUTÓNOMA DE BS. AS.']:
    df['PROVINCIA'] = df['PROVINCIA'].str.replace(i, 'CAPITAL FEDERAL', regex = True)

for i in ['CIUDAD AUTONOMA DE BS. AS.']:
    df['PARTIDO'] = df['PARTIDO'].str.replace(i, 'C.A.B.A.', regex = True)

for i in ['C.A.B.A.']:
    df['LOCALIDAD'] = df['LOCALIDAD'].str.replace(i, 'CIUDAD AUTONOMA BUENOS AIRES', regex = True)

for i in ['S/NRO', 'S/N','00000', 'S/C ', 'SN', 'S/N', 's/n']: 
    df['CALLE'] = df['CALLE'].str.replace(i, '', regex = True)

for i in ['S/CALLE']:
    df['CALLE'] = df['CALLE'].str.replace(i, 'CALLE', regex = True)

df = df.drop_duplicates( subset = ['DOMINIO'], keep = "last")

# df['NUMERO'] = df['CALLE'].apply(lambda x :int(x.split()[-1]) if x.split()[-1].isdigit() else '')

# df['CALLE'] = df['CALLE'].apply(lambda x: ' '.join(x.split(' ')[:-1]) if x.split()[-1].isdigit() else x)

with pd.ExcelWriter('special-delete-asignado.xlsx') as writer:  

    dfd.to_excel(writer, sheet_name = 'dominios', index = False)

    df.to_excel(writer, sheet_name = 'Sheet1', index = False)

print ('¡SPECIAL DELETE HAS BEEN INJECTED!')

#By Rodrigo ;D