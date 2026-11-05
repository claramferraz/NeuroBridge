# NeuroBridge: preferências para aulas e avaliações.
# Aplicação local: formulário, gestão de cadastros e relatórios pedagógicos.
# Cada linha da matriz registros representa um formulário.
# Colunas: 0 código, 1 apelido, 2 turma, 3 perfil opcional, 4 compartilhamento.
# A partir da coluna 5 ficam as respostas; a última coluna é a observação.
# Uma resposta -1 significa pergunta não aplicada; 0 é uma resposta válida.

perguntas = [
    "Qual formato ajuda nesta atividade?",
    "Como prefere começar a explicação?",
    "Que atividade deseja experimentar?",
    "Como prefere acompanhar o ritmo?",
    "Como prefere participar?",
    "O que ajuda no ambiente?",
    "Existe uma barreira de leitura ou números a apoiar agora?",
    "Que apoio de leitura deseja experimentar?",
    "Que apoio com números deseja experimentar?",
    "Como prefere receber o enunciado da avaliação?",
    "Como prefere demonstrar o que aprendeu?",
    "O que deseja conversar sobre o tempo da avaliação?",
    "Como prefere receber a devolutiva?",
    "Como foi a experiência com os apoios escolhidos?",
]

# A posição da opção será guardada como número na matriz de registros.
opcoes = [
    ["Sem preferência", "Texto curto", "Números e relações", "Símbolos com legenda", "Imagens com descrição", "Combinação de formatos"],
    ["Sem preferência", "Exemplo resolvido primeiro", "Regra seguida de exemplo", "Tentar e depois comparar", "Resumo antes dos detalhes"],
    ["Sem preferência", "Exercício guiado", "Situação prática", "Atividade lúdica", "Investigação e desafio", "Exemplos variados"],
    ["Sem preferência", "Uma etapa por vez", "Blocos com pausas", "Aprofundamento opcional", "Aviso antes de trocar de tarefa"],
    ["Sem preferência", "Individual", "Dupla ou grupo", "Alternar individual e coletivo"],
    ["Sem preferência", "Menos ruído", "Menos estímulos visuais", "Menos ruído e estímulos", "Pausas para movimento"],
    ["Não quero informar", "Nenhuma declarada", "Leitura", "Números", "Leitura e números"],
    ["Sem preferência", "Frases curtas", "Texto mais espaçado", "Leitura acompanhada"],
    ["Sem preferência", "Números alinhados", "Sinais destacados", "Rascunho por etapas"],
    ["Sem preferência", "Enunciado em partes", "Uma questão por vez", "Dados e sinais destacados", "Leitura mediada"],
    ["Sem preferência", "Resposta escrita", "Resposta oral", "Demonstração prática", "Resposta mista"],
    ["Sem preferência", "Tempo para revisar", "Pausas combinadas", "Conversar sobre tempo adicional"],
    ["Sem preferência", "Correção com exemplos", "Devolutiva escrita", "Conversa individual", "Critérios comentados"],
    ["Ainda não testei", "Ajudou", "Não percebi diferença", "Atrapalhou"],
]
perfis = ["Não informado", "TDAH", "Autismo", "Dislexia", "Discalculia", "Altas habilidades/superdotação"]
compartilhamentos = ["Não incluir nos relatórios", "Somente resumo da turma", "Resumo da turma e ficha individual"]
INICIO_RESPOSTAS = 5
COLUNA_OBSERVACAO = INICIO_RESPOSTAS + len(perguntas)
registros = []
proximo_id = 1

