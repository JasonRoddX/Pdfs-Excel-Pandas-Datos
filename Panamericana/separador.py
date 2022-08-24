import pandas as pd
import numpy as np
import re

s = pd.Series([1.1, 2.3])
a = np.array(s)
excel = input ('Ingrese nombre del excel: ')
df = pd.read_excel(excel, sheet_name = 'Sheet1')
dfd = pd.read_excel(excel, sheet_name = 'dominios')
def ajustar_nombres(PROPIETARIO_APELLIDO, PROPIETARIO_NOMBRE): 
    s = PROPIETARIO_APELLIDO.split(", ")
    if len(s) > 1:
        return f"{PROPIETARIO_NOMBRE} {s[1]}"
    else:
        return PROPIETARIO_NOMBRE
df["PROPIETARIO_NOMBRE"] = df.apply(lambda x: ajustar_nombres(x.PROPIETARIO_APELLIDO, x.PROPIETARIO_NOMBRE), axis =1)
df["PROPIETARIO_APELLIDO"] = df["PROPIETARIO_APELLIDO"].apply(lambda x: x.split(",")[0])
with pd.ExcelWriter('apellido-separado.xlsx') as writer:  
     dfd.to_excel(writer, sheet_name = 'dominios', index = False)
     df.to_excel(writer, sheet_name = 'Sheet1', index = False)
print ('¡NOMBRES SEPARADOS!')

#By Rodrigo ;D