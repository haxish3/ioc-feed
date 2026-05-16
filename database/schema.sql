CREATE TABLE IF NOT EXISTS ips_intel (
    id INTEGER PRIMARY KEY,
    ip_address TEXT NOT NULL UNIQUE,
    abuse_score INTEGER,
    country_code TEXT,
    last_reported TIMESTAMP,
    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)