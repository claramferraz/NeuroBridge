# README (3) — NeuroBridge: preferências, aula e avaliação adaptada

## 1. Escopo refinado

O estudante escolhe como prefere acessar o conteúdo, participar da aula e demonstrar o que aprendeu. O professor recebe percentuais da turma, uma proposta de divisão do tempo e sugestões individuais para adaptar a avaliação.

O princípio do projeto é **adaptar os meios de acesso e resposta preservando o objetivo e os critérios da avaliação**. A preferência é situada, pode mudar e não é diagnóstico, medida de capacidade ou prova de qual método produzirá melhor aprendizagem.

Esta versão não pergunta o que a pessoa "é", com o que se identifica ou qual condição possui. Não classifica estudantes, não gera perfis clínicos ocultos e não relaciona respostas a um diagnóstico provável.

## 2. Evolução do projeto

| Versão | Escopo | Local |
| --- | --- | --- |
| 1 | Mediador para organizar prompts acessíveis, com Python e Streamlit. | [README (1)](../README%20%281%29.md), `app.py` e `mediador_neuroinclusivo.py` da raiz. |
| 2 | Formulário no terminal, CRUD e relatórios pedagógicos. Incluía perfil declarado opcional. | [README (2)](../README%20%282%29.md) e [neurobridge_basico](../neurobridge_basico/). |
| 3 | Formulário clicável sem diagnósticos, percentuais, proposta de tempo, transferência manual de respostas e planos de avaliação com critérios comuns. | Esta pasta `neurobridge.developed`. |

A pasta `neurobridge_basico` foi preservada. A antiga estrutura de pastas `entrada`, `listas`, `matrizes`, `strings` e `crud` ão faz parte da nova aplicação. Os conceitos de Python são instrumentos da programação, não conteúdos oferecidos ao estudante.

## 3. O que o estudante escolhe

| Dimensão | Exemplos de escolhas |
| --- | --- |
| Formato principal de aula | Exemplos concretos; lógica e exemplos matemáticos; interação e exercícios; atividade lúdica com símbolos explicados; sem preferência. |
| Interação | Exercícios na sala, troca com colegas, relação com outros assuntos, alternância ou atividade individual. |
| Estímulos | Menos elementos visuais, menos sons, ambos ou nenhum ajuste solicitado. |
| Orientações | Passos e checklist, linguagem literal e sequência previsível, escolhas guiadas, pausas e avisos de transição. |
| Acesso ao conteúdo | Texto simples, áudio com transcrição, imagem descrita, ampliação e contraste, leitor de tela ou material acessível. |
| Resposta à avaliação | Escrita, digitação, áudio/conversa, diagrama/modelo, demonstração prática ou indicação de símbolos/CAA. |
| Contexto da apresentação | Professor em particular, pequeno grupo, turma ou entrega sem apresentação. |
| Desafio | Mais exemplos, etapas orientadas ou aprofundamento opcional. |
| Tempo | Revisão, pausas ou conversa sobre prazo/tempo adicional. |
| Experiência | Ainda não experimentei, ajudou, não percebi diferença ou atrapalhou. |
| Recursos | Calculadora, corretor/dicionário, ditado, apoio motor, organizador gráfico, leitura em voz, CAA e tecnologia assistiva. É possível escolher vários. |

CAA significa comunicação aumentativa e alternativa. O programa registra pedidos; não fornece essas tecnologias nem garante que um material externo seja compatível com elas.

O formulário não exige um diagnóstico para pedir um apoio. Uma pessoa pode combinar preferência por símbolos, menos ruído, trabalho individual e digitação sem ser enquadrada em uma categoria.

## 4. Das características às possibilidades

A lista inicial reunia diagnósticos, condições de acesso, traços e preferências. Ela foi convertida em necessidades e escolhas observáveis. Não existe uma regra "diagnóstico X → melhor aula Y".

