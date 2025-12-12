# LangGraph Greeting Agent (Python)

A simple greeting agent built with LangGraph that accepts a user's name and returns a personalized greeting message. This implementation does **not** use any LLM - it's a pure logic demonstration of LangGraph's state management capabilities.

## ✨ Features

- ✅ Single-node agent with proper state management
- ✅ START → greeting_node → END graph structure
- ✅ Type-safe state schema using TypedDict
- ✅ No LLM required - pure Python logic
- ✅ 6 comprehensive unit tests (100% passing)
- ✅ LangGraph MCP Server integration
- ✅ LangSmith tracing support
- ✅ Fast dependency management with uv

## 📁 Project Structure

```text
langgraph-greeting-python/
├── .dev-history.md          # Detailed development history
├── .env.example             # LangSmith configuration template
├── .gitignore               # Python-specific ignore patterns
├── .python-version          # Python version specification
├── main.py                  # Main application with graph definition
├── mcp.json                 # MCP server configuration
├── pyproject.toml           # Project dependencies
├── README.md                # This file
├── test_greeting.py         # Unit tests
└── uv.lock                  # Dependency lock file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- uv package manager ([install here](https://docs.astral.sh/uv/getting-started/installation/))

### Installation

```bash
# Clone the repository
git clone https://github.com/onurceylan/langgraph-greeting-python.git
cd langgraph-greeting-python

# Install dependencies
uv sync
```

## 📖 Usage

### Run the greeting agent

```bash
uv run python main.py
```

**Output:**
```
Hello, Alice! Welcome!
```

### Run unit tests

```bash
uv run pytest -v
```

**Test Results:**
```
test_greeting.py::test_greeting_basic PASSED                    [ 16%]
test_greeting.py::test_greeting_multiple_names PASSED           [ 33%]
test_greeting.py::test_greeting_node_directly PASSED            [ 50%]
test_greeting.py::test_greeting_output_format PASSED            [ 66%]
test_greeting.py::test_greeting_empty_name PASSED               [ 83%]
test_greeting.py::test_graph_state_preservation PASSED          [100%]

================================================= 6 passed in 0.65s =================================================
```

## 🏗️ How It Works

### State Schema

The agent uses a typed state schema defined with Python's TypedDict:

```python
from typing import TypedDict

class GreetingState(TypedDict):
    name: str       # Input: user's name
    greeting: str   # Output: greeting message
```

### Graph Flow

Simple linear flow from START to END:

```
┌─────────────────────────────────────┐
│           Graph Flow                │
├─────────────────────────────────────┤
│                                     │
│   START → greeting_node → END       │
│                                     │
│  • Receive name as input            │
│  • Process through greeting_node    │
│  • Return personalized greeting     │
│                                     │
└─────────────────────────────────────┘
```

### Node Implementation

```python
def greeting_node(state: GreetingState) -> GreetingState:
    """Generate a personalized greeting message."""
    name = state["name"]
    return {
        "name": name,
        "greeting": f"Hello, {name}! Welcome!"
    }
```

**Key Point:** No LLM is used - it's pure Python logic!

### Graph Compilation

```python
from langgraph.graph import StateGraph, START, END

def create_greeting_graph():
    workflow = StateGraph(GreetingState)
    
    # Add the greeting node
    workflow.add_node("greeting_node", greeting_node)
    
    # Define edges
    workflow.add_edge(START, "greeting_node")
    workflow.add_edge("greeting_node", END)
    
    return workflow.compile()
```

## 🎁 Bonus Points Implementation

This project includes all bonus points from the assignment:

### 1️⃣ LangGraph MCP Server Configuration

MCP (Model Context Protocol) enables IDE integration for LangGraph development.

**Configuration File:** `mcp.json`
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

**Benefits:**
- IDE-integrated LangGraph development
- Real-time graph visualization
- Seamless debugging and testing

### 2️⃣ LangSmith Integration

LangSmith provides tracing, monitoring, and visualization for your LangGraph applications.

#### Setup Instructions

**Step 1: Create LangSmith Account**
- Visit https://smith.langchain.com/
- Sign up with your email
- Navigate to Settings → API Keys
- Copy your API key

**Step 2: Configure Environment Variables**

Copy the template:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_api_key_here
LANGCHAIN_PROJECT=langgraph-greeting
```

