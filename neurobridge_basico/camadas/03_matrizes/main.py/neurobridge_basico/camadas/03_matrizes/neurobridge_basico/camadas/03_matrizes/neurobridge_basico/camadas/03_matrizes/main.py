# CAMADA 3: matriz, for/range, contadores, acumulador e porcentagem.
# Dados inteiramente fictícios. Colunas: apelido, código de abertura.
aberturas = ["Sem preferência", "Resumo", "Exemplo", "Passo a passo"]
perfis = [["Exemplo A", 2], ["Exemplo B", 1], ["Exemplo C", 2], ["Exemplo D", 0]]
contagens = [0, 0, 0, 0]

for linha in range(len(perfis)):
 codigo = perfis[linha][1]
 contagens[codigo] = contagens[codigo] + 1

total = len(perfis)
acumulador = 0
print("Base fictícia:", total, "registros; uma escolha por registro.")
for indice in range(len(aberturas)):
 acumulador = acumulador + contagens[indice]
    if total > 0:
 percentual = contagens[indice] / total * 100
        print(aberturas[indice], ":", contagens[indice], "de", total, "=", percentual, "%")
print("Total conferido pelo acumulador:", acumulador)
print("Contagem descreve escolhas. Não classifica capacidade ou diagnóstico.")
print("O professor pode oferecer alternativas; a maioria não elimina as outras escolhas.")
