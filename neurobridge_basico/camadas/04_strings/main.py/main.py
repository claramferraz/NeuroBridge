# CAMADA 4: exercício isolado de strings, fatiamento e palíndromos.
# Esta atividade NÃO analisa estudantes nem interfere nas sugestões.
texto = input("Digite uma palavra fictícia para o exercício: ").strip().lower()
normalizado = texto.replace(" ", "")
print("Primeiros 12 caracteres:", texto[:12])
print("Texto invertido:", normalizado[::-1])
if normalizado == "":
    print("Entrada vazia: não há palavra para comparar.")
elif normalizado == normalizado[::-1]:
    print("Palíndromo: a sequência é igual quando lida ao contrário.")
else:
    print("Não é palíndromo nesta comparação.")
print("A comparação ignora espaços e maiúsculas, mas mantém acentos e pontuação.")
print("Exemplos: arara e osso. Este exercício não tem significado clínico.")
