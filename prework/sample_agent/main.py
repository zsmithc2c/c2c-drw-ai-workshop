import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY") 
    ),
)

if __name__ == "__main__":
    agent.print_response("What is the capital of France", stream=True)
