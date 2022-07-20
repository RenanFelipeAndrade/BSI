import matplotlib.pyplot as plt  # matplot para gráfico


def f(x):
    """
    Letras do nome:
        Primeiro nome: Renan
            R = 0.571
            E = 11.18
            N = 3.918

        Último nome: Silva
            S = -2.691
            I = 0.912
            L = 4.705
    """

    return (
        0.571 * x**5
        + 11.18 * x**4
        + 3.918 * x**3
        + -2.691 * x**2
        + 0.912 * x
        + 4.705
    )


def valores_em_y(valor_inicial, valor_final):
    """
    Recebe valores inicial e final. Produz um intervalo entre os valores (incluindo-os).
    Calcula os y e retorna uma lista dos valores de x e valores de y
    """
    valores_y = []
    valores_x = []

    # isso garante que o valor inicial seja menor que o final
    valor_inicial, valor_final = min([valor_inicial, valor_final]), max(
        [valor_inicial, valor_final]
    )

    intervalo = []

    # loop entre os valores iniciais e final -1
    for numero in range(valor_inicial, valor_final):
        intervalo.append(numero)

        # toda vez que o tamanho da lista for impar, adicione também o número + meio
        if len(intervalo) % 2 != 0:
            intervalo.append((0.5 + numero))

    # incluímos o valor final
    intervalo.append(valor_final)

    # calculamos os xises (vários x)
    for x in intervalo:
        valor_y = f(x)
        valores_x.append(x)
        valores_y.append(valor_y)

    # retorna um dicionário com valores de x e y
    return {"valores_x": valores_x, "valores_y": valores_y}


def encontra_mudanca_sinal(lista_valores_x, lista_valores_y):
    """
    Percorre valores em y e adiciona os intervalos em uma lista quando y mudar de sinal.
    """
    intervalos_y = []
    intervalos_x = []
    y_anterior = 0

    # percorre na lista de y, armazenando também a posição do valor
    for index, y in enumerate(lista_valores_y):
        # se y for positivo e se tornar negativo, ou o contrário
        if (y < 0 and y_anterior > 0) or (y > 0 and y_anterior < 0):
            # adicione o y_anterior e y em uma lista intervalo_y
            intervalo_y = [y_anterior, y]
            intervalos_y.append(intervalo_y)

            intervalo_x = [lista_valores_x[index - 1], lista_valores_x[index]]
            intervalos_x.append(intervalo_x)

        y_anterior = y

    # retorna um dicionário com intervalos de x e y
    return {"intervalos_x": intervalos_x, "intervalos_y": intervalos_y}