# A mesma posição em opcoes e apoios liga a resposta à sugestão.
# Não há relação automática entre um diagnóstico e um método de aula.
apoios = [
    ["Combinar formatos com o estudante.", "Oferecer texto curto e organizado.", "Relacionar quantidades e exemplos quando o conteúdo permitir.", "Usar símbolos acompanhados de legenda; não presumir significado universal.", "Usar imagens simples acompanhadas de descrição.", "Combinar representações e explicar a ligação entre elas."],
    ["Oferecer diferentes formas de começar.", "Mostrar um exemplo resolvido antes de apresentar a regra.", "Apresentar a regra e aplicar em um exemplo.", "Permitir tentativa inicial e depois comparar o raciocínio.", "Começar pela ideia principal e depois detalhar."],
    ["Combinar uma atividade pertinente ao objetivo.", "Oferecer exercício com orientações graduais.", "Usar uma situação prática ligada ao conteúdo.", "Oferecer jogo ou atividade lúdica com alternativa sem competição.", "Oferecer desafio opcional sem presumir desempenho superior.", "Comparar exemplos diferentes e explicitar a regra em comum."],
    ["Combinar o ritmo durante a atividade.", "Apresentar uma instrução por vez.", "Dividir a explicação em blocos e combinar pausas.", "Disponibilizar aprofundamento por escolha.", "Avisar antes das mudanças de tarefa e combinar a transição."],
    ["Oferecer alternativas de participação.", "Disponibilizar atividade individual quando compatível com o objetivo.", "Oferecer dupla ou grupo com papéis claros.", "Alternar reflexão individual e troca com colegas."],
    ["Perguntar se algum ajuste de ambiente ajuda.", "Reduzir ruído evitável.", "Reduzir elementos visuais dispensáveis.", "Reduzir ruído e estímulos visuais dispensáveis.", "Combinar oportunidades de movimento e retorno à tarefa."],
    ["Não inferir ausência de barreiras a partir da não resposta.", "Confirmar se os apoios atuais continuam adequados.", "Conversar sobre a barreira de leitura relatada.", "Conversar sobre a barreira com números relatada.", "Conversar separadamente sobre leitura e números."],
    ["Combinar um apoio de leitura.", "Organizar frases curtas sem retirar informação necessária.", "Separar blocos de texto e manter espaçamento legível.", "Oferecer leitura acompanhada quando a leitura autônoma não for o objetivo avaliado."],
    ["Combinar um apoio para trabalhar com números.", "Alinhar números e reservar espaço para as operações.", "Distinguir os sinais sem indicar qual operação resolve a questão.", "Reservar rascunho para registrar as etapas do raciocínio."],
    ["Conversar sobre a apresentação do enunciado.", "Dividir o enunciado sem retirar dados ou revelar a solução.", "Apresentar uma questão por vez e permitir revisão quando cabível.", "Destacar dados e sinais sem resolver a seleção exigida pela tarefa.", "Considerar leitura mediada somente quando não substituir a competência avaliada."],
    ["Combinar uma forma de demonstrar a competência.", "Oferecer resposta escrita com espaço para o raciocínio.", "Considerar resposta oral se a escrita não for parte essencial do objetivo.", "Considerar demonstração prática se ela produzir evidência da mesma competência.", "Combinar formas de resposta com critérios equivalentes e explícitos."],
    ["Combinar a organização do tempo.", "Reservar oportunidade para revisão.", "Combinar pausas e explicar como o tempo será contado.", "Registrar o pedido e verificar com o professor e o apoio institucional; o programa não concede tempo adicional."],
    ["Combinar a forma da devolutiva.", "Usar exemplos na correção após a avaliação.", "Oferecer comentários escritos claros.", "Oferecer conversa individual sobre os resultados.", "Explicar os critérios e comentar as evidências do trabalho."],
    ["Experimentar o apoio e colher um retorno depois.", "Manter provisoriamente e verificar a aprendizagem com evidências.", "Rever a estratégia com o estudante; o relato não mede aprendizagem.", "Rever ou suspender o apoio que atrapalhou e combinar outra opção."],
]

print("NEUROBRIDGE | Formulário de preferências pedagógicas")
print("Demonstração local: use apelidos e informações fictícias.")
print("As respostas ficam na memória e serão perdidas ao encerrar.")
print("Não há login: quem usa este terminal pode operar todos os registros.")
print("Compartilhar controla apenas os relatórios desta demonstração.")
print("Não há diagnóstico, conexão com IA ou envio automático ao professor.")

