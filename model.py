"""LLM loader."""

import os

from langchain_openai import ChatOpenAI


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        api_key=os.environ["OPENAI_API_KEY"],
    )
