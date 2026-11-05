# CAMADA 2: lista, append, remove, len, enumerate e menu com while.
# Cada execução começa com uma lista vazia.
opcoes = ["Texto", "Números", "Símbolos com legenda", "Imagem com descrição"]
escolhidas = []
acao = ""
while acao != "0":
    print("\n1 - Adicionar apoio | 2 - Consultar | 3 - Remover | 0 - Sair")
    acao = input("Ação: ").strip()
    if acao == "1":
        for indice, opcao in enumerate(opcoes):
            print(indice + 1, "-", opcao)
        entrada = input("Número do apoio: ").strip()
        if entrada in ["1", "2", "3", "4"]:
            apoio = opcoes[int(entrada) - 1]
            if apoio not in escolhidas:
                escolhidas.append(apoio)
                print("Apoio adicionado.")
            else:
                print("Essa opção já está na lista.")
        else:
            print("Número inválido.")
    elif acao == "2":
        if len(escolhidas) == 0:
            print("Nenhum apoio selecionado.")
        for indice, apoio in enumerate(escolhidas):
            print(indice + 1, "-", apoio)
    elif acao == "3":
        apoio = input("Digite o nome exato do apoio a remover: ").strip()
        if apoio in escolhidas:
            escolhidas.remove(apoio)
            print("Apoio removido.")
        else:
            print("Esse apoio não está na lista.")
    elif acao != "0":
        print("Ação inválida.")
print("Fim da demonstração. A lista não foi salva em arquivo.")
