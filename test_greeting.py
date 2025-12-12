import pytest
from main import create_greeting_graph

def test_greeting():
    graph = create_greeting_graph()
    result = graph.invoke({"name": "Test User"})
    assert "Test User" in result["greeting"]
    assert "Hello" in result["greeting"]