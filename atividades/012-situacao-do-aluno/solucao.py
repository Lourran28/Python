def situacao(aluno, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return f'O aluno {aluno} aprovado com média {media:.1f}'
    elif 5 <= media < 7:
        return f'O aluno {aluno} em recuperação com média {media:.1f}'
    else:
        return f'O aluno {aluno} reprovado com média {media:.1f}'

for i in range(1, 3):  # quantidade de alunos
    nome = input("Digite o nome do aluno: ")
    
    while True:
        nota1 = float(input("Digite a primeira nota: "))
        if 0 <= nota1 <= 10:
            break
        print("Nota inválida. Tente novamente.")
    while True: 
        nota2 = float(input("Digite a segunda nota: "))
        if 0 <= nota2 <= 10:
            break
        print("Nota inválida. Tente novamente.")
    while True:
        nota3 = float(input("Digite a terceira nota: "))
        if 0 <= nota3 <= 10:
            break
        print("Nota inválida. Tente novamente.")
    
resultado = situacao(nome, nota1, nota2, nota3)
