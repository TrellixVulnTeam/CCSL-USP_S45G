def dimensoes(m):
    i = 0
    for each in range(len(m)):
        j = 0
        for nested in range(len(m[each])):
            j += 1
        i += 1
    resultado = print(i,'X',j)
    return resultado
