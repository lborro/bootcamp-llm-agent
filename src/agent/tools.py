import os

from langchain.chains import GraphCypherQAChain
from langchain_core.tools import tool
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector

from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI

print(os.getenv("NEO4J_URL"))

neo4j_vector_store = Neo4jVector.from_existing_graph(
    embedding=AzureOpenAIEmbeddings(model="text-embedding-3-large"),
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="movie_index",
    node_label="Movie",
    text_node_properties=["title", "description", "location"],
    embedding_node_property="movie_embedding",
)

neo4j_graph = Neo4jGraph(
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USER"),
    password=os.getenv("NEO4J_PASSWORD"),
)


@tool
def get_movies_by_description(description: str):
    """
    Função para busca um filme por meio de uma descrição (sinopse).
    A entrada é necessariamente um texto descritivo, nunca um nome de filme.
    O retorno é uma lista de filmes que mais se assemelham à descrição fornecida.
    """
    return neo4j_vector_store.similarity_search(description, top_n=10)


@tool
def get_info_about_movies(query: str):
    """
    Função que retorna informações sobre filmes.
    A entrada pode ser tanto uma pergunta sobre um ator quanto sobre um filme.
    Por exemplo: quais filmes o ator X participou? ou quais atores participaram do filme X?
    """
    chain = GraphCypherQAChain.from_llm(
        AzureChatOpenAI(temperature=0, model="gpt-4o"),
        graph=neo4j_graph,
        verbose=False,
        return_direct=True,
        top_k=10,
    )
    return chain.invoke({"query": query})
