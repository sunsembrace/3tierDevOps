#Will hold SQL Alchemy book model and will fill in later for connection to PostgreSQL.

from sqlalchemy import column, Integer, String
from app.database import Base

class Book(base):
    __tablename__ = "books"

id = column(Integer, primary_key =True, index=True)
title = column(String, nullabe=False)
author= column(String, nullable=False)

