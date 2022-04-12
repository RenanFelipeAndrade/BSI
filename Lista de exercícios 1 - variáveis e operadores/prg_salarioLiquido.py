gross_pay = float(input("Insira o salário (R$): "))
fees = {"inss": 0.08, "IR": 0.11, "syndicate": 0.05}

net_pay = round(gross_pay -
                (gross_pay * fees["inss"] + gross_pay *
                 fees["IR"] + gross_pay * fees["syndicate"]), 2)

print(f"O salário líquido após os descontos é: {net_pay}")
