import matplotlib.pyplot as plt


def f(x):
    return (
        0.571 * x**5
        + 11.18 * x**4
        + 3.918 * x**3
        + -2.691 * x**2
        + 0.912 * x
        + 4.705
    )


def valores_em_y(valor_inicial, valor_final):
    valores_y = []
    valores_x = []
    valor_inicial, valor_final = min([valor_inicial, valor_final]), max(
        [valor_inicial, valor_final]
    )
    intervalo = []

    for numero in range(valor_inicial, valor_final):
        intervalo.append(numero)
        if len(intervalo) % 2 != 0:
            intervalo.append((0.5 + numero))
    intervalo.append(valor_final)

    for x in intervalo:
        valor_y = f(x)
        valores_x.append(x)
        valores_y.append(valor_y)

    return {"valores_x": valores_x, "valores_y": valores_y}


def encontra_mudanca_sinal(lista_valores_x, lista_valores_y):
    intervalos_y = []
    intervalos_x = []
    y_anterior = 0

    for posicao, y in enumerate(lista_valores_y):
        if (y < 0 and y_anterior > 0) or (y > 0 and y_anterior < 0):
            intervalo_y = [y_anterior, y]
            intervalos_y.append(intervalo_y)

            intervalo_x = [lista_valores_x[posicao - 1], lista_valores_x[posicao]]
            intervalos_x.append(intervalo_x)

        y_anterior = y

    return {"intervalos_x": intervalos_x, "intervalos_y": intervalos_y}


def busca_binaria(intervalos_x, intervalos_y, posicao, iteracao, iteracoes, erro):
    if posicao >= len(intervalos_x):
        return {
            "intervalos_x": intervalos_x,
            "intervalos_y": intervalos_y,
            "erro": erro,
            "iteracoes": iteracoes,
        }

    iteracoes.append(iteracao)
    novo_intervalo_x = []
    novo_intervalo_y = []
    metade = (intervalos_x[posicao][0] + intervalos_x[posicao][1]) / 2
    novo_y = f(metade)

    if novo_y < 0:
        if intervalos_y[posicao][0] > 0:
            novo_intervalo_y.append(intervalos_y[posicao][0])
            novo_intervalo_y.append(novo_y)

            novo_intervalo_x.append(intervalos_x[posicao][0])
            novo_intervalo_x.append(metade)
        else:
            novo_intervalo_y.append(novo_y)
            novo_intervalo_y.append(intervalos_y[posicao][1])

            novo_intervalo_x.append(metade)
            novo_intervalo_x.append(intervalos_x[posicao][1])

    else:
        if intervalos_y[posicao][0] > 0:
            novo_intervalo_y.append(novo_y)
            novo_intervalo_y.append(intervalos_y[posicao][1])

            novo_intervalo_x.append(metade)
            novo_intervalo_x.append(intervalos_x[posicao][1])
        else:
            novo_intervalo_y.append(intervalos_y[posicao][0])
            novo_intervalo_y.append(novo_y)

            novo_intervalo_x.append(intervalos_x[posicao][0])
            novo_intervalo_x.append(metade)

    if abs(metade - intervalos_x[posicao][0]) < abs(metade - intervalos_x[posicao][1]):
        erro.append(abs(metade - intervalos_x[posicao][0]))
    else:
        erro.append(abs(metade - intervalos_x[posicao][1]))

    iteracao += 1
    if (abs(metade - intervalos_x[posicao][0]) < 10**-6) or (
        abs(metade - intervalos_x[posicao][1]) < 10**-6
    ):
        intervalos_x[posicao] = novo_intervalo_x
        intervalos_y[posicao] = novo_intervalo_y
        if posicao < len(intervalos_x):
            posicao += 1
            return busca_binaria(
                intervalos_x, intervalos_y, posicao, iteracao, iteracoes, erro
            )
    else:
        intervalos_x[posicao] = novo_intervalo_x
        intervalos_y[posicao] = novo_intervalo_y
        return busca_binaria(
            intervalos_x, intervalos_y, posicao, iteracao, iteracoes, erro
        )


lista_valores = valores_em_y(-20, 20)
intervalos = encontra_mudanca_sinal(
    lista_valores["valores_x"], lista_valores["valores_y"]
)
resultado_refinado = busca_binaria(
    intervalos["intervalos_x"],
    intervalos["intervalos_y"],
    posicao=0,
    iteracao=0,
    iteracoes=[],
    erro=[],
)


fig, ax = plt.subplots()
print(resultado_refinado["iteracoes"], resultado_refinado["erro"])
ax.plot(resultado_refinado["iteracoes"], resultado_refinado["erro"])
plt.show()
