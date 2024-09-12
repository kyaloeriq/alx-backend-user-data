#!/usr/bin/env python3
"""
DB module to manage database interactions, specifically for adding users.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class to handle database interactions for user management."""

    def __init__(self) -> None:
        """Initialize a new DB instance by setting up the SQLite engine and database."""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)  # Reset the database
        Base.metadata.create_all(self._engine)  # Create tables
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object for interacting with the database."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)  # Add the user to the current session
        self._session.commit()  # Commit the session to save the user to the database
        return new_user  # Return the newly created User object
