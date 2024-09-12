#!/usr/bin/env python3
"""
Module defines the User model for the 'users' table using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User model mapped to the 'users' table in the database
    """
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

# After defining the model, you can use Base.metadata.create_all(engine) to create the table in the database.