**Step 3: Verify Installation**

Run the interactive development server:
```bash
uv run langgraph dev
```

This command:
- ✅ Starts a local development server (http://localhost:8000)
- ✅ Enables interactive graph visualization
- ✅ Shows real-time execution traces
- ✅ Displays state changes at each node
- ✅ Records execution in LangSmith dashboard

#### LangSmith Graph Visualization

When you run `langgraph dev`, you'll see the graph visualized:

```
┌──────────────────────────────────────────┐
│         LangSmith Visualization          │
├──────────────────────────────────────────┤
│                                          │
│           ┌──────────────┐               │
│           │    START     │               │
│           └──────┬───────┘               │
│                  │                       │
│                  ▼                       │
│          ┌──────────────────┐            │
│          │  greeting_node   │            │
│          │  (Pure Python)   │            │
│          └──────┬───────────┘            │
│                 │                       │
│                 ▼                       │
│           ┌──────────────┐              │
│           │     END      │              │
│           └──────────────┘              │
│                                         │
│  • Input: name (str)                   │
│  • Output: greeting (str)              │
│  • No LLM required                     │
│                                         │
└──────────────────────────────────────────┘
```

**LangSmith Dashboard Features:**
- Execution traces with timing information
- State transitions visualization
- Input/output inspection
- Performance metrics
- Error tracking and debugging

### 3️⃣ Comprehensive Unit Tests

The project includes 6 comprehensive unit tests that verify all aspects of the greeting output:

**Test Suite:**

| Test Name | Purpose | Status |
|-----------|---------|--------|
| `test_greeting_basic()` | Validates basic greeting format | ✅ PASS |
| `test_greeting_multiple_names()` | Tests with different input names | ✅ PASS |
| `test_greeting_node_directly()` | Direct node function testing | ✅ PASS |
| `test_greeting_output_format()` | Validates exact output format | ✅ PASS |
| `test_greeting_empty_name()` | Edge case: empty name handling | ✅ PASS |
| `test_graph_state_preservation()` | Ensures state integrity | ✅ PASS |

**Run tests with verbose output:**
```bash
uv run pytest -v
```

**Run tests with coverage:**
```bash
uv run pytest --cov=. --cov-report=html
```

## 📋 Dependencies

### Main Dependencies
- **langgraph** (>=1.0.4) - LangGraph framework
- **python-dotenv** (>=1.0.0) - Environment variable management

### Development Dependencies
- **pytest** (>=9.0.2) - Unit testing framework

Install dependencies:
```bash
uv sync
```

## 🔧 Development Workflow

### Making Changes

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and test:
```bash
uv run pytest -v
```

3. Commit your changes:
```bash
git add .
git commit -m "feat: your meaningful commit message"
```

4. Push to GitHub:
```bash
git push origin feature/your-feature-name
```

### View Development History

See `.dev-history.md` for detailed documentation of all commits, AI prompts used, and challenges encountered.

## 📚 Documentation

- **README.md** - This file (project overview and setup)
- **.dev-history.md** - Detailed development history with all commits
- **mcp.json** - MCP server configuration
- **.env.example** - LangSmith environment setup template

## 🎓 Learning Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Python TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict)

## 📊 Project Statistics

- **Language:** Python
- **Framework:** LangGraph
- **Total Tests:** 6
- **Test Success Rate:** 100% ✅
- **Lines of Code (main.py):** ~35
- **Development Time:** ~2 hours
- **Commits:** 14 (with detailed history)

## ✅ Assignment Completion

This project successfully implements all requirements and bonus points:

- ✅ Basic LangGraph agent implementation
- ✅ TypedDict state management
- ✅ No LLM usage (pure Python logic)
- ✅ MCP server configuration (mcp.json)
- ✅ LangSmith integration with full setup guide
- ✅ 6 comprehensive unit tests (all passing)
- ✅ Complete development documentation
- ✅ Graph visualization guide

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Onur Ceylan**

---

**Last Updated:** 12.12.2025
" | Set-Content README.md -Encoding UTF8