from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def main():
    texto = {}
    with open("./Python/Poetry/Arquivos/Richard_Dawkins_O_Gene_Egoista.txt") as arquivo:
        texto["portugues"] = arquivo.read().lower()
    with open(
        "./Python/Poetry/Arquivos/Richard_Dawkins_O_Gene_Egoista_espanhol.txt"
    ) as arquivo:
        texto["espanhol"] = arquivo.read().lower()

    letras_portugues = [
        character for character in texto["portugues"] if character.isalpha()
    ]
    letras_espanhol = [
        character for character in texto["espanhol"] if character.isalpha()
    ]

    frequencia_letras = {}
    frequencia_letras["portugues"] = Counter(letras_portugues)
    frequencia_letras["espanhol"] = Counter(letras_espanhol)

    rotulos_pt, valores_pt = zip(*frequencia_letras["portugues"].most_common(5))
    rotulos_es, valores_es = zip(*frequencia_letras["espanhol"].most_common(5))

    x = np.arange(len(rotulos_es))

    width = 0.2
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, valores_pt, width, label="Português (Br)")
    rects2 = ax.bar(x + width / 2, valores_es, width, label="Espanhol")
    ax.set_ylabel("frequência das letras")
    ax.set_title("Letras mais frequêntes em Gene Egoísta")
    ax.set_xticks(x, rotulos_pt)
    # ax.set_xticks(x, rotulos_es)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
