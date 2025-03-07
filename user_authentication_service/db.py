#!/usr/bin/env python3
"""DB module
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base
from user import User


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
        """ add new user to DB """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ find user by keyword arguments """
        if not kwargs:
            raise InvalidRequestError("Invalid")

        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("Not found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid")

    def update_user(self, user_id: int, **kwargs) -> None:
        """ updates the user """
        user = self.find_user_by(id=user_id)

        valid_attributes = ['email',
                            'hashed_password',
                            'session_id',
                            'reset_token']
        for key in kwargs:
            if key not in valid_attributes:
                raise ValueError(f"Invalid attribute: {key}")

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()
