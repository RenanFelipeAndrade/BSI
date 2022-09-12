from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


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
    ax.set_ylabel("frequência das letras")
    ax.set_title("Letras mais frequêntes em Gene Egoísta")
    ax.set_xticks(x, rotulos)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()


def main():
    texto = {}
    with open("./Python/Poetry/Arquivos/Richard_Dawkins_O_Gene_Egoista.txt") as arquivo:
        texto["portugues"] = arquivo.read().lower()
    with open(
        "./Python/Poetry/Arquivos/Richard_Dawkins_O_Gene_Egoista_espanhol.txt"
    ) as arquivo:
        texto["espanhol"] = arquivo.read().lower()
    with open(
        "./Python/Poetry/Arquivos/Richard_Dawkins_O_Gene_Egoista_fances.txt"
    ) as arquivo:
        texto["frances"] = arquivo.read().lower()

    letras_portugues = [
        character for character in texto["portugues"] if character.isalpha()
    ]
    letras_espanhol = [
        character for character in texto["espanhol"] if character.isalpha()
    ]
    letras_frances = [
        character for character in texto["frances"] if character.isalpha()
    ]

    frequencia_letras = {}
    frequencia_letras["portugues"] = Counter(letras_portugues)
    frequencia_letras["espanhol"] = Counter(letras_espanhol)
    frequencia_letras["frances"] = Counter(letras_frances)
    mostra_grafico(frequencia_letras)


if __name__ == "__main__":
    main()
