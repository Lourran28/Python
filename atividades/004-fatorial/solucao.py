def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Não existe fatorial de número negativo.")
else:
    print(f"O fatorial de {numero} é {fatorial(numero)}")