| Necessidade ou preferência relatada | Possibilidade incluída |
| --- | --- |
| Ter autonomia na execução | Escolher caminhos para alcançar a mesma meta. |
| Organizar e acompanhar uma tarefa | Etapas, checklist, pausas e aviso de transição. |
| Expressar ideias sem depender apenas de fala ou escrita longa | Diagramas, modelos, demonstração ou comunicação por símbolos. |
| Apoiar o trabalho com números | Solicitar calculadora ou material de apoio, com revisão da habilidade avaliada. |
| Acompanhar leitura | Texto organizado, leitura em voz ou material acessível conforme a necessidade. |
| Evitar esforço de escrita manual | Digitação, ditado ou outro meio de resposta compatível com o objetivo. |
| Apoiar a composição e a ortografia | Corretor ou dicionário, quando não substituir a habilidade avaliada. |
| Reduzir exigências motoras que não sejam o objetivo | Apoios de navegação e alternativas de expressão. |
| Trabalhar com áudio | Áudio/conversa e conteúdo com transcrição, sem reprodução automática. |
| Trabalhar com representações visuais | Imagens e símbolos explicados, acompanhados de descrição. |
| Aprofundar o conteúdo | Maior complexidade opcional, sem aumentar individualmente a exigência mínima ou apenas acrescentar tarefas repetitivas. |
| Ter previsibilidade ou menor exposição pública | Sequência clara e apresentação em contexto combinado. |
| Ajustar o acesso visual | Ampliação, contraste e compatibilidade com a tecnologia assistiva usada. |
| Aprender ou responder por ação e movimento | Demonstrações e atividades práticas, com alternativa acessível. |

Preferências visuais, auditivas ou por movimento não são tratadas como tipos fixos de aluno. As sugestões são hipóteses pedagógicas para experimentar e rever.

## 5. Como os percentuais viram uma proposta de aula

Cada formulário indica **um formato principal**, evitando tratar várias modalidades do mesmo formulário como votos distintos. Para cada escolha:

```text
percentual = quantidade de formulários com a escolha / formulários autorizados da turma × 100
```

"Sem preferência" entra no relatório. O painel mostra o denominador e todas as escolhas com respostas, inclusive minoritárias. Recursos de apoio admitem escolhas múltiplas; seus percentuais podem somar mais de 100% e essa diferença aparece na tela.

O professor informa a duração total, reserva abertura e verificação/devolutiva e seleciona os formatos compatíveis com o conteúdo. O restante é distribuído proporcionalmente às escolhas desses formatos. Matemática pode ser retirada da proposta quando não fizer sentido para o tema; sua frequência continua visível no relatório.

Os minutos são arredondados para baixo, e o restante é distribuído pelas maiores partes decimais. Empates seguem a ordem exibida. A soma final é a duração informada.

Exemplo: numa aula de 50 minutos, com 5 de abertura e 5 de devolutiva, restam 40. Se as quatro modalidades tiverem a mesma quantidade de escolhas, cada uma recebe 10 minutos. Uma preferência de 25% não é uma afirmação de que aquele formato produzirá 25% da aprendizagem.

Se não houver escolhas aplicáveis, o sistema avisa que a divisão é equilibrada e provisória, sem fundamento em votos. Não inventa percentuais. Se o professor não reservar tempo para os formatos ou não selecionar nenhum, a proposta fica bloqueada.

**As necessidades de acesso valem em todos os blocos.** Menos ruído não vira um bloco isolado da aula. Uma preferência pouco frequente não autoriza retirar um apoio individual. A proposta é um ponto de partida revisável pelo professor.

## 6. Adaptação da avaliação

O professor define uma vez:

- Tema e objetivo comum.
- Critérios comuns de avaliação.
- Enunciado-base, quando houver.
- Habilidades que fazem parte essencial da avaliação.

O plano individual repete objetivo, critérios e enunciado-base, acrescentando possibilidades de acesso, expressão, apresentação, tempo e recursos. Não altera notas, pesos, dificuldade mínima ou critérios conforme preferências.

Há situações que exigem revisão expressa. Calculadora não é aprovada automaticamente quando o objetivo é calcular sem ferramentas. Corretor ou ditado exigem revisão quando a escrita/ortografia integra a habilidade avaliada. O mesmo cuidado se aplica à leitura em voz, coordenação motora e exposição oral.

Esses avisos não são proibições automáticas: o professor precisa preservar a evidência da habilidade e discutir alternativas, sem retirar o meio de comunicação necessário ao estudante. A ausência de aviso também não significa aprovação automática: as regras não cobrem todas as situações.

O programa produz **planos de adaptação para revisão humana**. Não cria questões de uma disciplina, interpreta semanticamente o objetivo, aplica uma prova, corrige respostas ou substitui a decisão do professor.

## 7. Cadastro, compartilhamento e transferência

As operações de cadastrar, consultar, atualizar e excluir funcionam na mesma aplicação. Atualizar mantém o código. Mudar preferências ou recursos reinicia o retorno para "Ainda não experimentei", evitando atribuir o resultado de uma experiência à configuração nova.

