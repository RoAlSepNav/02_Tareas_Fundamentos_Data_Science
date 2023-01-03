import pandas as pd
import numpy as np

"""Requerimiento 1"""   ;print("""Requerimiento 1:""")
df = pd.read_csv('worldcup2014.csv')
print(df.head(5))       ;print("")


"""Requerimiento 2"""   ;print("""Requerimiento 2:""")
print(df['continent'].value_counts())
print("")

print("¿Cuál es el continente con una mayor presencia en la muestra?")
print("R: El continente con mayor presencia en la muestra es Europa.\n")

print(df['continent'].value_counts('%'))
print("")

print("¿Cuál es la probabilidad de elegir un equipo asiático al azar?")
print("R: La probabilidad de elegir un equipo asiático al azar es 12.5%\n")

print("¿Cuál es la probabilidad de elegir un equipo africano al azar?")
print("R: La probabilidad de elegir un equipo africano al azar es 15.6%\n")



"""Requerimiento 3"""   ;print("""Requerimiento 3:""")
europe_df = df[df['continent'] == 'europe']
southamerica_df = df[df['continent'] == 'southamerica']
africa_df = df[df['continent'] == 'africa']
northamerica_df = df[df['continent'] == 'northamerica']
asia_df = df[df['continent'] == 'asia']

print(europe_df,"\n",
southamerica_df,"\n",
africa_df,"\n",
northamerica_df,"\n",
asia_df)
print("")



"""Requerimiento 4"""   ;print("""Requerimiento 4:""")

def pr_clasif_next_round(df):
    probabilidad = df['clasificado'].value_counts(normalize=True)
    return probabilidad

print("europe")
print(pr_clasif_next_round(europe_df))
print("\nsouthamerica")
print(pr_clasif_next_round(southamerica_df))
print("\nafrica")
print(pr_clasif_next_round(africa_df))
print("\nnorthamerica")
print(pr_clasif_next_round(northamerica_df))
print("\nasia")
print(pr_clasif_next_round(asia_df))


print("\n¿Cuál es la probabilidad de que un país asiático pase a la siguiente ronda?")
print(f"R: La probabilidad de que un país asiático pase a la siguiente ronda es 0 %.\n")

print("¿Cuáles son los dos continentes con la mayor probabilidad de clasificar?")
print("R: Los contienentes con la mayor probabilidad de clasificar son: Sudamérica y Norteamérica.\n")

print("¿Cuál es la probabilidad de que un país europeo no clasifique?")
print(f"R: La probabilidad de que un país europeo no clasifique es: 53.84%.\n\n")



"""Requerimiento 5"""   ;print("""Requerimiento 5:""")

df['ha_ganado'] = np.where(df['juegos_ganados'] >= 1, 1, 0)
print(df.groupby('continent')['ha_ganado'].value_counts(normalize=True))
print("")
print("¿Qué continente tiene la mayor probabilidad de tener países con al menos 1 victoria?")
print(f"R: El continente que tiene la mayor probabilidad de tener países con al menos 1 victoria es Sudamérica.\n")

print("¿Qué continente tiene un nivel similar entre países que tienen o no tienen victorias?")
print("R: El continente que tiene un nivel similar entre países que tienen o no tienen victorias es África.\n")


# Reformulación de código para juegos perdidos (1), juegos sin perder(0)
df['ha_perdido'] = np.where(df['juegos_perdidos'] >= 1, 1, 0)
print(df.groupby('continent')['ha_perdido'].value_counts(normalize=True))
print("")


print("Los continentes con mayor probabilidad de tener países sin juegos perdidos son Norteamérica y Sudamérica con 50% cada uno.")

# cd g56/02_Fundamentos_Data_Science/S2
