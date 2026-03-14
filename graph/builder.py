"""Builds and compiles the LangGraph workflow."""

from langgraph.graph import END, START, StateGraph

from graph.nodes import chat_node
from graph.state import State


def build_graph():
    workflow = StateGraph(State)
    workflow.add_node("chat", chat_node)
    workflow.add_edge(START, "chat")
    workflow.add_edge("chat", END)
    return workflow.compile()
