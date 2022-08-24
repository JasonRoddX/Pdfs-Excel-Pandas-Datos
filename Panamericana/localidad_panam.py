import pandas as pd

excel = input("Ingrese el nombre del archivo Excel: ")

#abro mi excel de dominios
df  = pd.read_excel(excel, sheet_name = 'Sheet1')
dfd = pd.read_excel(excel, sheet_name = 'dominios')

for i in range(len(df)):
    try:
        df.loc[i, 'LOCALIDAD'] = df.loc[i, 'LOCALIDAD'].split(')')[1]
    except:
        print(df.loc[i, 'LOCALIDAD'])
with pd.ExcelWriter('localidad-definida.xlsx') as writer:  

    dfd.to_excel(writer, sheet_name = 'dominios', index = False)

    df.to_excel(writer, sheet_name = 'Sheet1', index = False)