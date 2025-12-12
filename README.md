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

## Bonus Points Implementation

### 1️⃣ LangGraph MCP Server Configuration

This project includes a `mcp.json` configuration file for IDE integration:

```json
{
  "mcpServers": {
    "langgraph": {
      "command": "langgraph",
      "args": ["dev"],
      "disabled": false
    }
  }
}
```

This configuration enables:
- IDE-integrated LangGraph development
- Real-time graph visualization
- Seamless debugging experience

### 2️⃣ LangSmith Integration

#### Setup LangSmith Account

1. Create a free account at https://smith.langchain.com/
2. Navigate to Settings → API Keys
3. Copy your API key

#### Configure Environment Variables

Copy `.env.example` to `.env` and add your API key:

```bash
cp .env.example .env
```

Edit `.env` with your LangSmith credentials:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_api_key_from_smith_langchain
LANGCHAIN_PROJECT=langgraph-greeting
```

#### Verify with langgraph dev

Once configured, run the interactive development server:

```bash
uv run langgraph dev
```

This command:
- Starts a local development server
- Enables interactive graph visualization
- Shows real-time execution traces
- Displays state changes at each node

**Screenshot of LangSmith Graph Visualization:**

The graph visualization shows the simple three-step flow:

```
┌─────────┐
│  START  │
└────┬────┘
     │
     ▼
┌──────────────┐
│ greeting_node│
└────┬─────────┘
     │
     ▼
┌─────────┐
│   END   │
└─────────┘
```

When you run `langgraph dev` and invoke the graph with a name, you'll see in LangSmith:
- Input state with the name parameter
- Node execution and state transitions
- Final output with the generated greeting
- Complete execution trace and timing information

### 3️⃣ Comprehensive Unit Tests

The project includes multiple unit tests that verify the greeting output:

```python
pytest
```

**Test Coverage:**
- ✅ `test_greeting_basic()` - Verifies basic greeting format
- ✅ `test_greeting_multiple_names()` - Tests multiple input names
- ✅ `test_greeting_node_directly()` - Direct node function testing
- ✅ `test_greeting_output_format()` - Validates exact output format
- ✅ `test_greeting_empty_name()` - Edge case testing
- ✅ `test_graph_state_preservation()` - Ensures state integrity

Run tests with coverage:

```bash
uv run pytest -v
```

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
