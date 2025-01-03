#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import List, Dict
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def add_user(self, email: str, hashed_password: str) -> User:
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
        new_user = User(
            email=email,
            hashed_password=hashed_password
        )
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user by given attributes. Returns the first match found.

        Args:
            **kwargs: The attributes to filter users by.

        Returns:
            User: The first matching User object.

        Raises:
            NoResultFound: If no user is found.
            InvalidRequestError: If invalid attributes are provided.
        """
        if not kwargs:
            raise InvalidRequestError

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except InvalidRequestError as e:
            raise e

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates the attributes of an existing user record based on the provided
        user_id and keyword arguments.

        This method retrieves the user by their ID, and for each key-value pair
        in the provided kwargs, it updates the corresponding attribute of the
        user
        if the attribute exists. After updating the attributes, the changes are
        committed to the database.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs (Dict[str, str]): A dictionary of user attributes to
                                        update, where keys are attribute
                                        names and values are the new values
                                        to set.

        Returns:
            None: The method does not return any value.

        Raises:
            Exception: If an error occurs during the update process, the
                        exception is raised to the caller. Possible
                        exceptions include issues with querying the user
                        or committing changes to the database.
        """
        try:
            # Fetch the user by ID
            user = self.find_user_by(id=user_id)
            if not user:
                raise NoResultFound

            # Update the attributes dynamically based on kwargs
            for key, value in kwargs.items():
                if not hasattr(user, key):
                    # Not a valid attribute
                    raise ValueError
                    # a valid attribute of the user
                setattr(user, key, value)

            # Commit the changes to the database
            self._session.commit()

        except NoResultFound as e:
            # Handle any exceptions that occur and re-raise them
            raise e
        except ValueError as e:
            raise e
