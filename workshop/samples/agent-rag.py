import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.azure import AzureOpenAI
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

load_dotenv()

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFKnowledgeBase(
    urls=["$RETRIEVED FROM WORKSHOP ASSETS"],
    vector_db=PgVector(table_name="financial_reports", db_url=DB_URL, search_type=SearchType.hybrid),
)
knowledge_base.load(load=True,upsert=True)

agent = Agent(
    model=AzureOpenAI(id="gpt-4o"),
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True,
)

agent.print_response("What what NVDA's quarterly revenue in 2024?", stream=True)
