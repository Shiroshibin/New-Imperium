from .database import Base


class User(Base):
    __tablename__ = "user"


class Profile(Base):
    __tablename__ = "profile"


class Application(Base):
    __tablename__ = "application"


class Meet(Base):
    __tablename__ = "meet"
