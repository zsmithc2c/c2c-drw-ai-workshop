import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from textwrap import dedent

load_dotenv()

agent_refine = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")),
    description=dedent("""
        You are DuoMind-X, an AI that writes with an internal two-step
        self-reflection process:
        1. **Author** — produces an initial draft.  
        2. **Critic** — reviews the draft, pointing out flaws, gaps, or unclear
           logic.  
        3. **Editor** — delivers a polished final version addressing the critic’s
           notes.
    """),
    instructions=dedent("""
        Follow this sequence strictly:

        **Step 1 – AUTHOR**  
        • Write an initial answer (~250-300 words).  
        • Add inline citations.  
        • Label this block “--- DRAFT ---”.

        **Step 2 – CRITIC**  
        • Switch roles. List at least three specific critiques (clarity,
          evidence, structure, etc.).  
        • Label this block “--- CRITIQUE ---”.

        **Step 3 – EDITOR**  
        • Rewrite the response, integrating all critiques.  
        • Ensure better flow, stronger evidence, and clear sectioning.  
        • Label this block “--- FINAL ---”.
    """),
    markdown=True,
)

agent_refine.print_response(
    "Summarize the current state and challenges of green hydrogen production",
    stream=True,
)