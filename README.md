# MCPioneer 🚀
**Build Your Own Custom MCP Server for AI Agents**

MCPioneer is a beginner-friendly project demonstrating how to create a custom MCP (Message/Command/Processing) server using Python. This server acts as a bridge to extend the capabilities of AI agents, allowing them to perform external tasks like calling APIs, accessing databases, and executing custom tools.

---

## 📚 What is MCP?
An MCP server provides tools, resources, and services that AI agents can access to enhance their functionalities. Think of it as a "toolbox" that an AI can open whenever it needs external help beyond its basic capabilities.

---

## ⚙️ Technologies Used
- **Python 3.10+**
- **MXGp Python SDK**
- **UV Package Manager**
- **Claude Desktop (for testing)**

---

## 🚀 Getting Started

### 1. Install UV (Better Package Manager)
- Windows:
  ```bash
  iwr -useb https://mirror.ghproxy.com/https://raw.githubusercontent.com/astral-sh/uv/main/scripts/install.ps1 | iex
  ```
- Mac/Linux:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Initialize Project
```bash
uv init .
uv add mcp cli
```

### 3. Create a Simple MCP Server
Example `main.py`:
```python
from mcp_servers.fast_mcp import FastMCP

server = FastMCP(name="DemoServer")

@server.tool
def add_numbers(a: int, b: int) -> int:
    return a + b

@server.resource
def greet(name: str) -> str:
    return f"Hello, {name}!"

server.run()
```

### 4. Install MCP Server into Claude Desktop
```bash
uv run mcp install main.py
```

### 5. Configure Claude Desktop
- Go to **Settings → Developer → Edit Config**.
- Add your server to the configurations manually if necessary.
- Restart Claude Desktop if you don't see the MCP server immediately.

---

## 🛠️ Project Structure
```
MCPioneer/
├── main.py
├── README.md
├── .venv/ (created automatically)
└── uv.toml
```

---



---

## ✨ Author
Created with ❤️ by Nithin.
