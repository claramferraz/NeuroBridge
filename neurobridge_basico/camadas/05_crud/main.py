# CAMADA 5: aplicação completa no terminal, sem bibliotecas ou funções próprias.
# Matriz de registros: [id, apelido, formato, início, ritmo, atividade,
#                      avaliação, participação, compartilhar].
# Nas colunas 2 a 7 guardamos o índice da opção escolhida.
# A última coluna guarda "s" ou "n". É uma simulação, não controle de acesso.

perguntas = [
    "Formato principal para esta atividade",
    "Como prefere começar",
    "Ritmo da explicação",
    "Atividade de estudo",
    "Apresentação da avaliação",
    "Forma de participação",
]
opcoes = [
    ["Sem preferência", "Texto", "Números", "Símbolos com legenda", "Imagem com descrição", "Áudio com transcrição", "Texto e imagem"],
    ["Sem preferência", "Resumo primeiro", "Exemplo primeiro", "Passo a passo", "Depende da atividade"],
    ["Sem preferência", "Uma instrução por vez", "Blocos curtos", "Pausas entre etapas", "Aprofundar por escolha"],
    ["Sem preferência", "Exemplo resolvido", "Exercício guiado", "Tentar antes da explicação", "Atividade interativa"],
    ["Sem preferência", "Enunciado em partes", "Uma questão por vez", "Dados e sinais destacados", "Espaço para raciocínio"],
    ["Sem preferência", "Individual", "Dupla ou grupo", "Alternar", "Depende da atividade"],
]
# Mesma posição da matriz de opções = sugestão correspondente.
# São possibilidades para revisão humana, não regras clínicas.
apoios = [
    ["Perguntar quais formatos ajudam hoje.", "Oferecer texto claro e organizado.", "Usar números quando fizerem sentido para o conteúdo.", "Explicar cada símbolo com uma legenda.", "Oferecer esquema simples acompanhado de descrição.", "Oferecer áudio com transcrição, sem reprodução automática.", "Combinar texto curto com imagem explicada."],
    ["Oferecer alternativas de abertura.", "Apresentar a ideia central em poucas frases.", "Apresentar um exemplo concreto antes da regra.", "Explicar uma etapa por vez.", "Combinar a abertura para esta atividade."],
    ["Combinar o ritmo com a turma.", "Dar uma instrução por vez.", "Dividir a explicação em blocos curtos.", "Combinar pausas entre etapas.", "Deixar detalhes disponíveis por escolha."],
    ["Oferecer opções de atividade.", "Mostrar um exemplo resolvido e explicar as etapas.", "Oferecer um exercício com orientações graduais.", "Permitir uma tentativa antes da explicação.", "Oferecer interação opcional com instruções claras."],
    ["Conversar sobre a apresentação do enunciado.", "Dividir o enunciado em partes claras.", "Apresentar uma questão por vez.", "Destacar dados e sinais sem revelar a resposta.", "Oferecer espaço para explicar o raciocínio."],
    ["Oferecer alternativas de participação.", "Oferecer um momento individual.", "Oferecer trabalho em dupla ou grupo.", "Alternar momento individual e troca em grupo.", "Combinar a participação para esta atividade."],
]
registros = []
proximo_id = 1
acao = ""
print("NEUROBRIDGE - demonstração de preferências")
print("Use somente apelidos e respostas fictícios. Não informe diagnóstico ou saúde.")
print("As respostas ficam apenas na memória e são apagadas ao sair.")
print("Quem acessar este terminal poderá consultar, editar e excluir registros.")
print("A escolha de compartilhar afeta somente o resumo simulado do professor.")
print("Não há login, link público, envio à IA ou proteção para uso com dados reais.")

