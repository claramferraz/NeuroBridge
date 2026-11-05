# CAMADA 1: entrada, strings, condições, conversão e cálculo.
# Demonstração isolada: nenhum dado é salvo.
print("NeuroBridge - primeiros passos")
print("Use um apelido fictício. Não informe diagnóstico ou dados de saúde.")
apelido = input("Apelido: ").strip()
while apelido == "":
    apelido = input("Digite um apelido fictício: ").strip()

print("1 - Resumo primeiro")
print("2 - Exemplo primeiro")
print("3 - Depende da atividade")
escolha = input("Como prefere começar? ").strip()
while escolha not in ["1", "2", "3"]:
    escolha = input("Escolha 1, 2 ou 3: ").strip()

# Só convertemos depois de validar a entrada.
numero = int(escolha)
if numero == 1:
    apoio = "Oferecer uma ideia central curta."
elif numero == 2:
    apoio = "Oferecer um exemplo concreto antes da explicação."
else:
    apoio = "Perguntar a preferência para a atividade do dia."

print("Perfil fictício:", apelido)
print("Sugestão para o professor:", apoio)
# Cálculo ilustrativo: não é um resultado de pesquisa.
total_ficticio = 4
escolheram_exemplo = 3
percentual = escolheram_exemplo / total_ficticio * 100
print("Exemplo de cálculo: 3 entre 4 perfis fictícios =", percentual, "%")
print("Preferência não mede capacidade nem comprova aprendizado.")
