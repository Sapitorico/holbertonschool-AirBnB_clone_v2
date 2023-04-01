#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine and initialize the database."""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database),
            pool_pre_ping=True
            )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects depending on the class name"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        object_dict = {}
        if cls:
            object_dict = self.__session.query(cls).all()
        else:
            object_dict = self.__session.query(User).all()
            object_dict.extend(self.__session.query(State).all())
            object_dict.extend(self.__session.query(City).all())
            object_dict.extend(self.__session.query(Amenity).all())
            object_dict.extend(self.__session.query(Place).all())
            object_dict.extend(self.__session.query(Review).all())
        result_dict = {"{}.{}".format(obj.__class__.__name__, obj.id): obj for obj in object_dict}
        return result_dict

    def new(self, obj):
        """Add a new object to the database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine,
                         expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """close the connection"""
        self.__session.close()
