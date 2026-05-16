from .routes import get_ips_intel, get_ips_intel_status
from fastapi import FastAPI

app = FastAPI()


@app.get("/stats")
async def stats():
    return await get_ips_intel_status()


@app.get("/ips")
async def list_ips(country: str | None = None, score: int | None = None):
    return await get_ips_intel(country, score)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
