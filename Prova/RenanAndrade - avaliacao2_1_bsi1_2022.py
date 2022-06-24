# Avaliação 2 - BSI


def dobro(a, b):
    """
    Dados dois números inteiros retorna sua soma,
    porém se os números forem iguais retorna o dobro da soma.
    """
    if a == b:
        return (a + b) * 2
    return a + b


def dez(a, b):
    """
    Dados dois inteiros, retorna True se um dos dois é 10 ou a soma é 10.
    """
    return a == 10 or b == 10 or a + b == 10


def troca(s):
    """
    Seja uma string,
    se ela tiver tamanho <= 1 retorna ela mesma,
    caso contrário troca a primeira e a última letra.
    """
    if len(s) <= 1:
        return s
    string_formatada = s[-1] + s[1:-1] + s[0]  # troca primeira e última letra
    return string_formatada


def inicio_nove(nums):
    """
    Verifica se pelo menos um dos quatro primeiros itens é nove.
    """
    return (
        nums.index(9) < 4 if 9 in nums else False
    )  # procura o index apenas se existir o 9 na lista


def primeira_metade(s):
    """
    Seja uma string, retorna a primeira metade da string.
    """
    return s[: len(s) // 2]


def sem_pontas(s):
    """
    Seja uma string de pelo menos dois caracteres,
    retorna uma string sem o primeiro e último caracter.
    """
    return s[1:-1]


def gira_esquerda(s):
    """
    Rodar à esquerda uma string duas posições.
    A string possui pelo menos 2 caracteres.
    """
    return s[2:] + s[:2]


def inicio_fim_igual(nums):
    """
    Retorna True se a lista possui pelo menos um elemento
    e o primeiro elemento é igual ao último
    """
    return nums[0] == nums[-1] if len(nums) != 0 else False


def numero_invertido(num):
    """
    Receba um inteiro positivo e o mostre invertido.
    Ex.: 1234 gera 4321
    """
    return int(str(num)[::-1])  # converte para string, inverte, converte para inteiro


def nomes_pontas(n):
    """Dada uma string contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome, em
    maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO MENDES"
    """
    nomes = n.split(" ")

    return f"{nomes[0].upper()} {nomes[-1].upper()}"


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("soma_dobro")
    test(dobro(1, 2), 3)
    test(dobro(3, 2), 5)
    test(dobro(2, 2), 8)
    test(dobro(-1, 0), -1)
    test(dobro(0, 0), 0)
    test(dobro(0, 1), 1)

    print("dez")
    test(dez(9, 10), True)
    test(dez(9, 9), False)
    test(dez(1, 9), True)
    test(dez(10, 1), True)
    test(dez(10, 10), True)
    test(dez(8, 2), True)
    test(dez(8, 3), False)
    test(dez(10, 42), True)
    test(dez(12, -2), True)

    print("troca")
    test(troca("code"), "eodc")
    test(troca("a"), "a")
    test(troca("ab"), "ba")
    test(troca("abc"), "cba")
    test(troca(""), "")
    test(troca("Chocolate"), "ehocolatC")
    test(troca("nythoP"), "Python")
    test(troca("hello"), "oellh")

    print("nove_na_frente")
    test(inicio_nove([1, 2, 9, 3, 4]), True)
    test(inicio_nove([1, 2, 3, 4, 9]), False)
    test(inicio_nove([1, 2, 3, 4, 5]), False)
    test(inicio_nove([9, 2, 3]), True)
    test(inicio_nove([1, 9, 9]), True)
    test(inicio_nove([1, 2, 3]), False)
    test(inicio_nove([1, 9]), True)
    test(inicio_nove([5, 5]), False)
    test(inicio_nove([2]), False)
    test(inicio_nove([9]), True)
    test(inicio_nove([]), False)
    test(inicio_nove([3, 9, 2, 3, 3]), True)

    print("primeira_metade")
    test(primeira_metade("papagaio"), "papa")
    test(primeira_metade("Lula"), "Lu")
    test(primeira_metade("abcdef"), "abc")
    test(primeira_metade("ab"), "a")
    test(primeira_metade(""), "")
    test(primeira_metade("0123456789"), "01234")
    test(primeira_metade("buraco"), "bur")
    test(primeira_metade("joinville"), "join")

    print("sem_pontas")
    test(sem_pontas("Beleza"), "elez")
    test(sem_pontas("Python"), "ytho")
    test(sem_pontas("codigo"), "odig")
    test(sem_pontas("sala"), "al")
    test(sem_pontas("ab"), "")
    test(sem_pontas("Chocolate!"), "hocolate")
    test(sem_pontas("cozinha"), "ozinh")
    test(sem_pontas("Uhull"), "hul")

    print("gira_esquerda_2")
    test(gira_esquerda("Beleza"), "lezaBe")
    test(gira_esquerda("python"), "thonpy")
    test(gira_esquerda("Oi"), "Oi")
    test(gira_esquerda("code"), "deco")
    test(gira_esquerda("tio"), "oti")
    test(gira_esquerda("12345"), "34512")
    test(gira_esquerda("Chocolate"), "ocolateCh")
    test(gira_esquerda("tijolo"), "joloti")

    print("inicio_fim_igual")
    test(inicio_fim_igual([1, 2, 3]), False)
    test(inicio_fim_igual([1, 2, 3, 1]), True)
    test(inicio_fim_igual([1, 2, 1]), True)
    test(inicio_fim_igual([7]), True)
    test(inicio_fim_igual([]), False)
    test(inicio_fim_igual([7, 7]), True)

    print("número invertido")
    test(numero_invertido(1), 1)
    test(numero_invertido(0), 0)
    test(numero_invertido(10), 1)
    test(numero_invertido(1111), 1111)
    test(numero_invertido(00000), 0)
    test(numero_invertido(1234), 4321)
    test(numero_invertido(2013), 3102)
    test(numero_invertido(20130711), 11703102)

    print("nomes_pontas")
    test(nomes_pontas("Ivo Riegel"), "IVO RIEGEL")
    test(nomes_pontas("Eduardo da Silva"), "EDUARDO SILVA")
    test(nomes_pontas("Fernando José Braz"), "FERNANDO BRAZ")
    test(nomes_pontas("Marco André Lopes Mendes"), "MARCO MENDES")
    test(nomes_pontas("Paulo César de Oliveira"), "PAULO OLIVEIRA")


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
