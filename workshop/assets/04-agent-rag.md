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

## Quick‑start with Agnō

Below is a fully‑working snippet that loads a PDF cookbook and lets you ask questions about it.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

DB_URL = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=DB_URL, search_type=SearchType.hybrid),
)
knowledge_base.load(upsert=True)  # <1> Embeds & stores paragraphs

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,      # <2> Attach KB for retrieval
    add_references=True,           # <3> Show source links in the answer
    search_knowledge=False,        # Skip web search because we only care about the PDF
    markdown=True,
)

agent.print_response("How do I make chicken and galangal in coconut milk soup")
```

## Exercise for students

1. Replace the PDF URL with your own class notes.
2. Ask "Explain the three most important points for tomorrow’s quiz."
3. Notice the citations—click them to jump to the exact page.

## Common pitfalls + fixes

| Symptom                               | Fix                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------ |
| "No module named pgvector"            | `pip install pgvector psycopg2-binary`                                         |
| Agent returns wrong document snippets | Increase `SearchType.hybrid` top‑k or check if your pages are too big          |
| Wrong answer                          | Double‑check the material actually contains the info (garbage in, garbage out) |
