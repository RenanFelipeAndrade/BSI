import matplotlib.pyplot as plt
import numpy as np


def remove_duplicados(lista):
    return [
        elemento
        for index, elemento in enumerate(lista)
        if index == lista.index(elemento)
    ]


def calcular_frequencia_letras(texto):
    lista_letras = []
    for caracter in texto:
        if caracter.isalpha():
            lista_letras.append(caracter)
    return lista_letras


def mostra_grafico(frequencia_letras, linguas):
    rotulos = []
    for lingua in linguas:
        rotulos_lingua, _ = zip(*frequencia_letras[lingua].most_common(5))
        rotulos = [*rotulos, *rotulos_lingua]

    # não utilizar set() para não alterar a ordem das letras
    rotulos = remove_duplicados(rotulos)

    valores_pt = [frequencia_letras["portugues"][chave] for chave in rotulos]
    valores_en = [frequencia_letras["espanhol"][chave] for chave in rotulos]
    valores_fr = [frequencia_letras["frances"][chave] for chave in rotulos]

    x = np.arange(len(rotulos))

    largura = 0.2
    fig, ax = plt.subplots()
    barras = {}
    barras["pt"] = ax.bar(x - largura, valores_pt, largura, label="Português (Br)")
    barras["es"] = ax.bar(x, valores_en, largura, label="Espanhol")
    barras["fr"] = ax.bar(x + largura, valores_fr, largura, label="Francês")

    ax.set_ylabel("Frequência das letras")
    ax.set_title("Letras mais frequêntes em Gene Egoísta")
    ax.set_xticks(x, rotulos)
    ax.legend()

    for lingua in barras:
        ax.bar_label(barras[lingua], padding=3)

    fig.tight_layout()

    plt.show()
