def junta_pares():
   
    D = {}
    E = {}
    i = 30
    a = 1
    b = 30
    c = 30
    par_perfeito = 0

    for i in range(30,61):
        D[i] = 0
        E[i] = 0


        i += 1

    N = int(input())

    for a in range(N):
        tamanho = int(input())
        lado = input()

        if lado == "D":
            D[tamanho] += 1
        if lado == "E":
            E[tamanho] += 1

    for c in range(30,61):

        if D[c] != 0 and E[c] != 0:
            if D[c] <= E[c]:
                par_perfeito += D[c]
            elif E[c] < D[c]:
                par_perfeito += E[c]
        
        c += 1

    return par_perfeito
