import aiosqlite

DATABASE = "ioc-feed.db"

async def get_connection():
    return aiosqlite.connect(DATABASE)

async def init_db():
    with open("database/schema.sql", "r") as f:
        sql = f.read()

    async with aiosqlite.connect(DATABASE) as conn:
        await conn.execute(sql)
        await conn.commit()