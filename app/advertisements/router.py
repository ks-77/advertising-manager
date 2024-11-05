from datetime import date

from fastapi import APIRouter

from app.advertisements.schemas import SAdvertisement, SCategory, SPricing
from app.advertisements.dao import AdvertisementDAO, CategoryDAO, PricingDAO

add_router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)

category_router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

pricing_router = APIRouter(
    prefix="/prices",
    tags=["prices"],
)

# Advertisements

@add_router.get("/post/get-all")
async def get_all_advertisements() -> list[SAdvertisement]:
    return await AdvertisementDAO.get_all()


@add_router.get("/post/{advertisement_id}")
async def get_advertisement(advertisement_id: int) -> SAdvertisement:
    return await AdvertisementDAO.get_by_id(advertisement_id)


@add_router.get("/post/current/")
async def get_current_advertisements() -> list[SAdvertisement]:
    return await AdvertisementDAO.get_current()


@add_router.post("/post/add/")
async def add_advertisement(description: str, date_from: date, date_to: date, media_file: str, category_id: int):
    return await AdvertisementDAO.add(
        description=description,
        date_from=date_from,
        date_to=date_to,
        media_file=media_file,
        category_id=category_id
    )


# Category

@category_router.get("/category/get-all")
async def get_all_categories() -> list[SCategory]:
    return await CategoryDAO.get_all()


@category_router.get("/category/{category_id}")
async def get_category(category_id: int) -> SCategory:
    return await CategoryDAO.get_by_id(category_id)


# Pricing

@pricing_router.get("/pricing/get-all")
async def get_all_prices() -> list[SPricing]:
    return await PricingDAO.get_all()


@pricing_router.get("/pricing/{pricing_id}")
async def get_pricing(pricing_id: int) -> SPricing:
    return await PricingDAO.get_by_id(pricing_id)
