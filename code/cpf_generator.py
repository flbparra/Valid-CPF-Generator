import random

"""
Aqui temos algumas coisas para se melhorar, a primeira e em questão a complexibilidade do código
usandp funções talvez fique melhor.

"""
nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_1 = 10
contador_2 = 11
sum_results = 0

#for i in digitos:
for digito in nove_digitos:
    sum_results += int(digito) * contador_1
    contador_1 -= 1

first_digit = (sum_results * 10) % 11
first_digit = first_digit if first_digit <= 9 else 0

dez_digitos = nove_digitos + str(first_digit)
sum_results = 0

for digito in dez_digitos:
    sum_results += int(digito) * contador_2
    contador_2 -= 1

second_digit = (sum_results * 10) % 11
second_digit = second_digit if second_digit <= 9 else 0

cpf_gerado = dez_digitos + str(second_digit)

print(cpf_gerado)


