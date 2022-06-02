eggs = int(input("Insira a quantidade de ovos: "))

dozens = 1 + eggs // 12 if eggs % 12 > 0 else eggs // 12

print(f"A quantidade de dúzias é: {dozens}")
