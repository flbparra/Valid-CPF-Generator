
from cpf_package.number_generator import num_generator

def cpf_generator(digitos):
    
    sum_results = 0

    if len(digitos) == 9:
        contador = 10
        for digito in digitos:
            sum_results += int(digito) * contador
            contador -= 1
        
        first_digit = (sum_results * 10) % 11
        first_digit = first_digit if first_digit <= 9 else 0
        dez_digitos = digitos + str(first_digit)
        
        return dez_digitos
    
    else:
        contador = 11
        for digito in digitos:
            sum_results += int(digito) * contador
            contador -= 1
        
        second_digit = (sum_results * 10) % 11
        second_digit = second_digit if second_digit <= 9 else 0
        final_digitos = digitos + str(second_digit)
        
        return final_digitos

def cpf_init():
    #gerando primeiros 9 numeros do cpf
    cpf_digitos = num_generator(9)

    #gerando digito um e add no novo cpf
    cpf_digitos = cpf_generator(cpf_digitos)

    #versão final do cpf
    cpf_gerado = cpf_generator(cpf_digitos)

    return cpf_gerado



