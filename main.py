import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import asyncio
from database.db import init_db
from workers.abuseipdb_collector import save_to_db
from workers.test_data import TEST_IPS

async def main():
    print("Testing with mock data... I have no free tier requests left :(")
#    await init_db()
    await save_to_db(TEST_IPS)
    print("Fake DONE!")

asyncio.run(main())