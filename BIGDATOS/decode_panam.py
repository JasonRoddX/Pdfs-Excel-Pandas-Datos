import pandas
from unidecode import unidecode

excel = input('excel: ')

#abro mi excel de dominios
df  = pandas.read_excel(excel, sheet_name = 'Sheet1')
dfd = pandas.read_excel(excel, sheet_name = 'dominios')


for col in ['DOMINIO','PROPIETARIO_APELLIDO','PROPIETARIO_NOMBRE','CALLE','LOCALIDAD','PROVINCIA','PARTIDO','MARCA','MODELO'] :
    try:
        df[col] = df[col].astype(str).apply(unidecode)
    except:
        pass
    
#eliminar 'nan' de columnas
for col in ['DOMINIO','PROPIETARIO_APELLIDO','PROPIETARIO_NOMBRE','CALLE','LOCALIDAD','PROVINCIA','PARTIDO','MARCA','MODELO'] :
    df[col] = df[col].replace('nan','')

#eliminar filas con dominio duplicado

df = df.drop_duplicates(subset=['DOMINIO'], keep='first')
df = df.replace(';','', regex = True)
df = df.replace('=','', regex = True)
        
with pandas.ExcelWriter('unidecodeado.xlsx') as writer:  

    dfd.to_excel(writer, sheet_name = 'dominios', index = False)

    df.to_excel(writer, sheet_name = 'Sheet1', index = False)