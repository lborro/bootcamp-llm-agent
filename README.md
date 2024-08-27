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

## Desenho de solução

## Contato
Se precisar de ajuda ou quiser trocar uma ideia, sinta-se à vontade para me contatar:

- [LinkedIn](https://www.linkedin.com/in/lborro/)