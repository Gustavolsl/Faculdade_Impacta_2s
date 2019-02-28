def divisores(numero):
    i = 1
    lista = []
    for i in range(numero):
        i +=1

        if numero % i == 0:
            lista.append(i)
    return lista
        
def primo(n):

    resultado = 0
    resultado = divisores(n)

    if len(resultado) == 2:
        return "é primo"
    else:
        return "não é primo"

def num_perfeito(x):
    resultado = []
    
    resultado = divisores(x)

    i = 0

    soma = 0
    
    for i in range (0, len(resultado)):
        
        
        soma += resultado[i]


        i += 1

    if soma == x * 2:
        return "perfeito"
    else:
        return "imperfeito"
        

    
        

    
