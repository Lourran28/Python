print("Escolha uma opção:")
print("1. Soma")
print("2. Raiz quadrada")
print("3. Potência")

def soma(numero, numero2):
    return f"A soma do número {numero} com {numero2} é {numero + numero2}"

def raiz(numero):
    return f"A raiz quadrada de {numero} é {numero ** 0.5:.2f}"

def potencia(numero):
    return f"O número {numero} elevado ao quadrado é {numero ** 2}"

while True:
    op = int(input("Digite a opção desejada (1, 2 ou 3): "))
    if op in [1, 2, 3]:
        break
    print("Opção inválida! Tente novamente.")

if op == 1:
    numero = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    print(soma(numero, numero2))

elif op == 2:
    numero = float(input("Digite um número: "))
    print(raiz(numero))

elif op == 3:
    numero = float(input("Digite um número: "))
    print(potencia(numero))

print("-" * 20)  # separador entre operações


    