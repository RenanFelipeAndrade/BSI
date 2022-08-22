from random import shuffle, randint


def sorteia_palavra():
    palavras = [
        "batata",
        "jogo",
        "tardigrado",
        "oculos",
        "quadro",
        "computador",
        "cabelo",
        "arara",
        "lasanha",
    ]
    shuffle(palavras)
    palavra_sorteada = palavras[randint(0, len(palavras) - 1)]
    return palavra_sorteada


def embaralhada_palavra(palavra, palavra_anterior=""):
    palavra_anterior = palavra
    palavra = list(palavra)
    shuffle(palavra)
    palavra = "".join(palavra)

    if palavra == palavra_anterior:
        return embaralhada_palavra(palavra, palavra_anterior)
    return palavra


def frases_motivacional():
    frases_motivacionais = [
        "Vamos lá, você consegue!",
        "Não se desespere, você consegue!",
        "Positividade!",
        "Quase! Vamos lá, tente novamente!",
        "Não desista!",
    ]

    frase_sorteada = frases_motivacionais[randint(0, len(frases_motivacionais) - 1)]
    return frase_sorteada


if __name__ == "__main__":
    tentativa = 0
    palavra_sorteada = sorteia_palavra()
    palavra_embaralhada = embaralhada_palavra(palavra_sorteada)

    while True:
        frase_sorteada = frases_motivacional()

        print("A palavra embaralhada é", palavra_embaralhada)
        print("Você ganha se acerta em, no máximo, 5 tentativas")

        palpite = input("Qual é a palavra? \n> ")
        tentativa += 1

        if palpite.lower() == palavra_sorteada.lower():

            print(
                f"Você ganhou! \nForam {tentativa} {'tentativas' if tentativa > 1 else 'tentativa'}"
            ) if tentativa <= 5 else print(
                f"Você perdeu :( \nForam {tentativa} {'tentativas' if tentativa > 1 else 'tentativa'}"
            )
            break
        print(f"\n{frase_sorteada}")
