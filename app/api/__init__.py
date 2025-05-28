from .endpoints.bookings import router as bookings_router
from .endpoints.hotels import router as hotels_router
from .endpoints.rooms import router as rooms_router
from .endpoints.users import router as users_router
from .endpoints.auth import router as auth_router

__all__ = ["bookings_router", "hotels_router", "rooms_router", "users_router", "auth_router"]