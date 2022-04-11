wage = float(input("Insira o salário (R$): "))
increase = int(input("Insira a porcentagem do aumento (%): "))

new_wage = wage * (1 + increase / 100)

print(f"O salário será de: {new_wage} reais")
