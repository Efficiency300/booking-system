from app.db import Bookings
from app.db import Rooms
from app.db import BaseDao
from app.db.database import async_session_maker
from sqlalchemy import select, and_, or_, func , insert
from datetime import date

class BookingsDao(BaseDao):
    model = Bookings

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            # Подзапрос: забронированные комнаты, пересекающиеся по дате
            booked_rooms = (
                select(Bookings.room_id)
                .where(
                    and_(
                        Bookings.room_id == room_id,
                        or_(
                            and_(Bookings.date_from >= date_from, Bookings.date_from < date_to),
                            and_(Bookings.date_from <= date_from, Bookings.date_to > date_to)
                        )
                    )
                )
                .subquery()  # <-- ЭТО ОБЯЗАТЕЛЬНО
            )

            # Главный запрос: сколько свободных мест в комнате
            rooms_quantity = (
                select(
                    (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('quantity')
                )
                .outerjoin(booked_rooms, booked_rooms.c.room_id == Rooms.id)
                .where(Rooms.id == room_id)
                .group_by(Rooms.id, Rooms.quantity)
            )

            result = await session.execute(rooms_quantity)
            rooms_left = result.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()

                add_booking = (
                    insert(Bookings)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(
                        Bookings.id,
                        Bookings.user_id,
                        Bookings.room_id,
                        Bookings.date_from,
                        Bookings.date_to,
                    )
                )

                new_booking = await session.execute(add_booking)
                await session.commit()
                row = new_booking.mappings().one()
                return row

