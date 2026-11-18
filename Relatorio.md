# NeuroBridge

Relatório de Desenvolvimento do Projeto: Mediador de Inteligência Artificial Neuroinclusivo (NeuroBrigde)

# 1. Introdução

O projeto NeuroBrigde tem como objetivo tornar o uso de inteligências artificiais mais acessível para pessoas com diferentes necessidades cognitivas, especialmente pessoas com TDAH, autismo e dislexia.

Para isso, foi desenvolvido um protótipo em Python que personaliza prompts de acordo com as preferências e necessidades de cada usuário, orientando a IA a produzir respostas mais acessíveis.

# 2. Desenvolvimento e funcionalidades

O protótipo foi desenvolvido utilizando Python e Streamlit, permitindo que o usuário interaja com uma interface gráfica simples.

Foram implementadas as seguintes funcionalidades:
Seleção de perfis: TDAH, autismo, dislexia ou geral, com possibilidade de escolher mais de um.
Limite de palavras: permite definir o tamanho máximo da resposta.
Escolha de tom: acolhedor, neutro ou formal.
Campo de solicitação: permite escrever o que deseja pedir à IA.
Geração de prompts: combina automaticamente o pedido com instruções específicas de acessibilidade.

Cada perfil possui regras próprias. Para TDAH, são priorizados passos curtos e respostas diretas. Para autismo, utiliza-se linguagem literal e organizada. Para dislexia, são priorizadas frases simples, parágrafos curtos e espaçamento adequado.

Também foram desenvolvidos recursos de histórico, recuperação do último prompt, salvamento em arquivo de texto e atualização das preferências.

# 3. Funcionamento

O usuário seleciona suas preferências, descreve o que precisa e clica em "Gerar prompt". O sistema organiza essas informações em um comando personalizado, que pode ser copiado e enviado para uma ferramenta de inteligência artificial externa.

# 4. Tecnologias utilizadas

Python: desenvolvimento da lógica do sistema.

Streamlit: construção da interface gráfica.

Dataclasses e Enum: organização das preferências e dos perfis de acessibilidade.

# 5. Limitações e próximos passos

Atualmente, o protótipo não possui conexão direta com uma inteligência artificial. É necessário copiar o prompt gerado e enviá-lo manualmente para outra ferramenta.
Como próximos passos, pretende-se implementar essa conexão, aprimorar a interface e ampliar as opções de personalização, tornando a experiência mais completa e adaptada às necessidades individuais.

# 6. Conclusão

Nesta etapa, foi desenvolvido um protótipo funcional que transforma solicitações comuns em prompts personalizados, considerando diferentes necessidades cognitivas e de aprendizagem.

O resultado representa o primeiro passo na construção do NeuroBrigde, uma ferramenta que busca tornar a interação com inteligências artificiais mais acessível, clara e inclusiva.
