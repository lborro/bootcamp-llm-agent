import os
from typing import Sequence
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableLambda
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.prebuilt import create_react_agent

from src.agent.prompt import REACT_PROMPT
from src.agent.tools import get_info_about_movies, get_movies_by_description

MEMORY_MAX_MESSAGES = int(os.getenv("MEMORY_MAX_MESSAGES"))


def _modify_messages(messages: Sequence[BaseMessage]):
    """
    Trims the message list to include the most recent N human interactions.

    Args:
        messages (Sequence[BaseMessage]): A sequence of messages.

    Returns:
        List[BaseMessage]: A list of messages starting from the Nth most recent human interaction.
    """
    counter = 0
    # Finds the Nth most recent human message
    for i, message in enumerate(messages[::-1]):
        if isinstance(message, HumanMessage):
            counter  += 1
            if counter == MEMORY_MAX_MESSAGES:
                break
    return [
        SystemMessage(content=REACT_PROMPT)
    ] + messages[-(i + 1) :]


class ReactAgent:
    def __init__(
        self, llm: BaseChatModel, memory: BaseCheckpointSaver
    ):
        """
        Initializes a ReactAgent instance.

        Args:
            llm (BaseChatModel): The language model to be used.
            memory (BaseCheckpointSaver): The memory checkpoint saver.
        """
        self.graph = create_react_agent(
            llm,
            tools=[get_info_about_movies, get_movies_by_description],
            messages_modifier=RunnableLambda(_modify_messages),
            checkpointer=memory,
        )

    def answer_question(self, question: str, thread_id: str):
        """
        Answers a question based on the given inputs.

        Args:
            question (str): The question to be answered.
            thread_id (str): The ID used to keep track of the message chain state.

        Returns:
            dict: A dictionary containing the question, response, and reasoning.
        """
        config = {"configurable": {"thread_id": thread_id}}
        response = self.graph.invoke({"messages": [("user", question)]}, config=config)

        # Find the most recent human message in the response
        for i, message in enumerate(response["messages"][::-1]):
            if isinstance(message, HumanMessage):
                break

        # Extract the reasoning for the response
        reasoning = [
            {"action": message.type, "observation": message.pretty_repr()}
            for message in response["messages"][-i:]
        ]

        # Return the question, response, and reasoning
        return {
            "query": question,
            "response": response["messages"][-1].content,
            "reasoning": reasoning,
        }
