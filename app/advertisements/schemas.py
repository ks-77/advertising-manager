from datetime import date

from fastapi import File, UploadFile
from pydantic import BaseModel


class SAdvertisement(BaseModel):
    id: int
    description: str
    date_from: date
    date_to: date
    media_file: str
    category_id: int


class SCategory(BaseModel):
    id: int
    name: str


class SPricing(BaseModel):
    id: int
    days_from: int
    days_to: int
    daily_rate: int
    category_id: int


class SCategoryCreate(BaseModel):
    name: str


class SPricingCreate(BaseModel):
    days_from: int
    days_to: int
    daily_rate: int
    category_id: int