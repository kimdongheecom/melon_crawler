import httpx
from bs4 import BeautifulSoup

async def fetch_melon_chart():
    url = "https://www.melon.com/chart/index.htm?dayTime=2025040817"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.melon.com/index.htm"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "html.parser")
        chart_rows = soup.select("tr[data-song-no]")

        results = []

        for rank, row in enumerate(chart_rows, start=1):
            try:
                title = row.select_one("div.ellipsis.rank01 a").text.strip()
                artist = row.select_one("div.ellipsis.rank02 a").text.strip()
                album = row.select_one("div.ellipsis.rank03 a").text.strip()
                results.append({
                    "rank": rank,
                    "title": title,
                    "artist": artist,
                    "album": album
                })
            except Exception as e:
                print(f"[Error] {rank}위 처리 실패: {e}")

        return results
