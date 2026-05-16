from database.db import get_connection


async def get_ips_intel(country=None, abuse_score=None):
    query = "SELECT * FROM ips_intel"
    params = []

    async with await get_connection() as conn:
        filters = []

        if country:
            filters.append("country_code = ?")
            params.append(country)
        if abuse_score:
            filters.append("abuse_score >= ?")
            params.append(abuse_score)

        if filters:
            query += " WHERE " + " AND ".join(filters)

        cursor = await conn.execute(query, params)
        raws = await cursor.fetchall()

        return raws


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

        total_ips = await cursorCount.fetchone()
        avg_abuse_score = await cursorAVG.fetchone()
        top_countries = await cursorGroupBy.fetchall()

        return {
            "total_records": total_ips[0],
            "averege_threat_level": avg_abuse_score[0],
            "country_ranking": top_countries,
        }
