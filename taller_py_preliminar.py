import numpy as np

def generate_pet(n):
    opciones = ['perro', 'gato']
    return np.random.choice(opciones, size = n)


def simulate_pets_prob(n):
    np.random.seed(1)
    young_pet = generate_pet(n)
    old_pet = generate_pet(n)
    
    count_case_1 = 0
    count_case_2 = 0
    count_case_3 = 0



    #young_pet =['gato' 'gato' 'perro' 'perro' 'gato' 'gato' 'gato' 'gato' 'gato' 'perro']
   #old_pet = ['perro' 'gato' 'perro' 'gato' 'gato' 'perro' 'perro' 'gato' 'perro' 'perro']
    for i in range(n):    

        # Contamos las ocurrencias de cada caso
        if young_pet[i] == 'perro' or old_pet[i] == 'perro':
            count_case_1 += 1
        prob_case_1 = round((count_case_1/n),2)

        if old_pet[i] == 'perro':
            count_case_2 += 1
        prob_case_2 = round((count_case_2/n),2)

            
        if young_pet[i] == 'perro' and old_pet[i] == 'perro':
            count_case_3 += 1
        prob_case_3 = round((count_case_3/n),2)
        
    print(young_pet)
    print(old_pet)
    print("")
    print("count_cases")
    print(count_case_1)
    print(count_case_2)
    print(count_case_3)
    print("")
    print("probs")
    print(prob_case_1)
    print(prob_case_2)
    print(prob_case_3)        
    


    return prob_case_1, prob_case_2, prob_case_3

simulate_pets_prob(10)
