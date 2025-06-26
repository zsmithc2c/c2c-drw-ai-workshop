# Agent Tools versus MCP Servers

So far you saw a single Python object called `ExaTools`.  In practice there are two layers you can add to an agent: **Tool wrappers** and **Model Context Protocol (MCP) servers**.

| Layer          | What it is                                                  | Example                                         | Why you need it                                                     |
| -------------- | ----------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------- |
| **Tool**       | Thin Python class with `run()`                              | ExaTools, Calculator, PDF‑reader                | Gives the LLM super‑powers outside text                             |
| **MCP Server** | Long‑running micro‑service that exposes many tools via HTTP | Agents as a Service (Agnō MCP), LangChain Serve | Lets multiple agents share the same expensive resources (DBs, GPUs) |

## Model Context Protocol in 60 sec

MCP is a message format that extends the basic OpenAI schema:

```
system → user → tool → assistant
```

Each message can include:

* **`content`** – text
* **`tool_calls`** – JSON describing which tool to run
* **`results`** – what the tool returned
* **`state`** – any scratch‑pad the agent keeps

Because MCP is plain JSON, you can pipe it over WebSockets, store it in Postgres, or replay it for debugging.

## When to choose what

* **Class demo / hackathon** → Direct tool classes inside your script.  Fast & simple.
* **Production or team project** → Spin up an MCP server so mobile apps, Discord bots, and cron jobs can all hit the *same* agent backend without code duplication.
