"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_api(url: str) -> dict:
    async with aiohttp.ClientSession() as mysession:
        response = await mysession.get(url)
        data = await response.json()
        return data