while acao != "0":
    print("\n1 - Criar | 2 - Consultar | 3 - Editar | 4 - Excluir | 5 - Professor | 0 - Sair")
    acao = input("Ação: ").strip()

    # C e U: criar e atualizar usam as mesmas perguntas.
    if acao == "1" or acao == "3":
        posicao = -1
        if acao == "3":
            identificador = input("ID a editar (ou Enter para cancelar): ").strip()
            for indice, registro in enumerate(registros):
                if str(registro[0]) == identificador:
                    posicao = indice
            if posicao == -1:
                print("ID não encontrado. Nada foi alterado.")
        if acao == "1" or posicao != -1:
            apelido = input("Apelido fictício (1 a 30 caracteres): ").strip()
            while apelido == "" or len(apelido) > 30:
                apelido = input("Use entre 1 e 30 caracteres: ").strip()
            if acao == "1":
                linha = [proximo_id, apelido]
            else:
                linha = [registros[posicao][0], apelido]
            print("Escolha UMA opção principal por pergunta. Use 0 para não definir.")
            for campo in range(len(perguntas)):
                print("\n" + perguntas[campo])
                validas = []
                for numero, opcao in enumerate(opcoes[campo]):
                    print(numero, "-", opcao)
                    validas.append(str(numero))
                escolha = input("Opção: ").strip()
                while escolha not in validas:
                    escolha = input("Número inválido. Escolha uma opção da lista: ").strip()
                linha.append(int(escolha))
            compartilhar = input("Incluir no resumo simulado do professor? (s/n): ").strip().lower()
            while compartilhar not in ["s", "n"]:
                compartilhar = input("Digite s ou n: ").strip().lower()
            linha.append(compartilhar)
            print("Resumo antes de salvar:", linha[1])
            for campo in range(len(perguntas)):
                print(perguntas[campo], ":", opcoes[campo][linha[campo + 2]])
            print("Incluir no resumo:", compartilhar)
            confirmar = input("Salvar? Digite s; outra resposta cancela: ").strip().lower()
            if confirmar == "s":
                if acao == "1":
                    registros.append(linha)
                    proximo_id = proximo_id + 1
                    print("Registro criado. ID:", linha[0])
                else:
                    registros[posicao] = linha
                    print("Registro atualizado; ID preservado.")
            else:
                print("Operação cancelada. Nada foi salvo.")

    # R: consultar todos os registros da demonstração.
    elif acao == "2":
        if len(registros) == 0:
            print("Nenhum registro cadastrado.")
        for registro in registros:
            print("\nID:", registro[0], "| Apelido:", registro[1])
            for campo in range(len(perguntas)):
                print(perguntas[campo], ":", opcoes[campo][registro[campo + 2]])
            print("Incluir no resumo do professor:", registro[8])

    # D: excluir pelo ID, com confirmação.
    elif acao == "4":
        identificador = input("ID a excluir: ").strip()
        posicao = -1
        for indice, registro in enumerate(registros):
            if str(registro[0]) == identificador:
                posicao = indice
        if posicao == -1:
            print("ID não encontrado.")
        else:
            print("Excluir:", registros[posicao][1])
            confirmar = input("Digite s para confirmar: ").strip().lower()
            if confirmar == "s":
                registros.pop(posicao)
                print("Registro excluído.")
            else:
                print("Exclusão cancelada.")

    elif acao == "5":
        # Só os registros marcados com s entram nas contagens.
        selecionados = []
        for registro in registros:
            if registro[8] == "s":
                selecionados.append(registro)
        total = len(selecionados)
        if total == 0:
            print("Nenhum registro marcado para o resumo.")
        else:
            tema = input("Tema fictício da aula: ").strip()
            objetivo = input("Objetivo de aprendizagem: ").strip()
            if tema == "" or objetivo == "":
                print("Preencha tema e objetivo para gerar o resumo.")
            else:
                contagens = []
                for campo in range(len(perguntas)):
                    linha_contagem = []
                    for numero in range(len(opcoes[campo])):
                        linha_contagem.append(0)
                    contagens.append(linha_contagem)
                for registro in selecionados:
                    for campo in range(len(perguntas)):
                        numero = registro[campo + 2]
                        contagens[campo][numero] = contagens[campo][numero] + 1
                print("\nTema:", tema, "| Objetivo:", objetivo)
                print("Base:", total, "registros fictícios marcados para compartilhar.")
                print("Cada registro tem uma escolha por pergunta, incluindo Sem preferência.")
                for campo in range(len(perguntas)):
                    print("\n" + perguntas[campo])
                    acumulador = 0
                    for numero in range(len(opcoes[campo])):
                        quantidade = contagens[campo][numero]
                        acumulador = acumulador + quantidade
                        if quantidade > 0:
                            percentual = quantidade / total * 100
                            print(opcoes[campo][numero], ":", quantidade, "de", total, "(", round(percentual, 1), "%)")
                            print("Possibilidade:", apoios[campo][numero])
                    print("Total conferido nesta pergunta:", acumulador)
                print("\nUse as sugestões como ALTERNATIVAS; não aplique todas por obrigação.")
                print("A maioria não elimina apoios escolhidos por uma minoria.")
                print("Nas avaliações, preserve o objetivo, a dificuldade e os critérios.")
                print("O professor decide os apoios pertinentes e valida com os estudantes.")
                print("Preferências declaradas não comprovam eficácia e podem mudar.")
    elif acao != "0":
        print("Ação inválida. Escolha uma opção do menu.")

print("Programa encerrado. Os registros desta sessão não foram salvos.")
