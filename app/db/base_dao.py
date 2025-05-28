from app.db import async_session_maker
from sqlalchemy import  select , insert


class BaseDao:
    model=None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__)
            res = await session.execute(query)
            return res.mappings().all()


    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__).filter_by(id=model_id)
            res = await session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    async def find_by_name(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__).filter_by(**filter_by)
            res = await session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model.__table__).values(**data)
            await session.execute(query)
            await session.commit()




