CREATE TABLE threads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT NOT NULL,
    abuse_score INTEGER,
    country_code TEXT,
    ips TEXT,
    domain TEXT,
    usage_type TEXT,
    total_reports INTEGER,
    last_reported TIMESTAMP,
    colected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
