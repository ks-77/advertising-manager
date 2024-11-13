from app.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, and_
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    pricing = relationship('Pricing', back_populates='category', cascade='all, delete-orphan')

    advertisements = relationship('Advertisement', back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Category(name={self.name})"


class Pricing(Base):
    __tablename__ = 'pricing'

    id = Column(Integer, primary_key=True)
    days_from = Column(Integer, nullable=False)
    days_to = Column(Integer, nullable=False)
    daily_rate = Column(Integer, nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='pricing')

    def __repr__(self):
        return (
            f"Pricing(days_from={self.days_from}, "
            f"days_to={self.days_to}, "
            f"daily_rate={self.daily_rate}, "
            f"category={self.category.name})"
        )


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    media_file = Column(String, nullable=False)
    owner_username = Column(String, nullable=False)
    service = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='advertisements')

    @property
    def days_count(self):
        return (self.date_to - self.date_from).days + 1

    async def price(self, session: AsyncSession):
        if self.date_from and self.date_to and self.category:
            days = self.days_count

            query = select(Pricing).where(
                and_(
                    Pricing.category_id == self.category_id,
                    Pricing.days_from <= days,
                    Pricing.days_to >= days
                )
            )

            result = await session.execute(query)
            pricing = result.scalars().first()

            if pricing:
                return days * pricing.daily_rate
            return 0
