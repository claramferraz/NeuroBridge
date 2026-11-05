# NeuroBridge Developed

Formulário clicável de preferências para **aulas e avaliações**, com cadastro, consulta, atualização, exclusão e painel do professor. Não pergunta nem infere diagnóstico.

## Executar

Requer **Python 3.11 ou superior**. Na pasta principal do repositório:

```bash
python -m pip install -r neurobridge.developed/requirements.txt
python -m streamlit run neurobridge.developed/app.py
```

Abra o endereço local mostrado no terminal, normalmente `http://localhost:8501`. Se seu sistema usa `python3`, substitua `python` os dois comandos.

## Começar

1. Em **Formulário do aluno**, informe um apelido fictício, a turma e suas preferências. Escolha como compartilhar e clique em **Salvar preferências**.
2. Em **Cadastros**, consulte, edite ou exclua. Com a base vazia, **Carregar quatro exemplos fictícios** permite experimentar o painel.
3. Em **Painel do professor**, escolha a turma, informe tema, objetivo e critérios comuns. Confira percentuais, proposta de tempo e plano individual autorizado.

O aluno pode baixar sua resposta em TXT e entregá-la pelo canal combinado. Em outro navegador, o professor abre o arquivo, copia o texto e usa **Cadastros → Receber respostas de outro navegador**. A transferência é manual. O professor também pode baixar a proposta da aula e o plano individual.

Leia o [README (3) — escopo refinado, funcionamento e limites](README%283%29.md).

## Organização

`app.py` contém a aplicação, organizada internamente por responsabilidade. Não há pastas de assuntos de Python. `requirements.txt` fixa a versão de Streamlit usada na validação.

Os [READMEs anteriores](../README%20%282%29.md) e a pasta [neurobridge_basico](../neurobridge_basico/) permanecem como registro das versões anteriores.

**Esta é uma demonstração local sem login nem banco de dados. Use informações fictícias.** Recarregar a página, perder a sessão ou reiniciar o servidor pode descartar os cadastros. Arquivos baixados permanecem no computador de quem os recebeu.
