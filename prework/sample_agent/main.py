from agno.agent import Agent
from agno.models.openai import OpenAIChat


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
)

if __name__ == "__main__":
    agent.print_response(
        "What is the capital of France", stream=True
    )
