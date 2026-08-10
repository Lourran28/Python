
cidades = []
eleitores = []

def menu():
    while True:
        print("---------------------------")
        print("1. Cadastrar Cidade")
        print("2. Cadastrar Eleitor")
        print("3. Listar Cidades")
        print("4. Listar Eleitores")
        print("5. Buscar Eleitor por Título")
        print("6. Buscar Eleitor por Cidade")
        print("7. Sair")
        print("-----------------------------------")
        
        op = int(input("Digite a opção desejada: "))
        
        if op == 1:
            cadastrar_cidade()
        elif op == 2:
            cadastrar_eleitor()
        elif op == 3:
            listar_cidades()
        elif op == 4:
            listar_eleitores()
        elif op == 5:
            buscar_titulo()
        elif op == 6:
            buscar_cidade()
        elif op == 7:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


def cadastrar_cidade():
    """Cadastra uma nova cidade, gerando um código automático."""
    nome = input("Digite o nome da cidade: ")
    estado = input("Digite o estado da cidade: ")
    codigo = len(cidades) + 1
    
    cidade = {
        "codigo": codigo,
        "nome": nome,
        "estado": estado
    }
    cidades.append(cidade)
    print(f"\nCidade '{nome}' cadastrada! Código: {codigo}")


def cadastrar_eleitor():
    """Cadastra um novo eleitor, associando-o a uma cidade existente."""
    if len(cidades) == 0:
        print("\nErro: Nenhuma cidade cadastrada. Por favor, cadastre uma cidade primeiro.")
        return

    nome = input("Digite o nome do eleitor: ")
    titulo = input("Digite o número do título de eleitor: ")
    
    print("\nCidades cadastradas:")
    listar_cidades()
    
    while True:
        codigo_cidade = int(input("\nDigite o código da cidade do eleitor: "))
        
        cidade_encontrada = None
        for cidade in cidades:
            if cidade['codigo'] == codigo_cidade:
                cidade_encontrada = cidade
                break
        
        if cidade_encontrada:
            eleitor = {
                "nome": nome,
                "titulo": titulo,
                "cidade": cidade_encontrada['nome']
            }
            eleitores.append(eleitor)
            print(f"\nEleitor '{nome}' cadastrado com sucesso!")
            break
        else:
            print("Código de cidade inválido. Por favor, digite um código válido.")


def listar_cidades():
    """Exibe a lista de todas as cidades cadastradas."""
    if len(cidades) == 0:
        print("Nenhuma cidade cadastrada.")
        return
        
    print("\n--- Lista de Cidades ---")
    for cidade in cidades:
        print(f"Código: {cidade['codigo']} | Nome: {cidade['nome']} | Estado: {cidade['estado']}")


def listar_eleitores():
    """Exibe a lista de todos os eleitores cadastrados."""
    if len(eleitores) == 0:
        print("Nenhum eleitor cadastrado.")
        return
        
    print("\n--- Lista de Eleitores ---")
    for eleitor in eleitores:
        print(f"Nome: {eleitor['nome']}, Título de Eleitor: {eleitor['titulo']}, Cidade: {eleitor['cidade']}")


def buscar_titulo():
    """Busca e exibe um eleitor pelo número do título."""
    if len(eleitores) == 0:
        print("\nNenhum eleitor cadastrado para buscar.")
        return
        
    titulo_buscar = input("Digite o título de eleitor para buscar: ")
    encontrado = False
    
    for eleitor in eleitores:
        if eleitor['titulo'] == titulo_buscar:
            print("\n--- Eleitor Encontrado ---")
            print(f"Nome: {eleitor['nome']}, Título de Eleitor: {eleitor['titulo']}, Cidade: {eleitor['cidade']}")
            encontrado = True
            break
            
    if encontrado == False:
        print("\nNenhum eleitor encontrado com este título.")


def buscar_cidade():
    """Busca e exibe eleitores pelo nome de cidade."""
    if len(eleitores) == 0:
        print("\nNenhum eleitor cadastrado para buscar.")
        return
        
    cidade_buscar = input("Digite a cidade para buscar eleitores: ")
    encontrados = False
    
    print(f"\n--- Eleitores de {cidade_buscar} ---")
    for eleitor in eleitores:
        if eleitor['cidade'].lower() == cidade_buscar.lower():
            print(f"Nome: {eleitor['nome']}, Título de Eleitor: {eleitor['titulo']}, Cidade: {eleitor['cidade']}")
            encontrados = True
            
    if encontrados == False: 
        print("Nenhum eleitor encontrado nesta cidade.")



if __name__ == "__main__":
    menu()