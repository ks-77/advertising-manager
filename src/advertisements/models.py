from src.database import Base
from sqlalchemy import Column, Integer, String, Date


class Advertisement(Base):
    __tablename__ = 'advertisements'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    media_file = Column(String)
