import pandas as pd
import xlrd

df = pd.read_excel (io = 'partidos.xlsx', sheet_name='Sheet1')

#data = {'INDEX': [1,2]}

#df = pd.DataFrame(data, columns = ['LOCALIDAD', 'PROVINCIA', 'PARTIDO'])

#df.duplicated()

df = df.drop_duplicates()

df = df.sort_values('PARTIDO')

with pd.ExcelWriter('partidos1.xlsx') as writer:

     df.to_excel(writer, sheet_name = 'Sheet1', index = False)