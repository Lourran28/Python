print("-" * 30)
print("1. adição")
print("2. multiplicação")
print("3. subtração")
print("4. divisão")
print("-" * 30)

def adicao(a, b):
    return a + b
def multiplicacao(a, b):
    return a * b
def subtracao(a, b):
    return a - b
def divisao(a, b):
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b
print("Escolha uma operação")
while True:
    operacao = input("Digite a operação desejada (1, 2, 3 ou 4): ")
    if operacao in ['1', '2', '3', '4']:
        break
    print("Operação inválida! Tente novamente.")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
if operacao == '1':
    print(f"A soma de {a} e {b} é {adicao(a, b)}")
elif operacao == '2':
    print(f"A multiplicação de {a} e {b} é {multiplicacao(a, b)}")
elif operacao == '3':
    print(f"A subtração de {a} e {b} é {subtracao(a, b)}")
elif operacao == '4':
    print(f"A divisão de {a} por {b} é {divisao(a, b)}")
print("-" * 20)  