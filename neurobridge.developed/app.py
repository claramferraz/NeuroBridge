import streamlit as st

# INTERFACE: o Streamlit fornece os cliques e mantém a sessão.
# LÓGICA: registros são linhas de uma matriz, manipuladas por condições e laços.
st.set_page_config(page_title="NeuroBridge | Preferências", layout="centered")
st.title("NeuroBridge")
st.caption("Preferências para aprender e demonstrar o que você aprendeu.")
st.info("Demonstração sem login. Use apelidos fictícios. Os dados ficam nesta sessão; a transferência para outro navegador é manual.")

# Cada linha: código, apelido, turma, compartilhamento, dez respostas,
# oito recursos codificados como 0/1 em uma string e observação. Total: 16 colunas.
perguntas = [
    "Qual formato principal você gostaria de experimentar nesta aula?",
    "Como prefere interagir?",
    "Que ajuste de estímulos ajuda você?",
    "Como prefere receber as orientações?",
    "Como prefere acessar o conteúdo?",
    "Como prefere mostrar o que aprendeu?",
    "Para quem prefere apresentar o trabalho?",
    "Que tipo de desafio deseja experimentar?",
    "O que ajuda na organização do tempo?",
    "Como foi a experiência com essas preferências?",
]
opcoes = [
    ["Sem preferência", "Exemplos concretos", "Lógica e exemplos matemáticos", "Interação e exercícios", "Lúdica com símbolos explicados"],
    ["Sem preferência", "Resolver exercícios na sala", "Trocar com colegas", "Relacionar outros assuntos", "Alternar formas de interação", "Atividade individual"],
    ["Sem ajuste solicitado", "Menos elementos visuais", "Menos sons", "Menos elementos visuais e sons"],
    ["Sem preferência", "Passos curtos e checklist", "Instruções literais e sequência previsível", "Escolher caminhos para a mesma meta", "Pausas e aviso antes de mudar de tarefa"],
    ["Sem preferência", "Texto simples e espaçado", "Áudio com transcrição", "Imagem ou diagrama com descrição", "Texto ampliado e alto contraste", "Leitor de tela ou material acessível"],
    ["Sem preferência", "Escrita à mão", "Digitação", "Áudio ou conversa", "Imagem, diagrama ou modelo", "Demonstração prática e movimento", "Indicação de símbolos ou CAA"],
    ["Sem preferência", "Professor em particular", "Pequeno grupo", "Turma", "Entregar arquivo sem apresentação"],
    ["Sem preferência", "Mais exemplos e prática", "Etapas orientadas", "Aprofundamento com maior complexidade"],
    ["Sem preferência", "Tempo para revisar", "Pausas combinadas", "Conversar sobre prazo ou tempo adicional"],
    ["Ainda não experimentei", "Ajudou", "Não percebi diferença", "Atrapalhou"],
]
apoios = [
    ["Combinar formas de apresentar o conteúdo.", "Começar por exemplos concretos e explicitar a ideia em comum.", "Usar relações e exemplos matemáticos quando fizerem sentido para o conteúdo.", "Oferecer exercícios, discussão ou conexões com outros assuntos.", "Usar atividades lúdicas e símbolos com legenda, mantendo alternativa sem competição."],
    ["Combinar a participação.", "Resolver exercícios com instruções e devolutiva.", "Organizar troca com colegas com papéis claros.", "Relacionar o conteúdo a outros assuntos sem perder o objetivo.", "Alternar reflexão, exercício e conversa.", "Oferecer participação individual compatível com o objetivo."],
    ["Confirmar se algum ajuste de ambiente é necessário.", "Reduzir elementos visuais dispensáveis.", "Reduzir sons evitáveis e não reproduzir áudio automaticamente.", "Reduzir ruído e estímulos visuais dispensáveis."],
    ["Explicar objetivo, tarefa e critérios.", "Dividir a tarefa em etapas e oferecer checklist de progresso.", "Apresentar sequência previsível e linguagem literal.", "Oferecer escolhas guiadas para alcançar a mesma meta.", "Combinar pausas e avisar antes das transições."],
    ["Oferecer alternativas de acesso.", "Organizar texto legível, com frases claras e espaço entre blocos.", "Disponibilizar áudio acompanhado de transcrição.", "Descrever imagens e explicar símbolos.", "Oferecer ampliação e contraste conforme a preferência relatada.", "Verificar a compatibilidade do material com a tecnologia assistiva usada."],
    ["Combinar uma forma de demonstrar a competência.", "Disponibilizar resposta manuscrita quando adequada.", "Considerar digitação como meio de resposta.", "Considerar resposta oral ou gravada.", "Considerar representação por diagrama, imagem ou modelo com explicação acessível.", "Considerar demonstração prática, movimento ou manipulação, com alternativa acessível.", "Considerar comunicação por indicação de símbolos ou CAA."],
    ["Combinar o contexto de apresentação.", "Oferecer apresentação individual ao professor quando compatível com a meta.", "Oferecer apresentação em pequeno grupo quando compatível.", "Combinar apresentação à turma sem obrigar outros estudantes ao mesmo formato.", "Considerar entrega sem exposição pública quando a apresentação não for a habilidade avaliada."],
    ["Combinar desafio adequado ao objetivo.", "Oferecer exemplos variados e prática com devolutiva.", "Oferecer etapas orientadas com retirada gradual do apoio quando pertinente.", "Oferecer aprofundamento opcional; não substituir por mais tarefas repetitivas nem elevar a exigência mínima individual."],
    ["Explicar a organização do tempo.", "Prever oportunidade para revisão.", "Combinar pausas e esclarecer a contagem do tempo.", "Conversar sobre prazo e verificar os procedimentos da instituição; o sistema não concede tempo adicional."],
    ["Experimentar e colher retorno posteriormente.", "Manter provisoriamente e verificar a aprendizagem com evidências.", "Rever a estratégia com o estudante.", "Rever ou suspender o apoio que atrapalhou e combinar outra opção."],
]
recursos = ["Calculadora ou material de apoio ao cálculo", "Corretor ortográfico ou dicionário", "Ditado por voz", "Teclado, mouse ou apoio motor", "Organizador gráfico", "Leitura em voz ou texto para fala", "Comunicação por símbolos ou CAA", "Ampliação, contraste ou tecnologia assistiva"]
compartilhar = ["Não incluir nos relatórios", "Somente resumo da turma", "Resumo e plano individual"]
habilidades = ["Leitura autônoma", "Escrita ou ortografia", "Cálculo sem ferramentas", "Coordenação motora específica", "Expressão oral perante público"]
cabecalho = "NEUROBRIDGE-DEVELOPED-1"

