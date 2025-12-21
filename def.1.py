def positivo(numero):
    if numero > 0:
        return f"O número {numero} é positivo"
    else:
        return f"O número {numero} não é positivo"

def negativo(numero):
    if numero < 0:
        return f"O número {numero} é negativo"
    else:
        return f"O número {numero} não é negativo"

def neutro(numero):
    if numero == 0:
        return f"O número {numero} é neutro"
    else:
        return f"O número {numero} não é neutro"

numero = int(input("Digite um número: "))

print(positivo(numero))
print(negativo(numero))
print(neutro(numero))

