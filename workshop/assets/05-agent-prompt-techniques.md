# Agent Prompting Techniques

## 1. System vs. User prompt

* **System** – Sets overall behaviour (tone, role).  Think *“rules of the game.”*
* **User** – Asks a specific question or gives data.  Think *“current turn.”*

> **Tip:** In Agnō you pass `description` (persona) + `instructions` (strategy) as two separate strings so students can tweak them independently.

## 2. Context windows

Every model has a token limit (\~128k for GPT‑4o).  Keep it small:

* Short system prompt (≤ 50 tokens).
* Use bullet lists instead of paragraphs.
* Clip extra history you don’t need.

## 3. Zero‑shot prompting

**Pattern**: *“You are X. Do Y.”*
**Use when** the task is trivial or you can’t supply examples.

```text
You are a friendly explainer.  Explain photosynthesis in 3 bullet points.
```

## 4. Few‑shot prompting

**Pattern**: Provide 1‑3 Q/A pairs so the model copies the style.

```text
Q: 2+2
A: 4
Q: 5×3
A: 15
Q: 7×8
A:
```

## 5. Chain‑of‑thought (CoT)

Ask the model to *think step‑by‑step* but *hide* the chain from the final answer.

```text
You are a math tutor. Think step‑by‑step, then give the answer after "Answer:".
```

## 6. Constraint‑based prompting

Force the model to follow hard rules.

```text
**Constraints**
1. Answer in JSON.
2. Keys = ["definition", "analogy", "emoji"].
```

### Putting it together

Combine techniques:

1. **System**: *You are a JSON‑only assistant.*
2. **Few‑shot**: Show one perfect JSON answer.
3. **Constraints**: *No extra keys allowed.*

Result: deterministic, parseable output ready for a downstream program.
