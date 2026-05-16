CREATE TABLE ip_intel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT NOT NULL UNIQUE,
    abuse_score INTEGER,
    country_code TEXT,
    isp TEXT,
    domain TEXT,
    usage_type TEXT,
    total_reports INTEGER,
    last_reported TIMESTAMP,
    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);
