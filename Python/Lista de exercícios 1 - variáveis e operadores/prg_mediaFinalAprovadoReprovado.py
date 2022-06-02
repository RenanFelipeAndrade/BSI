first_test_grade = float(input("Insira a nota da primeira prova: "))
second_test_grade = float(input("Insira a nota da segunda prova: "))
first_exercise_grade = float(input("Insira a nota do primeiro exercício: "))
second_exercise_grade = float(input("Insira a nota do segundo exercício: "))

# weighted average: test weighs 7; 3 exercise weights; 20 is the sum of all weights 7 + 7 + 3 + 3
status = "aprovado" if (first_test_grade * 7 + second_test_grade *
                        7 + first_exercise_grade * 3 + second_exercise_grade * 3) / 20 >= 7 else "reprovado"

print(f"O aluno foi {status}")
