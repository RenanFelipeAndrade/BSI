price = float(input("Insira o preço (R$): "))
discount = int(input("Insira a porcentagem do desconto (%): "))

new_price = round(price * (1 - discount / 100), 2)

print(f"O preço será de: {new_price} reais")
