"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import aiohttp
# from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import List
import jsonplaceholder_requests
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base, engine, User, Post, Session


async def fetch_api(url: str) -> dict:
    async with aiohttp.ClientSession() as mysession:
        response = await mysession.get(url)
        data = await response.json()
        return data


# https://stackoverflow.com/questions/68230481/sqlalchemy-attributeerror-asyncengine-object-has-no-attribute-run-ddl-visit
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_users(session: AsyncSession, users_data_list):
    for item in users_data_list:
        user = User(id=item['id'], name=item['name'], username=item['username'], email=item['email'])
        session.add(user)
    await session.commit()


async def insert_posts(session: AsyncSession, posts_data_list):
    for item in posts_data_list:
        post = Post(user_id=item['userId'], id=item['id'], title=item['title'], body=item['body'])
        session.add(post)
    await session.commit()


async def async_main():
    users_data: List[dict]
    users_data_short: List[dict]
    posts_data: List[dict]
    posts_data_short: List[dict]

    # users_data, posts_data = await asyncio.gather(get_data_from_url(jsonplaceholder_requests.USERS_DATA_URL),
    #                                               get_data_from_url(jsonplaceholder_requests.POSTS_DATA_URL))
    users_data, posts_data = await asyncio.gather(fetch_api(jsonplaceholder_requests.USERS_DATA_URL),
                                                  fetch_api(jsonplaceholder_requests.POSTS_DATA_URL))

    users_data_short = [{'id': item['id'], 'name': item['name'], 'username': item['username'],
                         'email': item['email']} for item in users_data if 'id' in item
                        and 'name' in item and 'username' in item and 'email' in item]
    posts_data_short = [{'userId': item['userId'], 'id': item['id'], 'title': item['title'],
                         'body': item['body']} for item in posts_data if 'userId' in item
                        and 'id' in item and 'title' in item and 'body' in item]

    # print("Users_data:", users_data_short)
    # print("Posts_data:", posts_data_short)

    async with Session() as session:
        await init_models()
        await insert_users(session, users_data_short)
        await insert_posts(session, posts_data_short)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
