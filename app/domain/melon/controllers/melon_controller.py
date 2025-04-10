

from app.domain.melon.services.melon_services import fetch_melon_chart


class MelonController:
    def __init__(self):
        pass

    async def get_top100(self):
        try:
            result = await fetch_melon_chart()  # 비동기 함수이므로 await 필요함.
            for song in result:
                print(f"{song['rank']}위 | {song['title']} - {song['artist']} [{song['album']}]")
            return result
        except Exception as e:
            print(f"❌ Failed to crawl Melon TOP100: {e}")
            raise e