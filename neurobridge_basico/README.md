# NeuroBridge — formulário para aulas e avaliações

Um programa executável no terminal. O estudante informa preferências e barreiras atuais. O professor consulta sugestões individuais e percentuais da turma para planejar aulas e avaliações.

## Executar

Na pasta principal do repositório, execute:

```bash
python neurobridge_basico/main.py
```

Em sistemas que usam `python3`, troque somente o nome do comando. No VS Code, também é possível abrir `main.py` e selecionar **Run Python File in Terminal**. Requer Python 3, sem bibliotecas adicionais.

Toda a lógica está em `main.py`, com blocos para formulário, cadastros, ficha individual e painel do professor. Não há pastas por assunto de Python nem programas intermediários para executar.

## Menu

| Opção | Ação |
| --- | --- |
| 1 | Cadastrar um formulário. |
| 2 | Consultar por apelido, turma ou código; Enter lista todos. |
| 3 | Atualizar pelo código. Enter mantém uma resposta existente. |
| 4 | Excluir pelo código, confirmando com `EXCLUIR`. |
| 5 | Emitir a ficha individual autorizada para o professor. |
| 6 | Gerar relatório da turma e distribuir o tempo da aula. |
| 0 | Encerrar e descartar os dados da sessão. |

Cadastros e alterações passam por revisão e só são salvos com `s`. Na edição, `0` remove o perfil declarado e `-` apaga a observação. Códigos como `NB-11` identificam formulários durante a sessão; não são senhas.

## Formulário

| Parte | Informação |
| --- | --- |
| Identificação da demonstração | Apelido fictício e turma. |
| Perfil opcional | Um ou mais perfis declarados, ou não informar. |
| Aula | Formato, abertura, atividade, ritmo, participação e ambiente. |
| Barreiras atuais | Leitura, números, ambos, nenhuma declarada ou não informar. |
| Perguntas condicionais | Apoio específico para leitura e/ou números, conforme a barreira relatada. |
| Avaliação | Enunciado, modo de resposta, tempo e devolutiva. |
| Retorno | Ainda não testei, ajudou, não percebi diferença ou atrapalhou. |
| Complemento | Observação curta e escolha de compartilhamento. |

Há uma escolha principal por pergunta, referente ao momento atual. A observação permite registrar combinações não representadas pelas opções. As preferências podem ser atualizadas.

O perfil declarado é opcional e não determina os apoios. Não há cálculo de diagnóstico, gravidade ou capacidade. Quem prefere símbolos recebe a sugestão de símbolos com legenda; quem relata barreira de leitura recebe perguntas sobre leitura, independentemente do perfil.

Quando uma atualização muda as barreiras, as respostas que deixaram de se aplicar são removidas. Ao mudar as preferências, o retorno anterior começa em "Ainda não testei", para não atribuir a uma combinação nova o resultado de uma experiência anterior.

## Informações para o professor

| Compartilhamento escolhido | Ficha individual | Relatório da turma |
| --- | --- | --- |
| 0. Não incluir | Não | Não |
| 1. Somente resumo da turma | Não | Sim |
| 2. Resumo e ficha individual | Sim | Sim |

A ficha individual apresenta as preferências, sugestões correspondentes e a observação. O relatório agrega somente formulários autorizados de uma turma. Não exibe apelidos, perfis declarados ou observações individuais.

O painel mostra todas as opções escolhidas, inclusive minoritárias. Para cada pergunta, informa quantidade, percentual e denominador. Nas perguntas extras, o denominador inclui somente quem recebeu aquela pergunta. "Sem preferência" é resposta válida; pergunta não aplicada fica fora da contagem. Sem respondentes, não há divisão.

Exemplo: de quatro formulários autorizados, dois receberam a pergunta de leitura. Se um escolheu frases curtas, o painel mostra **1/2 = 50%**, com **2 não aplicadas**. O percentual descreve formulários, sem garantir uma resposta por pessoa ou representação de toda a turma.

## Planejamento da avaliação

O professor informa tema e competência a avaliar. O programa organiza sugestões de apresentação do enunciado, forma de resposta, tempo e devolutiva. O professor precisa verificar a compatibilidade com o objetivo: o programa não interpreta semanticamente esse texto.

Uma resposta oral pode demonstrar compreensão de um conceito, mas não substitui automaticamente uma tarefa cujo objetivo seja a escrita. Destacar dados não deve revelar uma resposta que o estudante deveria identificar. A proposta é reduzir barreiras mantendo a competência, o desafio e os critérios de avaliação.

O sistema não calcula notas, prevê desempenho, decide aprovação ou concede automaticamente adaptações. Pedidos de tempo adicional são registrados para discussão com o professor e o apoio institucional.

## Organização do tempo

O professor pode informar de 5 a 240 minutos de aula e distribuir o tempo entre abertura, explicação e prática. O restante fica para verificação e devolutiva. O programa impede valores acima do tempo disponível e sinaliza etapas com zero minuto.

Os percentuais de preferências não são convertidos automaticamente em minutos. A distribuição é uma decisão pedagógica, considerando o conteúdo e as necessidades individuais.

## Limites concretos

- **Somente memória:** encerrar o programa descarta todos os registros.
- **Terminal sem login:** qualquer operador pode consultar, alterar e excluir dados. Compartilhamento é filtro do relatório, não controle de acesso.
- **Demonstração com dados fictícios:** não inserir diagnósticos, nomes ou respostas reais. O agregado também não garante anonimato em grupos pequenos.
- **Sem integração externa:** não há IA, banco de dados, interface web ou envio automático ao professor. Os relatórios aparecem no mesmo terminal.
- **Regras explícitas:** sugestões previamente escritas, sem personalização clínica nem evidência de eficácia deste questionário.
- **Retorno é autorrelato:** "ajudou" não comprova, sozinho, melhora da aprendizagem.

Para uso real, será necessário definir persistência, acesso por papéis e proteção dos dados, além de validar perguntas e apoios com estudantes, professores e a instituição.

## Referências de concepção

As orientações sobre alternativas de expressão e alinhamento da avaliação ao objetivo foram consultadas nas fontes abaixo. Elas fundamentam decisões de projeto, sem validar automaticamente o formulário ou o software:

- [CAST — Action & Expression](https://udlguidelines.cast.org/action-expression/)
- [CAST — UDL Tips for Assessment](https://www.cast.org/resources/tips-articles/udl-tips-assessment/)
- [CAST — UDL and Assessment](https://udloncampus.cast.org/page/assessment_udl)

Veja [VALIDACAO.md](VALIDACAO.md) para os cenários testados e uma demonstração manual.
