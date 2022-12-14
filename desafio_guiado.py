"""Requerimiento 1"""
print("Hola Mundo, esta es mi primera incursión en Python")


""" Requerimiento 2"""
name = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
hobbies = [input("Ingrese una actividad favorita: ") for _ in range(3)]
pet = input("¿Tiene mascotas?: ")


"""Requerimiento 3"""
print(name, edad, hobbies[1], pet)
type(name); type(edad); type(hobbies[1]); type(pet)
print(f"""
Me presento...
Mi nombre es {name} y tengo {edad} años.
Mis actividades favoritas son {", ".join(hobbies[0:2])} y {hobbies[2]}.
Si me preguntan '¿Tiene mascotas?', mi respuesta es {pet}.""")


"""Requerimiento 4"""
print('Estaba la pájara pinta sentada en el verde limón')
# falta una comilla simple al final de la frase

print('Mi nombre es', name ,'y tengo' , edad , 'años')
# faltan las comas "," que indiquen donde empieza y termina la variable a mostrar

import pandas as pd
import numpy as np
# la manera estándar es agregar las librerías al inicio del código

print("Ornitorrinco" + "45")
# no es posible sumar tipos de datos 'string' e 'int'. Le agregué la función print() para darle alguna utilidad a la línea de código




"""Requerimiento 5"""
#Pandas y numpy están importados en las líneas 28 y 29 del requerimiento anterior
df = pd.read_csv('flights.csv')

# Primeras y últimas 5 observaciones
print(df.head(5))
print(df.tail(5))

year = df['year']
# Método describe() para columna year
print(year.describe())

month = df['month']
# Método value.counts() para meses y años
print(month.value_counts())
print(year.value_counts())


# Guardado en variables de primeras y últimas 15 observaciones para meses y años
primeros_15_months = month[:15]
ultimos_15_months = month[129:]

primeros_15_year = year[:15]
ultimos_15_year = year[129:]


# Media, mediana y desviación estándar para la cantidad de pasajeros
passengers = df['passengers']
print(np.mean(passengers))
print(np.median(passengers))
print(np.std(passengers))

print(np.mean(passengers[:15]))
print(np.mean(passengers[129:]))

print(np.median(passengers[:15]))
print(np.median(passengers[129:]))

print(np.std(passengers[:15]))
print(np.std(passengers[129:]))