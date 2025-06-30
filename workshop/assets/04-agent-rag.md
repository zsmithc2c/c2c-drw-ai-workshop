# Agents with RAG (Retrieval‑Augmented Generation)

> **Motto:** *“If the knowledge isn’t in the model, fetch it.”*

## Why RAG?

Large models know a *lot*, but not:

* Your school’s bell schedule.
* Today’s chemistry worksheet.
* That PDF recipe you found five minutes ago.

**Retrieval‑Augmented Generation (RAG)** plugs this hole by letting the agent *retrieve* external documents, then use those passages as extra context in the prompt.

## Key pieces

1. **Embedding model** – Converts each paragraph into a math vector.
2. **Vector database** – Stores the vectors so you can search by semantic meaning.
3. **Retriever** – Given a query, finds the *k* most relevant chunks.
4. **LLM** – Gets the retrieved text prepended to the user question.

## Quick‑start with Agno

Start PostgreSQL with `pgvector` extension pre-installed:

```bash
docker compose up -d
```

| Source | What you’ll grab | Quick link |
| --- | --- | --- |
| NVIDIA Investor Relations → Financial Reports → Quarterly Results | A curated packet with: press release, slide deck, and direct PDF link to Form 10‑Q. | https://investor.nvidia.com/financials/ |
| SEC EDGAR (CIK 1045810) | The legally filed 10‑Q PDF. More reliable if the IR site is down. | https://www.sec.gov/edgar/browse/?CIK=1045810 |
| Nasdaq “NVDA SEC Filings” | Handy listing of 10‑Qs/10‑Ks with one‑click PDFs. | https://www.nasdaq.com/market-activity/stocks/nvda/sec-filings |

Below is a fully‑working snippet that loads a PDF cookbook and lets you ask questions about it.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["$RETRIEVED FROM ABOVE"],
    vector_db=PgVector(table_name="financial_reports", db_url=DB_URL, search_type=SearchType.hybrid),
)
knowledge_base.load(load=True,upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True,
)

agent.print_response("What what NVDA's quarterly revenue in 2024?", stream=True)
```

## Exercise for students

1. Replace the PDF with your own class notes.
2. Ask "Explain the three most important points for tomorrow’s quiz."
3. Notice the citations—click them to jump to the exact page.

## Common pitfalls + fixes

| Symptom                               | Fix                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| "No module named pgvector"            | `pip install pgvector psycopg2-binary`                                         |
| Agent returns wrong document snippets | Increase `SearchType.hybrid` top‑k or check if your pages are too big          |
| Wrong answer                          | Double‑check the material actually contains the info (garbage in, garbage out) |
