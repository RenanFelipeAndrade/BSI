# Lista de exercícios com testes


def media_notas(nota1, nota2):
    """Retorna a média aritmética das duas notas

    Argumentos:
        nota1 (float): primeira nota
        nota2 (float): segunda nota

    Retorna:
        float: a média aritmética das duas notas.
    """
    return round((nota1 + nota2) / 2, 1)


def aprovado(media):
    """Retorne True se a média for maior ou igual a 7.0.
    Caso contrário, retorna False


    Argumento:
        media (float): a média do aluno

    Retorna:
        bool: True se média for maior ou igual a 7.0
              False se média for menor que 7.0

    """
    return media >= 7.0


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % "Falhou"
    else:
        prefixo = "\033[32m%s" % "Passou"
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (prefixo, repr(esperado), repr(obtido))
    )


def main():

    print(" Média de notas:")
    test(
        media_notas(
            nota1=10.0,
            nota2=10.0,
        ),
        10.0,
    )
    test(media_notas(nota1=0, nota2=0), 0.0)
    test(media_notas(nota1=10, nota2=0), 5.0)
    test(media_notas(nota1=0, nota2=10), 5.0)
    test(media_notas(nota1=7.0, nota2=8.0), 7.5)
    test(media_notas(nota1=7.5, nota2=8.2), 7.8)

    print(" Situação do aluno:")
    test(aprovado(media=0.0), False)
    test(aprovado(media=1.0), False)
    test(aprovado(media=6.9), False)
    test(aprovado(media=7.0), True)
    test(aprovado(media=7.1), True)
    test(aprovado(media=9.9), True)
    test(aprovado(media=10.0), True)


if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
