from bedrock_agentcore import BedrockAgentCoreApp
from graph.builder import build_graph

app = BedrockAgentCoreApp()
graph = build_graph()

@app.entrypoint
def invoke(payload):
    prompt = payload.get("prompt", "")
    result = graph.invoke({"messages": [{"role": "user", "content": prompt}]})
    return {"result": result["messages"][-1].content}

if __name__ == "__main__":
    app.run()
