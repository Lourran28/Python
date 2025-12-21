def postivo(num):
    if num > 0:
        return f"O numero {num} é positivo"
    else: 
        return f"O numero {num} é negativo"

def negativo(num):
    if num < 0:
        return f"O numero {num} é negativo"
    else:
        return f"o numero {num} nao e negativo"

def neutro(num):
    if num == 0:
        return f"O numero {num} é neutro"
    else:
        return f"o numero {num} nao e neutro"

num = int(input("digite seu numero: "))

print(postivo(num))
print(negativo(num))
print(neutro(num))