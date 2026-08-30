CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS public.dental_knowledge (
    id BIGSERIAL PRIMARY KEY,
    content TEXT,
    metadata JSONB,
    embedding VECTOR(1536)
);

CREATE INDEX IF NOT EXISTS dental_knowledge_embedding_idx
ON public.dental_knowledge
USING hnsw (embedding vector_cosine_ops);
