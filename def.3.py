def situacao(aluno, nota1, nota2,nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return f"{aluno} aprovado com média {media:.1f}"
    elif media >= 5:
        return f"{aluno} em recuperação com média {media:.1f}"
    else:
        return f"{aluno} reprovado com média {media:.1f}"

for i in range(2):  # quantidade de alunos
    nome = input("Digite o nome do aluno: ")

    while True:
        nota1 = float(input(f"Digite a nota 1 de {nome}: "))
        if 0 <= nota1 <= 10:
            break
        print("Nota inválida! Digite novamente.")

    while True:
        nota2 = float(input(f"Digite a nota 2 de {nome}: "))
        if 0 <= nota2 <= 10:
            break
        print("Nota inválida! Digite novamente.")
    while True:
        nota3 = float(input(f"Digite a nota 3 de {nome}: "))
        if 0 <= nota3 <= 10:
            break
        print("Nota inválida! Digite novamente.")
    print(situacao(nome, nota1, nota2, nota3))
    print("-" * 20)  # separador entre alunos
