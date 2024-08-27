from fastapi import FastAPI, status, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool

from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver

from src.auth import get_api_key

from src.agent import ReactAgent
from src.schema import BotResponse


llm_agent = ChatOpenAI(model="gpt-4o", temperature=0)
react_agent = ReactAgent(llm=llm_agent, memory=MemorySaver())


app = FastAPI(
    title="Movie Assistant",
    description="Assistant for movie-related questions",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    return {"healthcheck": "Everything OK!"}


@app.get("/answer", response_model=BotResponse)
async def answer_question(
    query: str, session_id: str, api_key: str = Security(get_api_key)
):
    try:
        response = await run_in_threadpool(
            react_agent.answer_question, query, session_id
        )
        return response
    except Exception:
        return {
            "query": query,
            "response": """Desculpe, não consegui encontrar informações para responder adequadamente sua pergunta.""",
            "reasoning": [],
        }