| Opção do estudante | Relatório agregado | Plano individual | Exportação da resposta |
| --- | --- | --- | --- |
| Não incluir | Não | Não | Não |
| Somente resumo da turma | Sim | Não | Sim, sem observação individual. |
| Resumo e plano individual | Sim | Sim | Sim, incluindo observação. |

Apelido e turma constam no arquivo exportado para identificação operacional. O resumo exibido ao professor não lista os apelidos. Isso não garante anonimato em grupos pequenos.

**Entre navegadores:** o aluno baixa o TXT e o entrega pelo canal combinado. O professor abre, copia e cola o texto em Cadastros. Não há envio automático, e-mail, nuvem ou banco de dados compartilhado.

A importação valida formato, versão, limites e escolhas. Um erro rejeita todo o lote. Apelido e turma repetidos não somam votos; a substituição exige marcar uma opção explícita. Essa chave reduz repetições, mas não comprova uma pessoa por formulário. Códigos locais são preservados ou atribuídos. O limite é de 100 respostas por importação.

O código de referência usa uma parte numérica simétrica, comparável por fatiamento. É apenas uma convenção de identificação da demonstração, não uma senha nem prova da identidade de quem respondeu.

## 8. Implementação e limites

`app.py` usa Streamlit para os controles clicáveis e o estado da sessão. A lógica usa listas, matriz de registros, strings, condições, conversões, cálculos, `for`, `range`, `while`, contadores, acumuladores, operações de lista, `enumerate` e fatiamento. Não introduz classes, funções próprias, dicionários de domínio ou modelos de IA.

O uso de Streamlit é a camada de interface necessária aos cliques. A versão de terminal continua em `neurobridge_basico`.

Esta entrega é uma **demonstração sem autenticação**. As áreas Aluno, Cadastros e Professor são modos de navegação, não contas ou permissões. Quem acessa a sessão pode operar seus cadastros. Use somente dados fictícios.

Os dados ficam em `session_state`. Recarregar a página, perder a conexão da sessão ou reiniciar o servidor pode descartá-los. Arquivos exportados não são apagados por uma exclusão na aplicação. Para retirar uma resposta já entregue, o professor precisa excluir ou atualizar sua própria cópia. Não publicar respostas reais no GitHub.

O preenchimento não foi validado com estudantes nem professores. Os testes de código não demonstram eficácia pedagógica, validade clínica ou conformidade de acessibilidade. Compatibilidade com leitores de tela e outras tecnologias precisa de validação específica com usuários.

## 9. Verificações realizadas

Foram aprovadas **24 verificações automatizadas** usando a ferramenta oficial `streamlit.testing.v1.AppTest`. Incluíram ações nos controles, cadastro, edição, exclusão, cancelamento, duplicidades, importação atômica, isolamento de sessões, compartilhamento, percentuais, arredondamento do tempo, preservação dos critérios comuns e conflitos entre apoios e habilidades essenciais.

O servidor Streamlit também iniciou localmente. Esses resultados verificam os fluxos programados; não equivalem a uma auditoria visual, de tecnologias assistivas ou de uso real com alunos.

## 10. Referências e atribuição das decisões

O referencial é o **Desenho Universal para a Aprendizagem (DUA)**, especialmente o princípio de **Ação e Expressão**. Na organização atual das diretrizes da CAST, a implementação se relaciona a três frentes:

| Frente do DUA | Aplicação no NeuroBridge |
| --- | --- |
| Interação | Alternativas de resposta, movimento, navegação e acesso a recursos assistivos. |
| Expressão e comunicação | Escrita, áudio, diagramas, modelos, demonstração e CAA, conforme o objetivo. |
| Desenvolvimento de estratégias | Metas claras, escolhas guiadas, etapas, checklist, organização do tempo e retorno sobre a experiência. |

As diretrizes da CAST orientam a oferta de alternativas de ação, comunicação e apoio ao planejamento. Não constituem uma tabela clínica de "melhor adaptação por diagnóstico". As regras deste programa são **decisões de projeto a validar**, inspiradas nas diretrizes.

- [CAST — Action & Expression](https://udlguidelines.cast.org/action-expression/).
- [CAST — UDL and Assessment](https://udloncampus.cast.org/page/assessment_udl): relação entre a habilidade avaliada e barreiras que podem ser removidas.
- [CAST — UDL Tips for Assessment](https://www.cast.org/resources/tips-articles/udl-tips-assessment/).
- [Streamlit — Forms](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form).
- [Streamlit — Session State](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state).

O próximo passo é testar a compreensão do formulário e a utilidade dos planos com dados fictícios e participantes voluntários. Persistência, autenticação, proteção de dados e eventual IA vêm depois dessa validação.
