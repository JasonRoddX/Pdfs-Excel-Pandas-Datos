import pandas as pd
import numpy as np
import re

excel = input('Ingrese el nombre del archivo Excel: ')

df = pd.read_excel(excel, sheet_name = 'Sheet1')
#dfd = pd.read_excel(excel, sheet_name = 'dominios')

# for i in ['S/N', 'S/N║', 'SIN NOMBRE','S/ CALLE', 'S/CALLE ', 'S/NO', 'S/No','S/No.', '-', 'S/NRO', 'S/Ndeg', 'SN', 'S/C', 'S/C ', 'SIN CALLE', 'SIN INFORMAR','//', 'o', 'PB', 'deg', 'Deg', '00000', 'S/Ndeg|']:
#     df['PISO'] = df['PISO'].str.replace(i, '', regex = True)

# for i in ['CAPITAL FEDERAL']:
#   df['PARTIDO'] = df['PARTIDO'].str.replace(i, 'C.A.B.A.', regex = True)

# for i in ['CAPITAL FEDERAL']:
#  df['LOCALIDAD'] = df['LOCALIDAD'].str.replace(i, 'CIUDAD AUTONOMA BUENOS AIRES', regex = True)

#df.loc[df['CP'] == 1661, 'PARTIDO'] = 'SAN MIGUEL'

#for i in ['C.A.B.A.', 'C.AUTONOMA DE BS.AS', 'CABA', 'CAPITAL FEDERAL', 'CAPITAL FEDERAL (CAPITA-C)', 'CEN POSTAL CONS', 'CIUDA DE BUENOS AIRES', 'CIUDAD AUTËNOMA DE BUENOS AIRES', 'CIUDAD AUTONOMA BUEN', 'CIUDAD AUTONOMA BUENOS AI']:
    #df['LOCALIDAD'] = df['LOCALIDAD'].str.replace(i, 'CIUDAD AUTONOMA BUENOS AIRES', regex = True)
    
# if df['LOCALIDAD'] == 'CIUDAD AUTONOMA BUENOS AIRES':
#     df['PROVINCIA'] == 'CAPITAL FEDERAL'

#for i in ['CIUDAD AUTONOMA']:
   #  df['PROVINCIA'] = df['PROVINCIA'].str.replace(i, 'CAPITAL FEDERAL', regex = True)

#numeros = (df['NUMERO'] == df['PISO']) & (df['PISO'].astype(int) > 99)
#df.loc[numeros, 'PISO'] = ''

# for i in len(df):
#     df.loc[i,'CAP'] = df.loc[i, 'PROVINCIA']
#     df['PROVINCIA'] = df['PROVINCIA'].str.replace(i, 'CAPITAL FEDERAL', regex = True)
    
#for i in ['0']:
  #  df['COLUMNAS'] = df['COLUMNAS'].str.replace(i, '')

#def repl_func(match):
  #if match == True:
    #return " "

df['CALLE'] = df['CALLE'].str.replace(r'\d\d\d-', "", regex = True)

#string = "000-asdada"

#new_string = re.sub(r'\d\d\d-', "", string)

#df['CALLE'] 

#print(new_string)

with pd.ExcelWriter('string-asingado.xlsx') as writer:

  df.to_excel(writer, sheet_name = 'Sheet1', index = False)

#Leer
#with pd.ExcelWriter('special-delete-asignado.xlsx') as writer:  

 #   dfd.to_excel(writer, sheet_name = 'dominios', index = False)

  #  df.to_excel(writer, sheet_name = 'Sheet1', index = False)

print ('¡SPECIAL DELETE HAS BEEN INJECTED!')

#By Rodrigo ;D