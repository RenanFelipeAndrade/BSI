from sorteia_palavra import sorteia_palavra
from frase_motivacional import frase_motivacional
from embaralha_palavra import embaralha_palavra


def main(tema, dificuldade_selecionada):
    tentativa = 0
    palavra_sorteada, dificuldade = sorteia_palavra(
        tema, dificuldade_selecionada)
    palavra_embaralhada = embaralha_palavra(palavra_sorteada)

    while True:
        frase_sorteada = frase_motivacional()

        print("A palavra embaralhada é", palavra_embaralhada)
        print("A dificuldade é:", dificuldade)
        print("Você ganha se acerta em, no máximo, 5 tentativas")

        print("\n------ Se quiser desistir, digite 'parar' ------")
        palpite = input("Qual é a palavra? \n> ")
        tentativa += 1

        if palpite.lower() == "parar":
            return print(f"Uma pena :/\nA palavra era: {palavra_sorteada}")

        elif palpite.lower() == palavra_sorteada.lower():
            print(
                f"Você ganhou! \nForam {tentativa} {'tentativas' if tentativa > 1 else 'tentativa'}"
            ) if tentativa <= 5 else print(
                f"Você perdeu :( \nForam {tentativa} {'tentativas' if tentativa > 1 else 'tentativa'}"
            )
            break
        print(f"\n{frase_sorteada}")


if __name__ == "__main__":
    while True:
        tema = int(
            input(
                """
Escolha um dos temas a seguir (digite o número do tema):
    1 = cidade
    2 = objetos
    3 = paises
    4 = verbos
    
>> """
            )
        )

        dificuldade = int(
            input(
                """
Escolha uma das dificuldades a seguir (digite o número do dificuldade):
    1 = fácil
    2 = médio
    3 = difícil
    
>> """
            )
        )

        if tema > 4 or tema < 1 or dificuldade < 1 or dificuldade > 3:
            print("--------- Escolha um tema e dificuldades válidas! ---------")
        else:
            break

    main(tema, dificuldade)
