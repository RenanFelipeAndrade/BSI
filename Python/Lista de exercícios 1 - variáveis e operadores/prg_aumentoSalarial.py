wage = float(input("Insira o salário (R$): "))
increase = int(input("Insira a porcentagem do aumento (%): "))

new_wage = round(wage * (1 + increase / 100), 2)

print(f"O salário será de: {new_wage} reais")
