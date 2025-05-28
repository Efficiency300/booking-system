from fastapi import FastAPI
from app.api import bookings_router , hotels_router , rooms_router , users_router , auth_router
app = FastAPI()



app.include_router(auth_router)
app.include_router(bookings_router)


app.include_router(hotels_router)
app.include_router(rooms_router)
app.include_router(users_router)

