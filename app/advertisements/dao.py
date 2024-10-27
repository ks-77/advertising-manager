from app.advertisements.models import Advertisement, Pricing, Category
from app.dao.base import BaseDAO


class CategoryDAO(BaseDAO):
    model = Category


class PricingDAO(BaseDAO):
    model = Pricing


class AdvertisementDAO(BaseDAO):
    model = Advertisement