def busca_binaria(intervalos_x, intervalos_y, index, iteracao, iteracoes, valores_erro):
    """
    Função recursiva para refinamento/busca binária.

    Recebe lista de intervalos (lista de listas) de x, y;
    Intervalo a ser acessado, ou seja, index;
    Iteração atual, ou seja, quantidade de vezes que o refinamento ocorreu;
    Iterações, lista de iterações para montar gráfico.
    Valores_erro, lista com os valores do módulo da diferença entre o x anterior e x atual.
    """

    # se tentarmos acessar um valor fora da lista de intervalos, retorne os valores e não executamos nada
    if index >= len(intervalos_x):
        return {
            "intervalos_x": intervalos_x,
            "intervalos_y": intervalos_y,
            "valores_erro": valores_erro,
            "iteracoes": iteracoes,
        }

    # ao entrar no loop, adicione o valor da iteração na lista de iterações
    iteracoes.append(iteracao)

    diferenca_atual = 0

    novo_intervalo_x = []
    novo_intervalo_y = []

    # ipslons à direita e à esquerda do intervalo atual
    y_esquerdo = intervalos_y[index][0]
    y_direito = intervalos_y[index][1]

    # xises à direita e à esquerda do intervalo atual
    x_esquerdo = intervalos_x[index][0]
    x_direito = intervalos_x[index][1]

    # calculamos a metade do intervalo em x
    metade = (intervalos_x[index][0] + intervalos_x[index][1]) / 2

    # calculamos um novo y baseado na metade
    novo_y = f(metade)

    # se o novo y for negativo
    if novo_y < 0:
        # se o y à esquerda no intervalo for negativo
        if intervalos_y[index][0] < 0:
            # criamos um novo intervalo com y atual à esquerda, mantendo o valor à direta
            novo_intervalo_y.append(novo_y)
            novo_intervalo_y.append(y_direito)

            # criamos um novo intervalo com x atual (o "metade") à esquerda, mantendo o valor à direta
            novo_intervalo_x.append(metade)
            novo_intervalo_x.append(x_direito)

        # se o y à esquerda no intervalo for positivo, substitua no lado oposto
        else:
            novo_intervalo_y.append(y_esquerdo)
            novo_intervalo_y.append(novo_y)

            novo_intervalo_x.append(x_esquerdo)
            novo_intervalo_x.append(metade)

    # se o novo y for positivo, faça verificações semelhantes e substitua
    else:
        # se o y à esquerda no intervalo for positivo
        if intervalos_y[index][0] > 0:
            # criamos um novo intervalo com y atual à esquerda, mantendo o valor à direta
            novo_intervalo_y.append(novo_y)
            novo_intervalo_y.append(y_direito)

            # criamos um novo intervalo com x atual (o "metade") à esquerda, mantendo o valor à direta
            novo_intervalo_x.append(metade)
            novo_intervalo_x.append(x_direito)

        # se o y à esquerda no intervalo for negativo, substitua no lado oposto
        else:
            novo_intervalo_y.append(y_esquerdo)
            novo_intervalo_y.append(novo_y)

            novo_intervalo_x.append(x_esquerdo)
            novo_intervalo_x.append(metade)

    # calcule o menor erro entre o x à esquerda e à direita
    # adicione o menor valor na diferenca_atual e na lista de erro
    if abs(metade - x_esquerdo) < abs(metade - x_direito):
        diferenca_atual = abs(metade - x_esquerdo)
        valores_erro.append(diferenca_atual)
    else:
        diferenca_atual = abs(metade - x_direito)
        valores_erro.append(diferenca_atual)

    # substitua os intervalos anteriores pelos novos
    intervalos_x[index] = novo_intervalo_x
    intervalos_y[index] = novo_intervalo_y

    # terminado 1 refinamento, adicionamos 1 à iteração
    iteracao += 1

    # respeitado a condição de parada
    if diferenca_atual < 10**-6:
        # adicione 1 ao index para acessar próximo intervalo
        index += 1

    # repete todo o processo com os intervalos, index, iterações e valores_erro atualizados
    return busca_binaria(
        intervalos_x, intervalos_y, index, iteracao, iteracoes, valores_erro
    )


# recebe os valores de x e y dado um intervalo de número para x
lista_valores = valores_em_y(-20, 20)

# encontra os intervalos contendo raízes com base nos valores calculados anteriormente
intervalos = encontra_mudanca_sinal(
    lista_valores["valores_x"], lista_valores["valores_y"]
)

print(f'\nAs raízes estão nos intervalos {intervalos["intervalos_x"]}\n')

# refina os intervalos com base na busca binária
resultado_refinado = busca_binaria(
    intervalos["intervalos_x"],
    intervalos["intervalos_y"],
    index=0,
    iteracao=0,
    iteracoes=[],
    valores_erro=[],
)

print(f'As raízes refinadas são {resultado_refinado["intervalos_x"]}\n')


plt.plot(resultado_refinado["iteracoes"], resultado_refinado["valores_erro"])
plt.title("Gráfico valores de erro vs iteração")
plt.xlabel("Iterações")
plt.ylabel("|x1 - x|")
plt.show()
