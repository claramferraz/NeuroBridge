# Verificação e demonstração

O programa único `main.py` passou em 21 verificações automatizadas locais, usando informações fictícias. O executor de testes é uma ferramenta de desenvolvimento separada da aplicação.

| Nº | Verificação aprovada |
| --- | --- |
| 1 | Executável sem imports, funções próprias, classes, dicionários ou compreensões. |
| 2 | Inicialização e encerramento da aplicação única. |
| 3 | Cadastro com múltiplos perfis, sem repetição, e matriz de 20 colunas. |
| 4 | Cinco ramificações do formulário para apoios de leitura e números. |
| 5 | Cancelamento do cadastro sem salvar nem consumir código. |
| 6 | Cancelamento da edição preserva a linha original. |
| 7 | Edição preserva código, remove apoios obsoletos e reinicia retorno. |
| 8 | Remoção explícita do perfil e da observação. |
| 9 | Busca por string ignora caixa e trata ausência de resultados. |
| 10 | Exclusão exige confirmação e os códigos não são reutilizados na sessão. |
| 11 | Códigos incorretos, ausentes e não palíndromos não alteram dados. |
| 12 | Ficha individual só é emitida na opção de compartilhamento correspondente. |
| 13 | Percentuais por turma e por pergunta, com exclusão de não autorizados e dados pessoais. |
| 14 | Base vazia, relatório sem autorização, turma ausente e menu inválido. |
| 15 | Retirada do compartilhamento é respeitada no próximo relatório. |
| 16 | Roteiro soma exatamente a duração e rejeita números inválidos. |
| 17 | Distribuição de tempo impede exceder o total e sinaliza etapas sem tempo. |
| 18 | Todas as opções possuem sugestão e códigos palíndromos são distintos. |
| 19 | Limites superiores das opções e retorno negativo chegam à ficha sem diagnóstico automático. |
| 20 | Validação de texto, perfil, opções, observação e compartilhamento. |
| 21 | Execução real do arquivo com o interpretador Python, sem dependências. |

## Demonstração manual

1. Execute `python neurobridge_basico/main.py` na raiz do repositório.
2. Escolha `1`, cadastre `Aluno A`, turma `SI-A` e perfil `0`. Selecione barreira de leitura e confira a pergunta extra. Em experiência, use `0 — Ainda não testei`. Compartilhamento `2`. Confirme com `s` e anote `NB-11`.
3. Cadastre `Aluno B`, também em `SI-A`, com outro formato de aula e sem barreira declarada. Use compartilhamento `1`.
4. Em `2`, busque `si-a`. Em `5`, consulte a ficha de `NB-11`; a ficha de `NB-22` deve indicar ausência de autorização individual.
5. Em `6`, escolha `SI-A`, tema `Frações` e objetivo `Comparar frações`. Confira dois formulários no total e somente um respondente na pergunta extra de leitura.
6. Informe `50` minutos e blocos de `10`, `20` e `15`. O último bloco terá `5`, completando exatamente `50`.
7. Atualize `NB-11` em `3`, retire a barreira de leitura e confirme. O apoio anterior de leitura deixará de aparecer. Exclua `NB-22` em `4`, confirmando `EXCLUIR`, e confira a diminuição da base no relatório.
8. Encerre em `0` e execute novamente. Não haverá registros, pois a aplicação ainda não possui persistência.

## O que os testes não demonstram

Os testes verificam o funcionamento do código nos cenários descritos. Não demonstram eficácia pedagógica, compreensão do formulário por estudantes ou segurança para dados reais. A versão atual é uma demonstração local sem autenticação.
