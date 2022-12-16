import numpy as np
import pandas as pd

"""Requerimiento 1"""
array1 = np.linspace(1, 50)
array2 = np.linspace(50, 150, 101)



"""Requerimiento 2"""
paridad = [f"{num} es par" if num % 2 == 0 else f"{num} es impar" for num in array1]
for elem in paridad:
    print(elem)


"""Requerimiento 3"""
# Contadores para cada condición
div_por_2_o_3 = 0
div_por_2_y_3 = 0
div_por_3_pero_no_2 = 0
no_div_por_2_ni_3 = 0

for elem in array2:
    # el número es divisible por 2 o 3
    if (elem % 2 == 0) or (elem % 3 == 0):
        div_por_2_o_3 += 1
    # el número es divisible por 2 y 3    
    if (elem % 2 == 0) and (elem % 3 == 0):    
        div_por_2_y_3 += 1
    # el número es divisible por 3 pero no por 2
    if (elem % 3 == 0) and (elem % 2 != 0):
        div_por_3_pero_no_2 += 1
    # el número no es divisible por 2 ni 3    
    if (elem % 2 != 0) and (elem % 3 != 0): 
        no_div_por_2_ni_3 += 1

print(f"Número de elementos divisibles por 2 o 3: {div_por_2_o_3}")
print(f"Número de elementos divisibles por 2 y 3: {div_por_2_y_3}")
print(f"Número de elementos divisibles por 3 pero no 2: {div_por_3_pero_no_2}")
print(f"Número de elementos no divisibles por 2 y 3: {no_div_por_2_ni_3}")



"""Requerimiento 5"""
df = pd.read_csv('flights.csv')

# Media de passengers
mean_passengers = df['passengers'].mean()
print(f"\nLa media de passengers es: {mean_passengers}\n")

# Nueva columna 'underperforming'
df['underperforming'] = 0

# Asignamos un 1 a la columna df.underperforming según las condiciones indicadas
for index, obs in df['passengers'].items():
    if obs < mean_passengers:
        df.at[index, 'underperforming'] = 1



"""Requerimiento 6"""

# Media y desviación estándar de passengers
mean_passengers = df['passengers'].mean() # esto se calculó anteriormente
std_passengers =  df['passengers'].std()

print(f"\nLa mediana de passengers es: {mean_passengers}")
print(f"La desviación estándar de passengers es: {std_passengers}\n")


# Nueva columna 'outlier'
df['outlier'] = 0

# Asignamos un 1 a la columna df.outlier según las condiciones indicadas
outlier_count = 0 
for index, obs in df['passengers'].items():
    if (obs < mean_passengers-std_passengers) | (obs > mean_passengers+std_passengers):
        outlier_count += 1
        df.at[index, 'outlier'] = 1

print(df)
print(f"La cantidad de observaciones clasificadas como casos extremos es: {outlier_count}")
