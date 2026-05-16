from dotenv import load_dotenv
import os

load_dotenv()

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/blacklist"