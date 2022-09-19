import matplotlib.pyplot as plt
import numpy as np


def calcular_frequencia_letras(texto):
    lista_letras = []
    for caracter in texto:
        if caracter.isalpha():
            lista_letras.append(caracter)
    return lista_letras


def mostra_grafico(frequencia_letras):
    rotulos_pt, _ = zip(*frequencia_letras["portugues"].most_common(5))
    rotulos_es, _ = zip(*frequencia_letras["espanhol"].most_common(5))
    rotulos_fr, _ = zip(*frequencia_letras["frances"].most_common(5))

    rotulos = [*rotulos_pt, *rotulos_es, *rotulos_fr]
    rotulos = [
        rotulo for index, rotulo in enumerate(rotulos) if index == rotulos.index(rotulo)
    ]

    valores_pt = [frequencia_letras["portugues"][chave] for chave in rotulos]
    valores_en = [frequencia_letras["espanhol"][chave] for chave in rotulos]
    valores_fr = [frequencia_letras["frances"][chave] for chave in rotulos]
    x = np.arange(len(rotulos))

    width = 0.2

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, valores_pt, width, label="Português (Br)")
    rects2 = ax.bar(x + width / 2, valores_en, width, label="Espanhol")
    rects3 = ax.bar(x + width + width / 2, valores_fr, width, label="Francês")

    ax.set_ylabel("Frequência das letras")
    ax.set_title("Letras mais frequêntes em Gene Egoísta")
    ax.set_xticks(x, rotulos)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()
