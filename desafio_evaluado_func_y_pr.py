import pandas as pd
import numpy as np

"""Desafío 1: Generación de funciones"""   ;print("""Desafío 1: Generación de funciones:""")

def media(x):
    """
    Calcula la media de un vector.
    
    Parameters
    ----------
    x : lista
        Vector del cual se quiere calcular la media.
        
    Returns
    -------
    float
        Media del vector.
    """
    # Calculamos la suma de los elementos del vector
    suma = 0
    for elemento in x:
        suma += elemento
        
    # Calculamos la media del vector
    media = suma / len(x)
    
    return media

def varianza(x):
    """
    Calcula la varianza de un vector.
    
    Parameters
    ----------
    x : lista
        Vector del cual se quiere calcular la varianza.
        
    Returns
    -------
    float
        Varianza del vector.
    """
    # Calculamos la media del vector
    media_vector = media(x)
    
    # Calculamos la varianza utilizando la media del vector
    varianza = 0
    for elemento in x:
        varianza += (elemento - media_vector)**2
    varianza = varianza / len(x)
    
    return varianza



df = pd.read_csv('worldcup2014.csv')

# Media goles_favor, goles_contra y puntos.
media_goles_favor = media(df['goles_favor'])
media_goles_contra = media(df['goles_contra'])
media_puntos = media(df['puntos'])

print(f"La media de 'goles_favor' es {round(media_goles_favor,2)}")
print(f"La media de 'goles_contra' es {round(media_goles_contra,2)}")
print(f"La media de 'puntos' es {round(media_puntos,2)}\n")


# Varianza goles_favor, goles_contra y puntos.
varianza_goles_favor = varianza(df['goles_favor'])
varianza_goles_contra = varianza(df['goles_contra'])
varianza_puntos = varianza(df['puntos'])

print(f"La varianza de 'goles_favor' es {round(varianza_goles_favor,2)}")
print(f"La varianza de 'goles_contra' es {round(varianza_goles_contra,2)}")
print(f"La varianza de 'puntos' es {round(varianza_puntos,2)}\n")



"""Desafío 2:"""   ;print("""\nDesafío 2:""")

# Media por continente
print("Media por continente:")
media_por_continente = df.groupby(by ='continent').agg(media)

print(f"La media de 'goles_favor' por continente es:\n{round(media_por_continente['goles_favor'],2)}\n")
print(f"La media de 'goles_contra' por continente es:\n{round(media_por_continente['goles_contra'],2)}\n")
print(f"La media de 'puntos' por continente es:\n{round(media_por_continente['puntos'],2)}\n\n")


# Varianza por continente
print("Varianza por continente:")
varianza_por_continente = df.groupby(by ='continent').agg(varianza)

print(f"La varianza de 'goles_favor' por continente es:\n{round(varianza_por_continente['goles_favor'],2)}\n")
print(f"La varianza de 'goles_contra' por continente es:\n{round(varianza_por_continente['goles_contra'],2)}\n")
print(f"La varianza de 'puntos' por continente es:\n{round(varianza_por_continente['puntos'],2)}\n\n")


# Desviación estándar por continente
print("Desviación estándar por continente:")
std_por_continente = df.groupby(by ='continent').agg(np.std)

print(f"La desviación estándar de 'goles_favor' por continente es:\n{round(std_por_continente['goles_favor'],2)}\n")
print(f"La desviación estándar de 'goles_contra' por continente es:\n{round(std_por_continente['goles_contra'],2)}\n")
print(f"La desviación estándar de 'puntos' por continente es:\n{round(std_por_continente['puntos'],2)}\n\n")


print("Preguntas:")
print("¿En qué continente se observa una mayor cantidad de goles a favor?")
print("R: Se observa una mayor cantidad de goles a favor en Sudamérica.\n")

print("¿En qué continente se observa una mayor cantidad de goles en contra?")
print("R: Se observa una mayor cantidad de goles en contra en Asia.\n")

print("¿En qué continente se observa una mayor cantidad de puntos en promedio?")
print("R: Se observa una mayor cantidad de puntos en promedio en Sudamérica.\n")




"""Desafío 3: Simulaciones"""   ;print("""\nDesafío 3: Simulaciones""")

# Función
def generate_pet(n):
    opciones = ['perro', 'gato']
    return np.random.choice(opciones, size = n)

# 20 muestras mediante la función generate_pet
muestras_20 = generate_pet(20)

# Probabilidad de elegir un perro al azar y probabilidad de elegir un gato al azar
print("¿Cuál es la probabilidad de elegir un perro al azar? ¿Y un gato?")
print("Las probabilidades son las que aparecen en la tabla siguiente:\n")

prob_animal = pd.DataFrame(muestras_20).value_counts(normalize=True)
print("Resultados random:\n", muestras_20)
print(prob_animal,"\n")

# np.random.seed(2) al inicio del chunk
def generate_pet_seed(n):
    np.random.seed(2)
    opciones = ['perro', 'gato']
    return np.random.choice(opciones, size = n)

muestras_20_seed = generate_pet_seed(20)
print("Resultados pseudo-random:\n", muestras_20_seed,"\n")

print("¿Qué diferencia hay cuando se ejecuta la función varias veces luego de fijar la semilla?")
print("""R: Al ejecutar varias veces la función, esta entrega el mismo resultado. Esto se 
debe a que en realidad np.random genera resultados psudo-random. Si en vez  de 2 
se utiliza 3 como semilla esta generaria otro resultado pero sin importar el numero
de repeticiones el resultado seria el mismo para 3.\n""")



"""Desafío 4: Función simuladora"""   ;print("""\nDesafío 4: Función simuladora""")

def simulate_pets_prob(n):
    np.random.seed(1)
    young_pet = generate_pet(n)
    old_pet = generate_pet(n)
    
    count_case_1 = 0
    count_case_2 = 0
    count_case_3 = 0

    for i in range(n):    
        # Caso 1
        count_case_1 += ('perro' in young_pet[i] or 'perro' in old_pet[i])
        pr_case_1 = round((count_case_1/n),2)

        # Caso 2
        count_case_2 += ('perro' in old_pet[i])
        pr_case_2 = round((count_case_2/n),2)

        # Caso 3
        count_case_3 += ('perro' in young_pet[i] and 'perro' in old_pet[i])
        pr_case_3 = round((count_case_3/n),2)      
    
    return pr_case_1, pr_case_2, pr_case_3

print(simulate_pets_prob(10))

print("De los tres escenarios, ¿Cuál es el menos probable? ¿Cuál es el más probable? ¿Por qué?")
print("""R: para n = 10, el caso 3 es el menos probable, el caso 1 es el más probable. 
Para este caso la cantidad de ocurrencias van de mayor a menor para el caso 1, 2 y 3""")

