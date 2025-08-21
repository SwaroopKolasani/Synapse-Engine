# Synapse-Engine
**AI-Powered Product Recall, Risk & Return Verification System**  
BigQuery + Generative AI + Vector Search + Multimodal (Object Tables)

## 1) Problem
Late product recalls and fraudulent returns cost billions. Traditional keyword analytics miss semantic patterns across reviews, tickets, regulations, and images.

## 2) Solution
Synapse-Engine unifies:
- **Semantic Recall Detection** — embeddings + `VECTOR_SEARCH` on reviews/tickets to find emerging risks.
- **Executive AI Insights** — `AI.GENERATE` summaries and `AI.FORECAST` time-series risk predictions.
- **Return Authenticity** — **Object Tables** over GCS images/manuals to detect label/serial mismatches and flag suspicious returns.

## 3) BigQuery AI Features Used
- **Generative AI in SQL**: `AI.GENERATE` (summaries/classification), `AI.FORECAST` (TimesFM-based forecasting).  
- **Vector Search**: `ML.GENERATE_EMBEDDING` for text/image embeddings, `VECTOR_SEARCH` (+ optional vector index).  
- **Multimodal**: **Object Tables** + **ObjectRef** to reason over images & documents.

## 4) Architecture
 The flow covers ingestion → embeddings → vector search → AI summaries/forecasts → multimodal verification → dashboard.



<img width="3840" height="3469" alt="Untitled diagram _ Mermaid Chart-2025-08-21-041336" src="https://github.com/user-attachments/assets/27e0226f-2dfa-42bb-ac1a-a36936430b87" />
