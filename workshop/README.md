# Code2College × DRW — AI-Agent Workshop

## Repo Map

| File                            | What it teaches                       |
| ------------------------------- | ------------------------------------- |
| `assets/01-agent-intro.md`             | Conceptual intro to agents            |
| `assets/02-agent-skeleton.md`          | Hands‑on starter agent                |
| `assets/03-agent-tools-and-mcp.md`     | How tools & MCP servers fit together  |
| `assets/04-agent-rag.md`               | Adding Retrieval‑Augmented Generation |
| `assets/05-agent-prompt-techniques.md` | Prompt engineering cookbook           |
| `assets/requirements.txt`              | All libs for the Python pieces        |

## Learning goals

* Know the difference between a prompt and an agent.
* Be able to wire a tool into an Agno agent.
* Understand when to reach for RAG vs web search.
* Leave with code you can show parents & friends.

## Setup

```bash
# 1. Clone the repo
git clone <your‑fork‑url>
cd c2c‑ai‑class

# 2. Install deps (Python ≥3.10)
pip install -r requirements.txt

# 3. Add an OpenAI API key
export OPENAI_API_KEY="sk‑..."

# 4. Run the starter agent
python 02-agent-skeleton.py
```
