CREATE TABLE votes (
    doc_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    poll_id TEXT NOT NULL,
    choice TEXT NOT NULL,
    timestamp DOUBLE PRECISION,
    edge_id TEXT,
    processed_at DOUBLE PRECISION
);

ALTER TABLE votes DISABLE ROW LEVEL SECURITY;
