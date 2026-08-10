def somaImposto(taxaImposto, custo):
    # Calcula o valor final incluindo o imposto
    custo_final = custo + (custo * (taxaImposto / 100))
    return custo_final

# Programa principal
taxa = float(input("Digite a taxa de imposto (%): "))
valor_produto = float(input("Digite o valor do produto: "))

valor_final = somaImposto(taxa, valor_produto)

print(f"O valor final com imposto é: R$ {valor_final:.2f}")


