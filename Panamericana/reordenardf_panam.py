import pandas
from unidecode import unidecode

excel = input('excel: ')

#abro mi excel de dominios
df  = pandas.read_excel(excel, sheet_name = 'Sheet1')
dfd = pandas.read_excel(excel, sheet_name = 'dominios')


df = df.sort_values(by=['DOMINIO'])

#eliminar filas con dominio duplicado

#df = df.drop_duplicates(subset=['DOMINIO'], keep='first')
        
with pandas.ExcelWriter('panamericana.xlsx') as writer:  

    dfd.to_excel(writer, sheet_name = 'dominios', index = False)

    df.to_excel(writer, sheet_name = 'Sheet1', index = False)