#!/usr/bin/env python3
"""
DB module to manage database interactions, specifically for adding users.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from user import Base, User


class DB:
    """DB class to handle database interactions for user management."""

    def __init__(self) -> None:
        """Initialize a new DB instance by setting up the SQLite"""
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
        self._session.commit()
        return new_user  # Return the newly created User object
    
    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments in the database.
        """
        try:
            # Query the users table with the provided keyword arguments
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound  # Raise if no user was found
            return user
        except NoResultFound:
            # Reraise NoResultFound if no matching user is found
            raise
        except InvalidRequestError:
            # Reraise InvalidRequestError if an invalid query is formed
            raise
        except Exception as e:
            # Catch any other exception and raise an InvalidRequestError
            raise InvalidRequestError from e
