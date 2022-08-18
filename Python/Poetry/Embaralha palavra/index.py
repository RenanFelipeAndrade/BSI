from random import shuffle, randint

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

frases_motivacionais = [
    "Vamos lá, você consegue!",
    "Não se desespere, você consegue!",
    "Positividade!",
    "Quase! Vamos lá, tente novamente!",
    "Não desista!",
]

shuffle(palavras)
palavra_sorteada = palavras[randint(0, len(palavras) - 1)]
palavra_embaralhada = list(palavra_sorteada)
shuffle(palavra_embaralhada)
palavra_embaralhada = "".join(palavra_embaralhada)
tentativa = 0

while True:
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
    print(f"\n{frases_motivacionais[randint(0, len(frases_motivacionais)-1)]}")
