# NeuroBridge

Protótipo acadêmico para apoiar estudantes a expressarem suas preferências de aprendizagem e ajudar professores a preparar aulas, atividades e avaliações mais acessíveis.

## Princípio do projeto

O estudante escolhe os apoios que prefere. O NeuroBridge organiza essas escolhas e sugere possibilidades ao professor. Não coleta diagnóstico, não classifica estudantes e não presume que pessoas com a mesma condição aprendam do mesmo jeito.

## O que o protótipo faz

- Registra preferências de formato, ritmo, explicação, atividade, convivência e avaliação.
- Permite criar, consultar, editar e excluir perfis de preferência (CRUD).
- Ajuda o professor a consultar as escolhas e montar sugestões para uma aula ou avaliação.
- Cria um prompt que pode ser revisado e copiado para uma IA externa.
- Não se conecta a uma IA nem altera notas ou avaliações automaticamente.

## Preferências registradas

O formulário permite combinar opções como texto, números, símbolos, imagens, exemplo primeiro, explicação por etapas, blocos curtos, atividade individual ou em grupo e questão por vez. O estudante também pode escolher "depende da atividade" ou não responder.

## Executar localmente

```bash
python -m pip install -r requirements.txt
python -m streamlit run app_preferencias.py
```

Os dados de demonstração ficam em `dados_neurobridge.json`, no computador em que o aplicativo é executado. O protótipo não tem autenticação, hospedagem segura ou controle de acesso; use apenas dados fictícios. Não publique nem compartilhe respostas reais de estudantes com esta versão.

## Organização

- `app_preferencias.py`: formulário e telas Streamlit.
- `neurobridge.py`: regras, sugestões e operações CRUD.
- `tests/test_neurobridge.py`: testes da lógica e do CRUD.

## Próximos passos

1. Validar as perguntas e sugestões com o grupo.
2. Testar o fluxo com dados fictícios.
3. Revisar segurança, acesso e armazenamento antes de qualquer uso real.
4. Avaliar integração com IA somente após definir o que será enviado e como o estudante controlará esse envio.

Este repositório descreve e demonstra um protótipo acadêmico. Não é ferramenta de diagnóstico, tratamento ou substituto das decisões do estudante, do professor ou da instituição.

## Continuidade do trabalho em grupo

O projeto foi iniciado por Clara Ferraz. Esta evolução adiciona um formulário de preferências e sugestões para o professor. O gerador original (`app.py` e `mediador_neuroinclusivo.py`) é mantido como etapa anterior; a nova demonstração é executada por `app_preferencias.py`. Os perfis clínicos da versão anterior não são usados no novo formulário.

## Como a lógica foi programada

1. Strings guardam as opções e os textos de apoio.
2. Listas armazenam perfis e escolhas; uma matriz guarda preferência e contagem.
3. `while` percorre escolhas; `for` e `range` percorrem a matriz.
4. Condicionais `if` combinam sugestões, pois várias preferências podem coexistir.
5. Funções separam criar, consultar, atualizar e excluir; JSON mantém a demonstração entre execuções.

As sugestões são regras explícitas, não inteligência artificial. As contagens se referem aos perfis selecionados e não medem capacidade, diagnóstico ou eficiência de aprendizagem. Preferências diferentes podem exigir alternativas para o professor escolher.

## Avaliações e privacidade

Os apoios se referem à apresentação dos enunciados e à organização da atividade. O professor decide o conteúdo, os critérios, a dificuldade e as adaptações institucionais. O formulário não substitui avaliação pedagógica nem produz laudos.

Antes de responder, a interface explica onde os dados ficam e quem pode acessá-los nesta demonstração. É possível consultar, editar e excluir registros. Apelidos e observações livres não entram no prompt. Não há envio automático a serviços externos. O arquivo local de respostas deve ficar fora do Git.

Ainda faltam autenticação, permissões por estudante e professor, gestão de turmas, política de retenção e revisão institucional para uso real. Um aviso ou termo não torna o protótipo adequado à LGPD por si só. Não use esta versão para coletar respostas reais nem a disponibilize como formulário público.

## Verificação

```bash
python -m unittest discover -s tests -v
python -m py_compile app_preferencias.py neurobridge.py
```
