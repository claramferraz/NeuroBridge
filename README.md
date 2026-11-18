# NeuroBridge — formulário e planejamento pedagógico

Aplicação em Python para registrar preferências dos estudantes e ajudar o professor a planejar **aulas e avaliações**.

## Executar

Abra a pasta principal do repositório no terminal do VS Code:

```bash
python neurobridge_basico/main.py
```

Se o sistema usar `python3`, substitua o nome do comando. Não é necessário instalar bibliotecas.

O programa inclui formulário com perguntas condicionais, cadastro, consulta, atualização, exclusão, ficha individual e relatório da turma. Os registros ficam somente na memória durante a execução. Não há conexão com IA ou envio automático de dados ao professor.

Toda a aplicação nova está em [neurobridge_basico/main.py](neurobridge_basico/main.py), organizada em blocos por responsabilidade. A antiga pasta `camadas` e suas subpastas foram removidas.

- [Como usar e limites da demonstração](neurobridge_basico/README.md)
- [Verificações e roteiro de execução](neurobridge_basico/VALIDACAO.md)

O [relatório original](README%20%281%29.md), `app.py` e `mediador_neuroinclusivo.py` continuam registrando o protótipo anterior. A aplicação acima é independente dele.
