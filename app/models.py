#Will hold SQL Alchemy book model and will fill in later for connection to PostgreSQL.

from sqlalchemy import Column, Integer, String
from app.database import Base

class Book(base):
    __tablename__ = "books"

id = Column(Integer, primary_key=True, index=True)
title = Column(String, nullable=False)
author = Column(String, nullable=False)


