# Aplicações de IA com Agentes Autônomos 
Este projeto foi desenvolvido para ensinar conceitos básicos relativos para o desenvolvimento de agentes usando modelos de linguagem massivos (LLMs, *Large Language Models*).

O foco será o desenvolvimento em **Python** de um assistente capaz de responder perguntas sobre filmes, armazenados como um knowledge Graph em [neo4j](https://neo4j.com).

Apesar de não se desenvolvido em Java, os conceitos aqui apresentados certamente podem ser extrapolados para outros contextos.

## Como utilizar este projeto
1. **Já tenho uma conta no GitHub**

- **Quero evoluir meu projeto a partir desse:** Nesse caso, dê um fork nesse projeto. Assim você poderá ampliar esse projeto no seu próprio GitHub, adicionando o seu próprio código, o que eu recomendo muito.
- **Quero apenas acompanhar esse projeto:** Caso deseje apenas acompanhar a evolução desse projeto para as próximas monitorias, dê um watch, assim será informado sobre as novas alterações desse projeto.

Considere dar uma “estrela“ ao projeto se você achar ele útil **😊**!

2. **Não tenho um conta no GitHub**

Primeiramente, recomendo que crie sua conta no GitHub e siga uma das opções do item 1. Caso opte por não criar a conta no GitHub, você pode:

- **Tenho o Git instalado em minha máquina:** clone este projeto com o comando:

“git clone <https://github.com/lborro/bootcamp-llm-agent>

… e você poderá alterar esse código na sua IDE favorita.

- **Não tenho o Git instalado em minha máquina:** você pode fazer o dowload do projeto clicando no botão verde “Code“ e depois em “Download ZIP”.


## Configuração do ambiente

### OpenAI
Iremos utilizar os modelos de linguagem e emmbeddigs da OpenAI. Logo, é necessário criar uma conta na [OpenAI](https://platform.openai.com/) e gerar uma API Key.

### Docker
Necessária a instalação do Docker e docker-compose para a execução do assistente.

### Python - Ambiente virtual

Vamos instalar o Ananconda para o gerenciamento dos ambientes virtuais em Python. As instruções de instalação podem ser vistas [aqui](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

Após instalado o Anaconda, precisamos criar um ambiente virtual

`conda create -n llm-agent python=3.9`

Ative então o ambiente virtual recém criado

`conda activate llm-agent`

Vamos agora instalar as dependências para trabalharmos com o desenvolvimento de um agente usando LLMs.

`pip install -r requirements.txt`

### Base de dados

Para subir o serviço do neo4j, vamos utilizar o seguinte comando:

`docker-compose up -d`

Em seguida, faremos a ingestão do catálgo de filmes. Na pasta `notebooks`, há um Jupyter Notebook para essa finalidade: `ingest_data.ipynb`. 

## Visão geral da solução

O núcleo do bot conversacional é um agente [ReAct](https://arxiv.org/abs/2210.03629), projetado para extrair informações de um Knowledge Graph em neo4j. Especificamente, o bot é composto por um agente e um conjunto de ferramentas. Durante uma interação com o bot, o agente decide qual ação tomar, que pode incluir o uso de uma ferramenta.
Se o agente determinar que uma ação deve ser executada (como a ativação de uma ferramenta), as ferramentas serão acionadas e os resultados serão retornados ao agente. Caso o agente não solicite a execução de ferramentas, a interação será concluída com uma resposta ao usuário.

### Implementação do agente ReAct
A implementação agente ReAct foi feita usando `langchain v0.2` e `langgraph`. Mais especificamente, o agente funciona como grafo de estados (vide Figura) composto por três componentes principais:

- Estado (State):  Estrutura de dados que armazena o status atual o agente.
- Nós (Nodes): Funções Python que codificam a lógica de um agente. Elas recebem o estado atual como entrada, realizam alguma ação e retornam um estado atualizado.
- Arestas (Edges): Funções Python que determinam o próximo nó de acordo com o estado atual.

![ ](https://raw.githubusercontent.com/lborro/bootcamp-llm-agent/main/img/react-agent.png)


O nó principal (agent) executa um modelo de linguagem (Azure gpt-4o versão 2024-05-13) para determinar se precisa buscar novas informações da base de dados relacional ou se já é capaz de dar uma resposta adequada à interação do usuário. A execução é finalizada se o agente não possui mais nenhuma ação a ser executada. 

## Contato
Se precisar de ajuda ou quiser trocar uma ideia, sinta-se à vontade para me contatar:

- [LinkedIn](https://www.linkedin.com/in/lborro/)