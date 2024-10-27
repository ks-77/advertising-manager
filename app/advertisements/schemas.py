from datetime import date

from pydantic import BaseModel


class SAdvertisement(BaseModel):
    id: int
    description: str
    date_from: date
    date_to: date
    media_file: str
    category_id: int
