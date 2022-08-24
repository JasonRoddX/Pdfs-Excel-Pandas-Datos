import pandas as pd

excel = input('excel: ')

df = pd.read_excel(excel)

df=df.drop_duplicates( subset = ['DOMINIO'], keep = "last")

df.to_excel('duplicados-chau.xlsx', index=False)

print(df)