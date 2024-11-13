import base64
from datetime import date
from fastapi import APIRouter, Form, UploadFile, File

from app.advertisements.schemas import SAdvertisement, SCategory, SPricing, SCategoryCreate, SPricingCreate
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

@add_router.post("/post/add")
async def add_advertisement(
    description: str = Form(...),
    date_from: date = Form(...),
    date_to: date = Form(...),
    category_id: int = Form(...),
    media_file: UploadFile = File(...),
    owner_username: str = Form(...),
    service: str = Form(...),
):
    media_file_bytes = await media_file.read()
    media_file_coded = base64.b64encode(media_file_bytes).decode('utf-8')

    return await AdvertisementDAO.add(
        description=description,
        date_from=date_from,
        date_to=date_to,
        media_file=media_file_coded,
        category_id=category_id,
        owner_username=owner_username,
        service=service,
    )


@add_router.get("/post/get-all")
async def get_all_advertisements() -> list[SAdvertisement]:
    return await AdvertisementDAO.get_all()

@add_router.get("/post/current")
async def get_current_advertisements() -> list[SAdvertisement]:
    return await AdvertisementDAO.get_current()

@add_router.get("/post/{advertisement_id}")
async def get_advertisement(advertisement_id: int) -> SAdvertisement:
    return await AdvertisementDAO.get_by_id(advertisement_id)


# Category

@category_router.post("/category/add")
async def add_category(category: SCategoryCreate):

    return await CategoryDAO.add(
        name=category.name,
    )

@category_router.get("/category/get-all")
async def get_all_categories() -> list[SCategory]:
    return await CategoryDAO.get_all()

@category_router.get("/category/{category_id}")
async def get_category(category_id: int) -> SCategory:
    return await CategoryDAO.get_by_id(category_id)


# Pricing

@pricing_router.post("/pricing/add")
async def add_pricing(pricing: SPricingCreate):

    return await PricingDAO.add(
        days_from=pricing.days_from,
        days_to=pricing.days_to,
        daily_rate=pricing.daily_rate,
        category_id=pricing.category_id,
    )

@pricing_router.get("/pricing/get-all")
async def get_all_prices() -> list[SPricing]:
    return await PricingDAO.get_all()

@pricing_router.get("/pricing/{pricing_id}")
async def get_pricing(pricing_id: int) -> SPricing:
    return await PricingDAO.get_by_id(pricing_id)
