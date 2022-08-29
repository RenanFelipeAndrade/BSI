from random import randint


def frase_motivacional():
    frases_motivacionais = [
        "Vamos lá, você consegue!",
        "Não se desespere, você consegue!",
        "Positividade!",
        "Quase! Vamos lá, tente novamente!",
        "Não desista!",
    ]

    frase_sorteada = frases_motivacionais[randint(0, len(frases_motivacionais) - 1)]
    return frase_sorteada
