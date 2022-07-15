from numpy import linspace


def funcao(x):
    return x**5 - 7 * x**4 + 8 * x**2 + 7
    # x = -1 y = 6
    # x = -0.5 y = valor negativo
    # return -3 * x**7 + 4 * x**6 - 8 * x**3 - 8


def valores_em_y(valor_inicial, valor_final):
    valores_y = []
    valores_x = []
    valor_inicial, valor_final = min([valor_inicial, valor_final]), max(
        [valor_inicial, valor_final]
    )
    intervalo = linspace(valor_inicial, valor_final, 10)

    for x in intervalo:
        valor = funcao(x)
        valores_x.append(x)
        valores_y.append(valor)

    return {"entrada": valores_x, "saida": valores_y}


def encontra_mudanca_sinal(lista_valores_x, lista_valores_y):
    valores_y = []
    valores_x = []
    y_anterior = 0
    for posicao, y in enumerate(lista_valores_y):
        if (y < 0 and y_anterior > 0) or (y > 0 and y_anterior < 0):
            valores_y.append(y_anterior)
            valores_y.append(y)
            valores_x.append(lista_valores_x[posicao - 1])
            valores_x.append(lista_valores_x[posicao])
        y_anterior = y
    print(
        f"Retorno da função encontra mudança de sinal \n{ {'intervalo_x': valores_x, 'intervalo_y': valores_y} } \n"
    )
    return {"intervalo_x": valores_x, "intervalo_y": valores_y}


def busca_binaria(intervalo_x, intervalo_y):
    metade = (intervalo_x[0] + intervalo_x[1]) / 2
    novo_y = funcao(metade)
    if (abs(novo_y) - abs(intervalo_y[0])) < (abs(novo_y) - abs(intervalo_y[1])):
        intervalo_y[0] = novo_y
        intervalo_x[0] = metade
    else:
        intervalo_y[1] = novo_y
        intervalo_x[1] = metade

    print(
        f"Retorno da função busca binária \n{ {'intervalo_x': intervalo_x, 'intervalo_y': intervalo_y} } \n"
    )
    return {"intervalo_x": intervalo_x, "intervalo_y": intervalo_y}


lista_valores = valores_em_y(-1, -1.5)
intervalos = encontra_mudanca_sinal(lista_valores["entrada"], lista_valores["saida"])
for _ in range(5):
    intervalos = busca_binaria(intervalos["intervalo_x"], intervalos["intervalo_y"])
