from random import shuffle


def embaralha_palavra(palavra, palavra_anterior=""):
    palavra_anterior = palavra
    palavra = list(palavra)
    shuffle(palavra)
    palavra = "".join(palavra)

    if palavra == palavra_anterior:
        return embaralha_palavra(palavra, palavra_anterior)
    return palavra
