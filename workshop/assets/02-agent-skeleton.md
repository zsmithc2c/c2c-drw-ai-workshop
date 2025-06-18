# A Skeleton Agent with Agno

Below is your **starter agent** built with the [Agno](https://github.com/agno-ai) framework.  You already saw the raw snippet in the repo; here it is with inline comments so you know *why* each line exists.

```python
from agno.agent import Agent          # Core agent class
from agno.models.openai import OpenAIChat  # Wrapper around OpenAI chat models
from agno.tools.duckduckgo import DuckDuckGoTools
from textwrap import dedent


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),       # 1️⃣ LLM brain
    tools=[DuckDuckGoTools()],  # 2️⃣ Tool belt
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.
        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
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
