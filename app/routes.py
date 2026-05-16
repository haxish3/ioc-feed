from database.db import get_connection
import aiosqlite


async def get_ips_intel(country: str | None = None, score: int | None = None) -> list:
    query = "SELECT * FROM ips_intel"
    params = []

    async with await get_connection() as conn:

        conn.row_factory = aiosqlite.Row

        filters = []

        if country:
            filters.append("country_code = ?")
            params.append(country)
        if score:
            filters.append("abuse_score >= ?")
            params.append(score)

        if filters:
            query += " WHERE " + " AND ".join(filters)

        cursor = await conn.execute(query, params)
        rows = await cursor.fetchall()

        return [dict(row) for row in rows]


async def get_ips_intel_status():
    async with await get_connection() as conn:
        queryCount = "SELECT COUNT(*) FROM ips_intel"
        queryAVG = "SELECT AVG(abuse_score) FROM ips_intel"
        queryGroupBy = (
            "SELECT country_code, COUNT(*) FROM ips_intel GROUP BY country_code"
        )

        cursorCount = await conn.execute(queryCount)
        cursorAVG = await conn.execute(queryAVG)
        cursorGroupBy = await conn.execute(queryGroupBy)

        total_ips_row = await cursorCount.fetchone()
        avg_score_row = await cursorAVG.fetchone()
        top_countries_rows = await cursorGroupBy.fetchall()

        total_ips = total_ips_row[0] if total_ips_row else 0
        avg_score = avg_score_row[0] if avg_score_row else 0
        top_countries = [
            {"country_code": r[0], "count": r[1]} for r in top_countries_rows
        ]

        return {
            "total_records": total_ips,
            "average": avg_score,
            "country_ranking": top_countries,
        }
