#``` python
import pandas as pd 

datos = pd.read_excel("partido-asignado0.xlsx")

df = pd.DataFrame(datos)

df['CALLE'] = df['NUMERO']

num=df['CALLE'].str.extract('(\d+(?:\.\d+)?)')

print(num)

#```