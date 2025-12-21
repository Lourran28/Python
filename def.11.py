def somaImposto(taxaImposto, custo):
    custo_final = custo + (custo * (taxaImposto / 100))
    return custo_final

taxa = float(input("Digite a taxa de imposto (%): "))
custo = float(input("Digite o valor do produto: "))

valor_final = somaImposto(taxa, custo)
print(f"O valor final com imposto é: R$ {valor_final:.2f}")