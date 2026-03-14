from graph.builder import build_graph

graph = build_graph()

result = graph.invoke({
    "messages": [{"role": "user", "content": "Hello"}]
})


print(result["messages"][-1].content)

