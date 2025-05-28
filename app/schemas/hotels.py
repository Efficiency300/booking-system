from pydantic import BaseModel, ConfigDict
from typing import List


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    service: List[str]
    rooms_quantity: int
    image_id: int

    model_config = ConfigDict(from_attributes=True)