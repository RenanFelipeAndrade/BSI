# Calcular as Raízes de uma Equação do 5º Grau

import matplotlib.pyplot as pyplot
import numpy as np


def calcularEquacao(valorX):

    x1 = 2.981
    x2 = -7.193
    x3 = 4.705
    x4 = -3.510
    x5 = 4.705
    x6 = -14.269
    y = (
        (x1 * pow(valorX, 5))
        + (x2 * pow(valorX, 4))
        + (x3 * pow(valorX, 3))
        + (x4 * pow(valorX, 2))
        + (x5 * pow(valorX, 1))
        + (x6)
    )

    print("\nResolução da equacao: {0} para x: {1}".format(y, valorX))
    return y


def encontra_raizes(intervalo_x, intervalo_y):
    y_anterior = 0
    novo_intervalo_y = []
    novo_intervalo_x = []

    for posicao, y_atual in enumerate(intervalo_y):
        x_atual = intervalo_x[posicao]
        x_anterior = intervalo_x[posicao - 1]

        if (y_atual > 0 and y_anterior < 0) or (y_atual < 0 and y_anterior > 0):
            novo_intervalo = [y_anterior, y_atual]
            novo_intervalo_y.append(novo_intervalo)

            novo_intervalo = [x_anterior, x_atual]
            novo_intervalo_x.append(novo_intervalo)
        y_anterior = y_atual

    return novo_intervalo_x, novo_intervalo_y


def refinador(intervalos_x, intervalos_y):
    valor_atual_erro = []
    quantidade_iteracao = []
    for posicao, _ in enumerate(intervalos_x):
        iteracao = 0
        while True:
            quantidade_iteracao.append(iteracao)

            x1 = intervalos_x[posicao][0]
            x2 = intervalos_x[posicao][1]

            y1 = intervalos_y[posicao][0]

            meio = (x1 + x2) / 2
            novo_y = calcularEquacao(meio)

            if novo_y < 0:
                if y1 < 0:
                    intervalos_y[posicao][0] = novo_y
                    intervalos_x[posicao][0] = meio
                else:
                    intervalos_y[posicao][1] = novo_y
                    intervalos_x[posicao][1] = meio
            else:
                if y1 > 0:
                    intervalos_y[posicao][0] = novo_y
                    intervalos_x[posicao][0] = meio
                else:
                    intervalos_y[posicao][1] = novo_y
                    intervalos_x[posicao][1] = meio

            if abs(meio - x1) < abs(meio - x2):
                valor_atual_erro.append(abs(meio - x1))
            else:
                valor_atual_erro.append(abs(meio - x2))

            iteracao += 1

            condicao_parada = (abs(meio - x1) < 10**-6) or (abs(meio - x2) < 10**-6)
            if condicao_parada:
                break
    return intervalos_x, intervalos_y, valor_atual_erro, quantidade_iteracao


def gerarGrafico(iteracoes, valores_erro):

    fig, ax = pyplot.subplots()
    # ax.set_ylim(lista[0], lista[-1])
    # ax.set_xlim(-20, 20)
    ax.plot(valores_erro, iteracoes)
    # for i, j in zip(x, y):
    #     ax.annotate(str(j), xy=(i, j))

    pyplot.xlabel("Vezes refinado")
    pyplot.ylabel("|x1 - x|")
    pyplot.show()


if __name__ == "__main__":
    while True:
        minha_lista_x = []
        minha_lista_y = []
        print("Calculando as raízes de uma equação de 5º grau\n")
        print("O intervalo é de -20 a 20 com incremento de 0,5\n")
        for x in range(-40, 40):
            x = x / 2
            valor = calcularEquacao(x)
            minha_lista_x.append(x)
            minha_lista_y.append(valor)

        x_raiz, y_raiz = encontra_raizes(minha_lista_x, minha_lista_y)
        x_refinado, y_refinado, iteracoes, erro = refinador(x_raiz, y_raiz)

        print(x_refinado, y_refinado)

        # print("\n", minha_lista_x, "\n", minha_lista_y, "\n")
        gerarGrafico(iteracoes, erro)
        continua = input("Deseja sair? Digite q ou Enter para novo cálculo:")
        if continua == "q":
            break
