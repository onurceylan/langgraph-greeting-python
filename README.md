# LangGraph Greeting Agent (Python)

A simple greeting agent built with LangGraph that accepts a user's name and returns a personalized greeting message. This implementation does **not** use any LLM - it's a pure logic demonstration of LangGraph's state management capabilities.

## Features

- ✅ Single-node agent with proper state management
- ✅ START → greeting_node → END graph structure
- ✅ Type-safe state schema using TypedDict
- ✅ No LLM required - pure Python logic
- ✅ Comprehensive unit tests with pytest
- ✅ Fast dependency management with uv

## Project Structure
```tree
LANGGRAPH-GREETING-PYTHON/
    ├── .dev-history.md
    ├── .gitignore
    ├── .python-version
    ├── main.py
    ├── pyproject.toml
    ├── README.md
    ├── test_greeting.py
    └── uv.lock
```

## Prerequisites

- Python 3.10 or higher
- uv package manager

## Setup
```bash
# Install uv - if it is not working use in bash or pip
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/langgraph-greeting-python.git
cd langgraph-greeting-python
```

## Install dependencies
```bash
uv sync
```

This will create a .venv virtual environment, install langgraph and install pytest (dev dependency).

## Usage 
### Run the agent
```bash
uv run python main.py
```

### Testing
```bash
uv run pytest
```

# How It Works
## State Schema
The agent uses a typed state schema defined with Python's TypedDict:

```python
from typing import TypedDict

class GreetingState(TypedDict):
    name: str       # Input: user's name
    greeting: str   # Output: greeting message
```
Graph Structure
```text
START → greeting_node → END
The graph flows through a single node that:
- Receives a name as input state
- Generates a greeting message
- Returns the updated state with greeting
```

# Node Implementation
```python

def greeting_node(state: GreetingState) -> GreetingState:
    name = state["name"]
    return {
        "name": name,
        "greeting": f"Hello, {name}! Welcome!"
    }
No LLM is used - it's pure Python string formatting.
```
# Graph Creation
```python

from langgraph.graph import StateGraph, START, END

def create_greeting_graph():
    workflow = StateGraph(GreetingState)
    
    # Add the greeting node
    workflow.add_node("greeting_node", greeting_node)
    
    # Define the graph flow
    workflow.add_edge(START, "greeting_node")
    workflow.add_edge("greeting_node", END)
    
    return workflow.compile()
```
