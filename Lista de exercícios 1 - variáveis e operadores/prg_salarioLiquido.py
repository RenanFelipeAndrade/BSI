income_per_hour = float(input("Insira o valor por hora(R$): "))
hours_worked = int(input("Insira a quantia de horas mensais trabalhadas: "))

gross_pay = income_per_hour * hours_worked
fees = {"inss": 0.08, "IR": 0.11, "syndicate": 0.05}

net_pay = round(gross_pay -
                (gross_pay * fees["inss"] + gross_pay *
                 fees["IR"] + gross_pay * fees["syndicate"]), 2)

print(f"O salário líquido após os descontos é: {net_pay}")
