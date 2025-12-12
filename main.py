from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# State şeması
class GreetingState(TypedDict):
    name: str
    greeting: str

# Greeting node fonksiyonu (LLM YOK!)
def greeting_node(state: GreetingState) -> GreetingState:
    name = state["name"]
    return {
        "name": name,
        "greeting": f"Hello, {name}! Welcome!"
    }

# Graph oluştur
def create_greeting_graph():
    workflow = StateGraph(GreetingState)
    
    # Node ekle
    workflow.add_node("greeting_node", greeting_node)
    
    # Edges ekle
    workflow.add_edge(START, "greeting_node")
    workflow.add_edge("greeting_node", END)
    
    return workflow.compile()

# Test
if __name__ == "__main__":
    graph = create_greeting_graph()
    result = graph.invoke({"name": "Alice"})
    print(result["greeting"])