if "nb_registros" not in st.session_state:
    st.session_state.nb_registros = []
    st.session_state.nb_proximo = 1
    st.session_state.nb_editar = ""
    st.session_state.nb_versao = 0
    st.session_state.nb_aviso = ""
    st.session_state.nb_proxima_area = ""
if st.session_state.nb_proxima_area != "":
    st.session_state.nb_area = st.session_state.nb_proxima_area
    st.session_state.nb_proxima_area = ""
registros = st.session_state.nb_registros
area = st.sidebar.radio("Área da demonstração", ["Formulário do aluno", "Cadastros", "Painel do professor"], key="nb_area")
st.sidebar.caption("Estas áreas não são contas nem permissões de acesso.")
if st.session_state.nb_aviso != "":
    st.success(st.session_state.nb_aviso)
    st.session_state.nb_aviso = ""

# FORMULÁRIO: nenhuma pergunta solicita ou infere diagnóstico.
if area == "Formulário do aluno":
    posicao = -1
    for indice, registro in enumerate(registros):
        if registro[0] == st.session_state.nb_editar:
            posicao = indice
    linha = ["", "", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "00000000", ""]
    if posicao >= 0:
        linha = registros[posicao][:]
        st.subheader("Atualizar minhas preferências")
        st.caption("Código: " + linha[0])
    else:
        st.subheader("Como você prefere aprender hoje?")
    st.write("Você pode escolher o que ajuda nesta atividade e mudar de ideia depois. Não há resposta certa nem classificação de pessoas.")
    formulario = st.form("preferencias_" + str(st.session_state.nb_versao), enter_to_submit=False)
    apelido = formulario.text_input("Apelido fictício", value=linha[1], max_chars=30)
    turma = formulario.text_input("Turma", value=linha[2], max_chars=20)
    respostas = []
    for campo, pergunta in enumerate(perguntas):
        if campo == 0:
            formulario.subheader("A aula e o acesso ao conteúdo")
        elif campo == 5:
            formulario.subheader("Como mostrar o que aprendi")
        elif campo == 9:
            formulario.subheader("Retorno sobre a experiência")
        resposta = formulario.selectbox(pergunta, opcoes[campo], index=linha[campo + 4], key="q_" + str(st.session_state.nb_versao) + "_" + str(campo))
        respostas.append(opcoes[campo].index(resposta))
    padrao_recursos = []
    for numero, recurso in enumerate(recursos):
        if linha[14][numero] == "1":
            padrao_recursos.append(recurso)
    escolhidos = formulario.multiselect("Que recursos gostaria de experimentar? (opcional)", recursos, default=padrao_recursos)
    observacao = formulario.text_area("Algo mais que ajuda você? (opcional, sem dados de saúde)", value=linha[15], max_chars=240)
    permissao = formulario.selectbox("Como suas respostas podem entrar nos relatórios?", compartilhar, index=linha[3])
    formulario.caption("Os recursos são pedidos para análise do professor. O objetivo e os critérios da avaliação continuam comuns à turma.")
    salvar = formulario.form_submit_button("Salvar preferências")
    if salvar:
        apelido = " ".join(apelido.split())
        turma = " ".join(turma.split()).upper()
        duplicado = False
        for indice, registro in enumerate(registros):
            if indice != posicao and registro[1].lower() == apelido.lower() and registro[2] == turma:
                duplicado = True
        if len(apelido) == 0 or len(apelido) > 30 or len(turma) == 0 or len(turma) > 20:
            st.error("Preencha um apelido de 1 a 30 caracteres e uma turma de 1 a 20.")
        elif duplicado:
            st.error("Já existe este apelido na turma. Atualize o cadastro existente ou escolha um apelido distinto.")
        else:
            bits = ""
            for recurso in recursos:
                if recurso in escolhidos:
                    bits = bits + "1"
                else:
                    bits = bits + "0"
            if posicao == -1:
                numero = str(st.session_state.nb_proximo)
                # Código de referência simétrico; não é senha nem anonimização.
                linha[0] = "NB-" + numero + numero[::-1]
            nova = [linha[0], apelido, turma, compartilhar.index(permissao)]
            nova.extend(respostas)
            nova.extend([bits, " ".join(observacao.split())])
            aviso = "Preferências salvas. Código: " + nova[0]
            if posicao >= 0:
                if nova[4:13] != linha[4:13] or nova[14] != linha[14]:
                    nova[13] = 0
                    aviso = aviso + ". Como os apoios mudaram, o retorno foi reiniciado para Ainda não experimentei."
                registros[posicao] = nova
            else:
                registros.append(nova)
                st.session_state.nb_proximo = st.session_state.nb_proximo + 1
            st.session_state.nb_editar = nova[0]
            st.session_state.nb_versao = st.session_state.nb_versao + 1
            st.session_state.nb_aviso = aviso
            st.rerun()
    if posicao >= 0:
        if st.button("Começar outro formulário / sair da edição"):
            st.session_state.nb_editar = ""
            st.session_state.nb_versao = st.session_state.nb_versao + 1
            st.rerun()
        if linha[3] > 0:
            envio = linha[:]
            if envio[3] == 1:
                envio[15] = ""
            campos = []
            for valor in envio:
                campos.append(str(valor).replace("\t", " ").replace("\n", " "))
            pacote = cabecalho + "\n" + "\t".join(campos) + "\n"
            st.download_button("Baixar resposta para entregar ao professor", pacote, file_name="neurobridge_resposta.txt", mime="text/plain")
            st.caption("Envio manual pelo canal combinado. O professor importa o texto na área Cadastros. Apelido e turma vão no arquivo; a observação só vai se o plano individual foi autorizado.")

