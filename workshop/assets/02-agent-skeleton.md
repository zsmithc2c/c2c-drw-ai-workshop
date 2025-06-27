# A Skeleton Agent with Agno

Below is your **starter agent** built with the [Agno](https://github.com/agno-ai) framework.  You already saw the raw snippet in the repo; here it is with inline comments so you know *why* each line exists.

```python
from agno.agent import Agent          # Core agent class
from agno.models.openai import OpenAIChat  # Wrapper around OpenAI chat models
from agno.tools.exa import ExaTools  # Web‑search tool (keyword & news)
from textwrap import dedent
from datetime import date

today = date.today().isoformat()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),       # 1️⃣ LLM brain
    tools=[ExaTools(start_published_date=today, type="keyword")],  # 2️⃣ Tool belt
    description=dedent("""\
        You are Professor X‑1000 … (persona text trimmed for brevity)
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches … (strategy steps)
    """),
    markdown=True,               # Pretty output
    show_tool_calls=True,        # Expose what the agent does under the hood
    add_datetime_to_instructions=True,  # Embed today’s date for temporal grounding
)

# ---------- Usage demo ----------
if __name__ == "__main__":
    agent.print_response(
        "Research the latest developments in brain‑computer interfaces",
        stream=True,
    )
```

### How it works

1. **Planning** – The instructions tell the agent to start with three searches.
2. **Tool execution** – `ExaTools` hits the Exa API and returns JSON citations.
3. **Synthesis** – The LLM composes a markdown report citing its sources.

### Try it yourself

```bash
pip install -r requirements.txt  # once
python 02-agent-skeleton.py
```

Then tweak:

* Change the persona to a *Sports Statistician*.
* Swap the tool list for a *Weather* API.
* Ask a totally new question.
