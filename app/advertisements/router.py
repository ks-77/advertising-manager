from fastapi import APIRouter

from app.advertisements.schemas import SAdvertisement
from app.advertisements.dao import AdvertisementDAO


router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)


@router.get("/post/get-all")
async def get_all_advertisements() -> list[SAdvertisement]:
    return await AdvertisementDAO.get_all()


@router.get("/post/{advertisement_id}")
async def get_advertisement(advertisement_id: int) -> SAdvertisement:
    return await AdvertisementDAO.get_by_id(advertisement_id)


@router.get("/post/current/")
async def get_current_advertisements() -> list[SAdvertisement]:
    return await AdvertisementDAO.get_current()