# CADASTROS: consultar, editar, excluir e receber respostas de outra sessão.
elif area == "Cadastros":
    st.subheader("Cadastros desta sessão")
    busca = st.text_input("Buscar apelido, turma ou código").strip().lower()
    rotulos = []
    posicoes = []
    for indice, registro in enumerate(registros):
        if busca in registro[1].lower() or busca in registro[2].lower() or busca in registro[0].lower():
            rotulos.append(registro[0] + " | " + registro[1][:30] + " | " + registro[2])
            posicoes.append(indice)
    st.write("Formulários encontrados:", len(posicoes))
    if len(posicoes) > 0:
        selecionado = st.selectbox("Cadastro", rotulos)
        posicao = posicoes[rotulos.index(selecionado)]
        registro = registros[posicao]
        st.write("Uso nos relatórios:", compartilhar[registro[3]])
        for campo, pergunta in enumerate(perguntas):
            st.write(pergunta, opcoes[campo][registro[campo + 4]])
        pedidos = []
        for numero, recurso in enumerate(recursos):
            if registro[14][numero] == "1":
                pedidos.append(recurso)
        st.write("Recursos solicitados:", ", ".join(pedidos))
        st.text("Observação: " + registro[15])
        if st.button("Editar cadastro"):
            st.session_state.nb_editar = registro[0]
            st.session_state.nb_versao = st.session_state.nb_versao + 1
            st.session_state.nb_proxima_area = "Formulário do aluno"
            st.rerun()
        confirmar = st.checkbox("Confirmo a exclusão deste cadastro", key="excluir_" + registro[0])
        if st.button("Excluir cadastro", disabled=not confirmar):
            registros.pop(posicao)
            st.session_state.nb_editar = ""
            st.session_state.nb_aviso = "Cadastro excluído. Os próximos relatórios serão recalculados."
            st.rerun()
    if len(registros) == 0 and st.button("Carregar quatro exemplos fictícios"):
        for indice in range(4):
            numero = str(st.session_state.nb_proximo)
            registros.append(["NB-" + numero + numero[::-1], "Exemplo " + str(indice + 1), "DEMO", 2, indice + 1, indice + 1, indice % 4, indice + 1, indice + 1, indice + 2, 1, 1, 0, 0, "00000000", "Dado fictício para demonstração."])
            st.session_state.nb_proximo = st.session_state.nb_proximo + 1
        st.rerun()
    st.subheader("Receber respostas de outro navegador")
    st.caption("Abra o TXT que o aluno entregou, copie seu conteúdo e cole abaixo. A transferência não é automática. Importações repetidas não somam votos duplicados.")
    entrada = st.text_area("Conteúdo do arquivo de respostas", max_chars=60000)
    substituir = st.checkbox("Substituir cadastros com o mesmo apelido e turma")
    if st.button("Validar e importar respostas"):
        linhas = entrada.strip("\n\r").splitlines()
        erros = []
        pendentes = []
        destinos = []
        chaves = []
        if len(linhas) in [0, 1] or linhas[0] != cabecalho or len(linhas) > 101:
            erros.append("Use o arquivo NeuroBridge desta versão, com até 100 respostas.")
        else:
            for numero in range(1, len(linhas)):
                campos = linhas[numero].split("\t")
                valida = len(campos) == 16
                if valida:
                    referencia = campos[0][3:]
                    if campos[0][:3] != "NB-" or referencia == "" or referencia != referencia[::-1]:
                        valida = False
                    campos[1] = " ".join(campos[1].split())
                    campos[2] = " ".join(campos[2].split()).upper()
                    if len(campos[1]) == 0 or len(campos[1]) > 30 or len(campos[2]) == 0 or len(campos[2]) > 20 or len(campos[15]) > 240:
                        valida = False
                    if campos[3] not in ["1", "2"] or len(campos[14]) != len(recursos):
                        valida = False
                    for caractere in campos[14]:
                        if caractere not in "01":
                            valida = False
                    for campo in range(len(perguntas)):
                        validos = []
                        for opcao in range(len(opcoes[campo])):
                            validos.append(str(opcao))
                        if campos[campo + 4] not in validos:
                            valida = False
                if not valida:
                    erros.append("Linha " + str(numero + 1) + " inválida.")
                else:
                    chave = campos[1].lower() + "\t" + campos[2]
                    destino = -1
                    for indice, registro in enumerate(registros):
                        if registro[1].lower() == campos[1].lower() and registro[2] == campos[2]:
                            destino = indice
                    if chave in chaves or (destino >= 0 and not substituir):
                        erros.append("Linha " + str(numero + 1) + ": apelido e turma já cadastrados ou repetidos neste lote.")
                    chaves.append(chave)
                    nova = campos[:]
                    for coluna in range(3, 14):
                        nova[coluna] = int(nova[coluna])
                    if nova[3] == 1:
                        nova[15] = ""
                    pendentes.append(nova)
                    destinos.append(destino)
        if len(erros) != 0:
            st.error("Nada foi importado. " + " ".join(erros[:8]))
        else:
            for indice, nova in enumerate(pendentes):
                destino = destinos[indice]
                if destino >= 0:
                    nova[0] = registros[destino][0]
                    if nova[4:13] != registros[destino][4:13] or nova[14] != registros[destino][14]:
                        nova[13] = 0
                    registros[destino] = nova
                else:
                    numero = str(st.session_state.nb_proximo)
                    nova[0] = "NB-" + numero + numero[::-1]
                    registros.append(nova)
                    st.session_state.nb_proximo = st.session_state.nb_proximo + 1
            st.session_state.nb_aviso = str(len(pendentes)) + " respostas importadas. Códigos locais preservados ou atribuídos."
            st.rerun()

