from core.config import ABUSEIPDB_KEY, ABUSEIPDB_URL
from database.db import get_connection, init_db
import httpx


async def fetch_abuseipdb():
    headers = {"Key": ABUSEIPDB_KEY, "Accept": "application/json"}
    params = {"limit": 10000, "plaintext": False}

    async with httpx.AsyncClient() as client:
        response = await client.get(ABUSEIPDB_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise RuntimeError(
            f"AbuseIPDB request failed with status {response.status_code}: {response.text}"
        )

    try:
        data = response.json()
    except ValueError as e:
        raise RuntimeError(f"AbuseIPDB returned invalid JSON: {response.text!r}") from e

    return data["data"]


async def save_to_db(ips_data):
    await init_db()

    async with await get_connection() as conn:
        for ip_info in ips_data:
            await conn.execute(
                """
                INSERT OR IGNORE INTO ips_intel
                (ip_address, abuse_score, country_code, last_reported)
                VALUES (?, ?, ?, ?)""",
                (
                    ip_info["ipAddress"],
                    ip_info["abuseConfidenceScore"],
                    ip_info["countryCode"],
                    ip_info.get("lastReportedAt"),
                ),
            )
        await conn.commit()


async def run():
    """Runs the full collector"""
    print("Fetching API data...")
    ips_data = await fetch_abuseipdb()
    print(f"Found {len(ips_data)} IPs")

    print("Saving database...")
    await save_to_db(ips_data)
    print("Done!")
