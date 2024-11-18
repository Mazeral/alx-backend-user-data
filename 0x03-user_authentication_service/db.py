"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import TypeVar, List
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> UserType:
        """
        Adds a new user to the database with the provided email and hashed
        password.

        Args:
            email (str): The email address of the user.
            hashed_password (str): The hashed password for the user.

        Returns:
            UserType: The newly created User object.

        Raises:
            Exception: If an error occurs while adding the user to the
            database.
        """
        try:
            new_user = User(
                email=email,
                hashed_password=hashed_password
            )
            self._session.add(new_user)
            self._session.commit()
            self._session.refresh(new_user)
            return new_user
        except Exception as e:
            raise e

    def find_user_by(self, **kwargs) -> List[UserType]:
        """
        Finds a user by given attributes. Returns the first match found.

        Args:
            **kwargs: The attributes to filter users by.

        Returns:
            List[UserType]: A list of matching User objects.

        Raises:
            Exception: If an error occurs while querying the database.
        """
        try:
            if kwargs:
                user = self._session.query(User).filter_by(**kwargs).one()
                return [user]
        except Exception as e:
            raise e