# PROFESSOR: porcentagens, proposta de aula e avaliação individual com critérios comuns.
else:
    st.subheader("Planejar a partir das preferências da turma")
    turmas = []
    for registro in registros:
        if registro[3] > 0 and registro[2] not in turmas:
            turmas.append(registro[2])
    turmas.sort()
    if len(turmas) == 0:
        st.warning("Ainda não há respostas autorizadas. Cadastre ou importe respostas na mesma sessão.")
    else:
        turma = st.selectbox("Turma do planejamento", turmas)
        selecionados = []
        for registro in registros:
            if registro[2] == turma and registro[3] > 0:
                selecionados.append(registro)
        total = len(selecionados)
        st.write("Base:", total, "formulários autorizados desta turma.")
        st.caption("Os percentuais descrevem preferências declaradas. Não medem capacidade nem garantem representação de todos os alunos.")
        contagens = []
        for campo in range(len(perguntas)):
            linha_contagem = []
            for numero in range(len(opcoes[campo])):
                linha_contagem.append(0)
            contagens.append(linha_contagem)
        contagem_recursos = [0] * len(recursos)
        for registro in selecionados:
            for campo in range(len(perguntas)):
                resposta = registro[campo + 4]
                contagens[campo][resposta] = contagens[campo][resposta] + 1
            for numero in range(len(recursos)):
                if registro[14][numero] == "1":
                    contagem_recursos[numero] = contagem_recursos[numero] + 1
        for campo, pergunta in enumerate(perguntas):
            bloco = st.expander(pergunta, expanded=campo == 0 or campo == 2)
            for numero, quantidade in enumerate(contagens[campo]):
                if quantidade > 0:
                    percentual = quantidade / total * 100
                    bloco.write(f"{opcoes[campo][numero]}: {quantidade}/{total} ({percentual:.1f}%)")
                    bloco.caption(apoios[campo][numero])
        bloco = st.expander("Recursos pedidos pela turma")
        bloco.caption("Escolhas múltiplas: estes percentuais podem somar mais de 100%.")
        for numero, quantidade in enumerate(contagem_recursos):
            if quantidade > 0:
                bloco.write(f"{recursos[numero]}: {quantidade}/{total} ({quantidade / total * 100:.1f}%)")

        st.subheader("Proposta de divisão da aula")
        tema = st.text_input("Tema da aula", max_chars=120)
        objetivo = st.text_area("Objetivo de aprendizagem comum", max_chars=400)
        criterios = st.text_area("Critérios de avaliação comuns a todos", max_chars=1000)
        enunciado = st.text_area("Enunciado-base da avaliação (opcional)", max_chars=3000)
        essenciais = st.multiselect("Quais habilidades são parte essencial desta avaliação?", habilidades)
        duracao = st.number_input("Duração total da aula (minutos)", min_value=10, max_value=240, value=50, step=1)
        abertura = st.number_input("Abertura e objetivo (minutos)", min_value=0, max_value=240, value=5, step=1)
        fechamento = st.number_input("Verificação e devolutiva (minutos)", min_value=0, max_value=240, value=5, step=1)
        permitidos = st.multiselect("Formatos compatíveis com este conteúdo", opcoes[0][1:], default=opcoes[0][1:])
        st.caption("Retire matemática quando não fizer sentido para o tema. As necessidades de acesso continuam válidas em todos os blocos.")
        if tema.strip() == "" or objetivo.strip() == "" or criterios.strip() == "":
            st.info("Preencha tema, objetivo e critérios para obter a proposta e os planos individuais.")
        elif abertura + fechamento >= duracao or len(permitidos) == 0:
            st.error("Reserve tempo para os formatos da aula e selecione pelo menos um formato compatível.")
        else:
            disponivel = int(duracao - abertura - fechamento)
            pesos = []
            soma = 0
            for numero in range(1, 5):
                peso = 0
                if opcoes[0][numero] in permitidos:
                    peso = contagens[0][numero]
                pesos.append(peso)
                soma = soma + peso
            sem_preferencia = contagens[0][0]
            fora_da_proposta = total - sem_preferencia - soma
            st.write("Sem preferência:", sem_preferencia, "| Preferências por formatos não selecionados:", fora_da_proposta)
            if soma == 0:
                st.warning("Não há escolhas aplicáveis para distribuir o tempo. A divisão abaixo é equilibrada e provisória, sem fundamento em votos da turma.")
                for indice in range(4):
                    if opcoes[0][indice + 1] in permitidos:
                        pesos[indice] = 1
                        soma = soma + 1
            minutos = []
            restos = []
            usados = 0
            for peso in pesos:
                cota = disponivel * peso / soma
                inteiro = int(cota)
                minutos.append(inteiro)
                restos.append(cota - inteiro)
                usados = usados + inteiro
            faltam = disponivel - usados
            # Distribuir os minutos restantes pelas maiores partes decimais.
            while faltam > 0:
                maior = 0
                for indice in range(1, len(restos)):
                    if restos[indice] > restos[maior]:
                        maior = indice
                minutos[maior] = minutos[maior] + 1
                restos[maior] = -1
                faltam = faltam - 1
            relatorio = "NEUROBRIDGE — PROPOSTA PARA REVISÃO DO PROFESSOR\nTurma: " + turma + "\nTema: " + tema.strip() + "\nObjetivo: " + objetivo.strip() + "\nCritérios comuns: " + criterios.strip() + "\n"
            st.write("Abertura:", int(abertura), "minutos")
            relatorio = relatorio + "\nAbertura: " + str(int(abertura)) + " minutos\n"
            total_planejado = int(abertura) + int(fechamento)
            for indice, tempo in enumerate(minutos):
                total_planejado = total_planejado + tempo
                st.write(opcoes[0][indice + 1] + ":", tempo, "minutos")
                relatorio = relatorio + opcoes[0][indice + 1] + ": " + str(tempo) + " minutos\n"
            st.write("Verificação e devolutiva:", int(fechamento), "minutos")
            st.write("Total:", total_planejado, "minutos")
            st.caption("Proposta inicial, não obrigação. Uma parcela pequena não elimina apoios individuais; o professor pode combinar formatos e rever a duração.")
            relatorio = relatorio + "Verificação e devolutiva: " + str(int(fechamento)) + " minutos\nBase: " + str(total) + " formulários. Sem preferência: " + str(sem_preferencia) + ". Fora dos formatos escolhidos: " + str(fora_da_proposta) + ".\n"
            relatorio = relatorio + "Preservar os apoios de acesso em todos os blocos. Rever a proposta com a turma.\n"
            st.download_button("Baixar proposta da aula", relatorio, file_name="neurobridge_aula.txt", mime="text/plain")

            st.subheader("Adaptação individual da avaliação")
            individuais = []
            for registro in selecionados:
                if registro[3] == 2:
                    individuais.append(registro)
            if len(individuais) == 0:
                st.info("Nenhum estudante autorizou plano individual.")
            else:
                nomes = []
                for registro in individuais:
                    nomes.append(registro[0] + " | " + registro[1])
                nome = st.selectbox("Estudante para o plano", nomes)
                registro = individuais[nomes.index(nome)]
                plano = "PLANO DE AVALIAÇÃO — REVISÃO DO PROFESSOR\n" + nome + " | Turma: " + turma + "\nObjetivo comum: " + objetivo.strip() + "\nCritérios comuns: " + criterios.strip() + "\nEnunciado-base: " + enunciado.strip() + "\n\n"
                for campo in range(len(perguntas)):
                    plano = plano + perguntas[campo] + " " + opcoes[campo][registro[campo + 4]] + "\nPossibilidade: " + apoios[campo][registro[campo + 4]] + "\n\n"
                alertas = []
                if "Escrita ou ortografia" in essenciais and registro[9] in [3, 4, 5, 6]:
                    alertas.append("A forma de resposta escolhida pode substituir a escrita avaliada. Definir uma adaptação que preserve essa evidência.")
                if "Expressão oral perante público" in essenciais and (registro[9] != 3 or registro[10] in [1, 2, 4]):
                    alertas.append("Rever a forma e o contexto de apresentação: expressão oral perante público integra o objetivo declarado.")
                if "Coordenação motora específica" in essenciais and registro[9] != 5:
                    alertas.append("Rever se a resposta proposta evidencia a habilidade motora específica que se pretende avaliar.")
                for numero, recurso in enumerate(recursos):
                    if registro[14][numero] == "1":
                        plano = plano + "Recurso solicitado: " + recurso + "\n"
                        if numero == 0 and "Cálculo sem ferramentas" in essenciais:
                            alertas.append("Calculadora: revisar porque o cálculo sem ferramentas é parte do objetivo. Não aprovar automaticamente.")
                        elif numero in [1, 2] and "Escrita ou ortografia" in essenciais:
                            alertas.append(recurso + ": revisar para não substituir a escrita ou ortografia avaliada.")
                        elif numero == 3 and "Coordenação motora específica" in essenciais:
                            alertas.append("Apoio motor: verificar como preservar a habilidade específica avaliada.")
                        elif numero == 5 and "Leitura autônoma" in essenciais:
                            alertas.append("Leitura em voz: revisar porque a leitura autônoma integra o objetivo.")
                        elif numero == 6 and "Expressão oral perante público" em essenciais:
                            alertas.append("CAA: discutir a forma de produzir evidência do objetivo sem retirar o meio de comunicação necessário.")
                if registro[8] == 2 and "Leitura autônoma" em essenciais:
                    alertas.append("Áudio como acesso: verificar se não substitui a leitura autônoma que está sendo avaliada.")
                if registro[7] == 3 and registro[9] in [4, 5]:
                    plano = plano + "As escolhas de formato e de caminho são guiadas pela mesma meta; não representam redução da exigência.\n"
                plano = plano + "\nObservação do estudante: " + registro[15] + "\n"
                for alerta in alertas:
                    st.warning(alerta)
                    plano = plano + "REVISÃO NECESSÁRIA: " + alerta + "\n"
                plano = plano + "\nEste plano não atribui nota nem aprova automaticamente recursos. Conferir equivalência das evidências, manter os critérios comuns e combinar a adaptação com o estudante.\n"
                st.text(plano)
                st.download_button("Baixar plano individual para revisão", plano, file_name="neurobridge_avaliacao.txt", mime="text/plain")
