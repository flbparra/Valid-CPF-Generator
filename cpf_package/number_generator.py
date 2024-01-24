import random

def num_generator(num):
    
    digitos = ''
    for i in range(num):
        digitos += str(random.randint(0, 9))

    return digitos