"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:example@localhost/blog"

engine = create_async_engine(PG_CONN_URI)
Session = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False)


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class User(Base):
    name = Column(String(50), nullable=True)  # FullName
    username = Column(String(32), nullable=False)  # NickName
    email = Column(String, nullable=True)

    # создайте связи relationship между моделями: User.posts и Post.user
    posts = relationship(
        "Post",
        back_populates="user",  # access through Post.user
    )


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    body = Column(String(255))
    user = relationship(
        "User",
        back_populates="posts",  # access through User.posts
    )
