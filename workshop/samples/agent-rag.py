import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.pgvector import PgVector, SearchType

load_dotenv()

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Retrieve PDF's from any of the following sources:
# https://investor.nvidia.com/financials/
# https://www.sec.gov/edgar/browse/?CIK=1045810
# https://www.nasdaq.com/market-activity/stocks/nvda/sec-filings

knowledge_base = PDFKnowledgeBase(
    path="data/pdfs", # <-- Relative path to downloaded PDF's
    vector_db=PgVector(
        table_name="financial_reports", 
        db_url=DB_URL, 
        search_type=SearchType.hybrid,
    ),
    reader=PDFReader(chunk=True)
)

agent = Agent(
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")),
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True,
)

agent.knowledge.load(recreate=True)

agent.print_response("What was NVIDA's quarterly revenue in 2025?", stream=True)
