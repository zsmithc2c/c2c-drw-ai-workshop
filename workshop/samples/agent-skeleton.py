import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from textwrap import dedent

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")),
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
    markdown=True,
)

agent.print_response(
    "Research the latest developments in brain‑computer interfaces",
    stream=True,
)
