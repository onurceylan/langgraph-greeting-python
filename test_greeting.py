import pytest
from main import create_greeting_graph, greeting_node, GreetingState

def test_greeting_basic():
    """Test that the greeting graph returns proper greeting with user's name"""
    graph = create_greeting_graph()
    result = graph.invoke({"name": "Test User"})
    assert "Test User" in result["greeting"]
    assert "Hello" in result["greeting"]
    assert "Welcome" in result["greeting"]

def test_greeting_multiple_names():
    """Test greeting with different names"""
    graph = create_greeting_graph()
    names = ["Alice", "Bob", "Charlie", "Diana"]
    
    for name in names:
        result = graph.invoke({"name": name})
        assert name in result["greeting"], f"Name {name} should be in greeting"
        assert result["greeting"].startswith("Hello"), "Greeting should start with Hello"

def test_greeting_node_directly():
    """Test the greeting_node function directly"""
    state: GreetingState = {"name": "Direct Test", "greeting": ""}
    result = greeting_node(state)
    
    assert result["name"] == "Direct Test"
    assert "Direct Test" in result["greeting"]
    assert result["greeting"] == "Hello, Direct Test! Welcome!"

def test_greeting_output_format():
    """Test that greeting output matches expected format"""
    graph = create_greeting_graph()
    result = graph.invoke({"name": "Format Test"})
    
    expected_format = "Hello, Format Test! Welcome!"
    assert result["greeting"] == expected_format

def test_greeting_empty_name():
    """Test greeting with empty name"""
    graph = create_greeting_graph()
    result = graph.invoke({"name": ""})
    assert "Hello" in result["greeting"]
    assert "Welcome" in result["greeting"]

def test_graph_state_preservation():
    """Test that the graph preserves the name in state"""
    graph = create_greeting_graph()
    result = graph.invoke({"name": "State Test"})
    
    assert result["name"] == "State Test"
    assert "greeting" in result
    assert result["greeting"] != ""