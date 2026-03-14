"""Graph nodes."""

from graph.state import State
from model import get_llm

llm = get_llm()


def chat_node(state: State) -> dict:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