acao = ""
while acao != "0":
    print("\n1 Cadastrar | 2 Consultar | 3 Atualizar | 4 Excluir | 5 Ficha individual | 6 Relatório da turma | 0 Sair")
    acao = input("Ação: ").strip()

    # Formulário: criar ou atualizar um cadastro, com revisão antes de salvar.
    if acao == "1" or acao == "3":
        posicao = -1
        if acao == "3":

            codigo = input("Código do registro (ex.: NB-11; Enter cancela): ").strip().upper()
            posicao = -1
            # Fatiamento remove o prefixo; a comparação checa a simetria do código.
            parte_numerica = codigo[3:]
            if codigo[:3] == "NB-" and parte_numerica != "" and parte_numerica == parte_numerica[::-1]:
                for indice, registro in enumerate(registros):
                    if registro[0] == codigo:
                        posicao = indice
            if posicao == -1:
                print("Código não encontrado. Nenhum registro alterado.")
        if acao == "1" or posicao != -1:

            if acao == "1":
                base_codigo = str(proximo_id)
                # Parte numérica palíndroma: 12 + 21 = NB-1221.
                # Serve para referência e checagem simples, nunca como senha.
                codigo = "NB-" + base_codigo + base_codigo[::-1]
                linha = [codigo, "", "", "Não informado", 0]
                for campo in range(len(perguntas)):
                    linha.append(0)
                linha.append("")
            else:
                linha = registros[posicao][:]

            apelido = input("Apelido fictício (1 a 30; Enter mantém na edição): ").strip()
            if acao == "3" and apelido == "":
                apelido = linha[1]
            while apelido == "" or len(apelido) > 30:
                apelido = input("Informe de 1 a 30 caracteres: ").strip()
            linha[1] = apelido

            turma = input("Turma (1 a 20; Enter mantém na edição): ").strip().upper()
            if acao == "3" and turma == "":
                turma = linha[2]
            while turma == "" or len(turma) > 20:
                turma = input("Informe uma turma de 1 a 20 caracteres: ").strip().upper()
            linha[2] = turma

            print("\nPerfil declarado é opcional e não define as sugestões.")
            print("Pode marcar vários, separados por vírgula. Não informe laudos.")
            for numero, perfil in enumerate(perfis):
                print(numero, "-", perfil)
            print("Na edição: Enter mantém; 0 remove a informação anterior.")
            entrada = input("Perfis (Enter para não informar no cadastro): ").strip()
            perfil_valido = False
            while not perfil_valido:
                if entrada == "" and acao == "3":
                    perfil_valido = True
                elif entrada == "" or entrada == "0":
                    linha[3] = "Não informado"
                    perfil_valido = True
                else:
                    escolhidos = []
                    perfil_valido = True
                    for item in entrada.split(","):
                        item = item.strip()
                        if item not in ["1", "2", "3", "4", "5"]:
                            perfil_valido = False
                        elif perfis[int(item)] not in escolhidos:
                            escolhidos.append(perfis[int(item)])
                    if perfil_valido:
                        linha[3] = ", ".join(escolhidos)
                    else:
                        entrada = input("Use 0 sozinho ou opções de 1 a 5 separadas por vírgula: ").strip()

            print("\nUma opção principal por pergunta, referente ao momento atual.")
            print("Na edição, Enter mantém a resposta mostrada.")
            for campo in range(len(perguntas)):
                aplicada = True
                barreira = linha[INICIO_RESPOSTAS + 6]
                if campo == 7 and barreira not in [2, 4]:
                    aplicada = False
                elif campo == 8 and barreira not in [3, 4]:
                    aplicada = False

                if not aplicada:
                    # Apagar a resposta antiga evita um apoio desatualizado.
                    linha[INICIO_RESPOSTAS + campo] = -1
                else:
                    print("\n" + perguntas[campo])
                    validas = []
                    for numero, opcao in enumerate(opcoes[campo]):
                        print(numero, "-", opcao)
                        validas.append(str(numero))
                    anterior = linha[INICIO_RESPOSTAS + campo]
                    if acao == "3" and campo == 13:
                        if linha[5:18] != registros[posicao][5:18]:
                            anterior = 0
                            print("As preferências mudaram. O retorno anterior foi reiniciado.")
                    if acao == "3" and anterior >= 0:
                        print("Atual:", opcoes[campo][anterior])
                    escolha = input("Opção: ").strip()
                    if acao == "3" and escolha == "" and anterior >= 0:
                        escolha = str(anterior)
                    while escolha not in validas:
                        escolha = input("Escolha um dos números apresentados: ").strip()
                        if acao == "3" and escolha == "" and anterior >= 0:
                            escolha = str(anterior)
                    linha[INICIO_RESPOSTAS + campo] = int(escolha)

            observacao = input("Observação pedagógica opcional (até 240; '-' apaga; Enter mantém na edição): ").strip()
            while len(observacao) > 240:
                observacao = input("Use no máximo 240 caracteres: ").strip()
            if observacao == "-":
                observacao = ""
            elif acao == "3" and observacao == "":
                observacao = linha[COLUNA_OBSERVACAO]
            linha[COLUNA_OBSERVACAO] = observacao

            for numero, texto in enumerate(compartilhamentos):
                print(numero, "-", texto)
            if acao == "3":
                print("Atual:", compartilhamentos[linha[4]])
            compartilhar = input("Uso no relatório (Enter mantém na edição): ").strip()
            if acao == "3" and compartilhar == "":
                compartilhar = str(linha[4])
            while compartilhar not in ["0", "1", "2"]:
                compartilhar = input("Escolha 0, 1 ou 2: ").strip()
            linha[4] = int(compartilhar)

            print("\nREVISÃO |", linha[0], "|", linha[1], "| Turma:", linha[2])
            print("Perfil opcional:", linha[3])
            for campo in range(len(perguntas)):
                resposta = linha[INICIO_RESPOSTAS + campo]
                if resposta >= 0:
                    print(perguntas[campo], opcoes[campo][resposta])
            print("Observação:", linha[COLUNA_OBSERVACAO])
            print("Compartilhamento:", compartilhamentos[linha[4]])
            confirmar = input("Salvar estas respostas? (s para salvar): ").strip().lower()
            if confirmar == "s":
                if acao == "1":
                    registros.append(linha)
                    proximo_id = proximo_id + 1
                    print("Cadastro criado. Código:", linha[0])
                else:
                    registros[posicao] = linha
                    print("Cadastro atualizado. Código preservado:", linha[0])
            else:
                print("Operação cancelada. Os registros não foram alterados.")

    # Consulta dos cadastros da demonstração.
    elif acao == "2":
        busca = input("Buscar apelido, turma ou código (Enter lista todos): ").strip().lower()
        encontrados = 0
        for registro in registros:
            if busca == "" or busca in registro[1].lower() or busca in registro[2].lower() or busca in registro[0].lower():
                encontrados = encontrados + 1
                print("\n", registro[0], "|", registro[1], "| Turma:", registro[2])
                print("Perfil opcional:", registro[3])
                for campo in range(len(perguntas)):
                    resposta = registro[INICIO_RESPOSTAS + campo]
                    if resposta >= 0:
                        print(perguntas[campo], opcoes[campo][resposta])
                print("Observação:", registro[COLUNA_OBSERVACAO])
                print("Uso nos relatórios:", compartilhamentos[registro[4]])
        print("Registros encontrados:", encontrados)

    # Exclusão de um cadastro após confirmação.
    elif acao == "4":

        codigo = input("Código do registro (ex.: NB-11; Enter cancela): ").strip().upper()
        posicao = -1
        # Fatiamento remove o prefixo; a comparação checa a simetria do código.
        parte_numerica = codigo[3:]
        if codigo[:3] == "NB-" and parte_numerica != "" and parte_numerica == parte_numerica[::-1]:
            for indice, registro in enumerate(registros):
                if registro[0] == codigo:
                    posicao = indice
        if posicao == -1:
            print("Código não encontrado. Nenhum registro alterado.")

        if posicao != -1:
            print("Excluir:", registros[posicao][0], registros[posicao][1])
            confirmar = input("Digite EXCLUIR para confirmar: ").strip().upper()
            if confirmar == "EXCLUIR":
                registros.pop(posicao)
                print("Registro excluído. Ele não aparecerá nos próximos relatórios.")
            else:
                print("Exclusão cancelada.")

    # Sugestões individuais autorizadas para o professor.
    elif acao == "5":

        codigo = input("Código do registro (ex.: NB-11; Enter cancela): ").strip().upper()
        posicao = -1
        # Fatiamento remove o prefixo; a comparação checa a simetria do código.
        parte_numerica = codigo[3:]
        if codigo[:3] == "NB-" and parte_numerica != "" and parte_numerica == parte_numerica[::-1]:
            for indice, registro in enumerate(registros):
                if registro[0] == codigo:
                    posicao = indice
        if posicao == -1:
            print("Código não encontrado. Nenhum registro alterado.")

        if posicao != -1:
            registro = registros[posicao]
            if registro[4] != 2:
                print("Ficha individual não autorizada para este registro.")
            else:
                print("\nFICHA PARA O PROFESSOR |", registro[0], registro[1], "|", registro[2])
                print("Perfil declarado opcional:", registro[3])
                print("Este perfil não é usado para escolher métodos ou medir capacidade.")
                for campo in range(len(perguntas)):
                    resposta = registro[INICIO_RESPOSTAS + campo]
                    if resposta >= 0:
                        print("\nPreferência:", opcoes[campo][resposta])
                        print("Sugestão:", apoios[campo][resposta])
                print("Observação do estudante:", registro[COLUNA_OBSERVACAO])
                print("Avaliação: preservar a competência, o desafio e os critérios.")
                print("Rever os apoios com o estudante; preferências podem mudar.")

    # Visão da turma, avaliação e organização do tempo da aula.
    elif acao == "6":
        turmas = []
        for registro in registros:
            if registro[4] > 0 and registro[2] not in turmas:
                turmas.append(registro[2])
        turmas.sort()
        if len(turmas) == 0:
            print("Nenhum formulário autorizado para o relatório da turma.")
        else:
            print("Turmas com respostas autorizadas:", ", ".join(turmas))
            turma = input("Turma do relatório: ").strip().upper()
            selecionados = []
            for registro in registros:
                if registro[2] == turma and registro[4] > 0:
                    selecionados.append(registro)
            total = len(selecionados)
            if total == 0:
                print("Esta turma não possui formulários autorizados.")
            else:
                tema = input("Tema da aula ou avaliação (1 a 120 caracteres): ").strip()
                while tema == "" or len(tema) > 120:
                    tema = input("Informe um tema de 1 a 120 caracteres: ").strip()
                objetivo = input("Qual competência o aluno deverá demonstrar? (1 a 200): ").strip()
                while objetivo == "" or len(objetivo) > 200:
                    objetivo = input("Informe um objetivo de 1 a 200 caracteres: ").strip()

                print("\nRELATÓRIO DA TURMA", turma)
                print("Tema:", tema, "| Objetivo:", objetivo)
                print("Base:", total, "formulários autorizados nesta turma.")
                print("Não representa alunos ausentes nem garante pessoas únicas.")
                print("Cada pergunta tem uma escolha; perguntas extras podem não se aplicar.")

                contagens = []
                for campo in range(len(perguntas)):
                    contagem = []
                    for numero in range(len(opcoes[campo])):
                        contagem.append(0)
                    contagens.append(contagem)
                for registro in selecionados:
                    for campo in range(len(perguntas)):
                        resposta = registro[INICIO_RESPOSTAS + campo]
                        if resposta >= 0:
                            contagens[campo][resposta] = contagens[campo][resposta] + 1

                for campo in range(len(perguntas)):
                    respondentes = 0
                    for quantidade in contagens[campo]:
                        respondentes = respondentes + quantidade
                    print("\n" + perguntas[campo])
                    print("Base desta pergunta:", respondentes, "| Não aplicada:", total - respondentes)
                    if respondentes == 0:
                        print("Sem respostas aplicáveis; nenhum percentual calculado.")
                    else:
                        for numero, quantidade in enumerate(contagens[campo]):
                            if quantidade > 0:
                                percentual = quantidade / respondentes * 100
                                print(f"{opcoes[campo][numero]}: {quantidade}/{respondentes} ({percentual:.1f}%)")
                                print("Possibilidade:", apoios[campo][numero])

                print("\nPLANEJAMENTO DA AVALIAÇÃO")
                print("1. Conferir se cada forma de resposta evidencia o objetivo informado.")
                print("2. Usar critérios equivalentes e explicar esses critérios antes da tarefa.")
                print("3. Rever apoios que possam revelar a resposta ou substituir a habilidade avaliada.")
                print("4. Conversar sobre pausas, tempo e recursos com os responsáveis pela avaliação.")
                print("5. Oferecer alternativas também às minorias; maioria não decide necessidades individuais.")
                print("6. Após a experiência, editar o formulário e registrar o que ajudou ou atrapalhou.")

                print("\nROTEIRO INICIAL DA AULA")
                print("A duração de cada bloco será uma escolha do professor, sem fórmula por diagnóstico.")
                entrada = input("Minutos da aula (5 a 240; Enter pula o roteiro): ").strip()
                minutos_validos = []
                for numero in range(5, 241):
                    minutos_validos.append(str(numero))
                while entrada != "" and entrada not in minutos_validos:
                    entrada = input("Digite minutos de 5 a 240 ou Enter para pular: ").strip()
                if entrada != "":
                    duracao = int(entrada)
                    etapas = ["Abertura e objetivo", "Explicação com representações", "Prática e participação", "Verificação e devolutiva"]
                    tempos = []
                    restante = duracao
                    for indice in range(len(etapas) - 1):
                        validos = []
                        for minuto in range(restante + 1):
                            validos.append(str(minuto))
                        tempo = input(etapas[indice] + " - minutos (restam " + str(restante) + "): ").strip()
                        while tempo not in validos:
                            tempo = input("Informe de 0 a " + str(restante) + " minutos: ").strip()
                        tempos.append(int(tempo))
                        restante = restante - int(tempo)
                    tempos.append(restante)
                    inicio = 0
                    for indice, etapa in enumerate(etapas):
                        fim = inicio + tempos[indice]
                        print(f"{inicio:02d}-{fim:02d} min | {etapa}")
                        inicio = fim
                    print("Total planejado:", inicio, "minutos.")
                    if min(tempos) == 0:
                        print("Há etapa sem tempo reservado. Reveja se ela é necessária ao objetivo.")
                    print("Maior bloco:", max(tempos), "minutos. Ajuste com a turma durante a aula.")

    elif acao != "0":
        print("Ação inválida. Escolha uma opção do menu.")

print("Programa encerrado. Os registros desta sessão foram descartados.")
