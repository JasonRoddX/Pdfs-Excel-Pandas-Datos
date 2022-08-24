import pandas as pd
import numpy as np
import pathlib

df = pd.read_excel ( io = pathlib.Path(__file__).parent.resolve() / 'bigdatos.xlsx', sheet_name = 'dominios', usecols = ['DOMINIO1', 'DOMINIO2'])

s1 = df ['DOMINIO1']

s2 = df ['DOMINIO2']

res = s1 [~s1.isin(s2)]

res.to_csv (pathlib.Path(__file__).parent.resolve() / 'bigdatos-CRACKEADO.xlsx',

    index = False,
    sep = "@",
    encoding = "utf-8-sig",)

    # by Rodrigo ;D 