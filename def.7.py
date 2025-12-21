def salario_funcionario(salario):
    if salario <= 500:
        bonificacao = salario * 0.05
        return salario + bonificacao
    elif salario <= 1200:
        bonificacao = salario * 0.12
        return salario + bonificacao
    else:
        print("O funcionário não receberá bonificação.")
        return salario

def auxilio_escolar(salario):
    if salario <= 600:
        return salario + 150
    else:
        return salario + 100

def inss(salario):
    if salario < 1000:
        desconto = 0.0
    elif salario <= 2000:
        desconto = salario * 0.08
    else:
        desconto = salario * 0.10
    return salario - desconto

print("-" * 30)
print("1. funcionário")
print("2.auxílio escolar")
print("3.INSS")
print("-" * 30)

print("------------------------------")
op = int(input("Escolha uma opção: "))
salario = float(input("Digite o salário da sua funcao: "))
print("------------------------------")

if op == 1:
    print(f"O salário do funcionário é {salario_funcionario(salario)}")
elif op == 2:
    print(f"O salário do auxílio escolar é {auxilio_escolar(salario)}")
elif op == 3:
    print(f"O salário do INSS é {inss(salario)}")
print("-" * 20)



