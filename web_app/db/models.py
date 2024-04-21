from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .database import Base
from web_app.settings.constants import ENGINE


class User(Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, index=True, autoincrement=True)
    phone = sa.Column(sa.String(15), unique=True, nullable=False)
    telegram_id = sa.Column(sa.BigInteger, unique=True, nullable=False)
    is_admin = sa.Column(sa.Boolean, default=False, nullable=False)
    is_active = sa.Column(sa.Boolean, default=False, nullable=False)

    profile = relationship("Profile", overlaps="user")
    applications = relationship("Application", overlaps="user")
    first_meets = relationship("Meet", foreign_keys="[Meet.first_user_id]", overlaps="first_user")
    second_meets = relationship("Meet", foreign_keys="[Meet.second_user_id]", overlaps="second_user")


class Profile(Base):
    __tablename__ = "profile"

    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), primary_key=True, index=True)
    last_name = sa.Column(sa.String(150), nullable=False)
    first_name = sa.Column(sa.String(100), nullable=False)
    job_title = sa.Column(sa.String(255), nullable=False)
    born_date = sa.Column(sa.Date(), nullable=False)

    user = relationship("User", overlaps="profile")


class Application(Base):
    __tablename__ = "application"

    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), primary_key=True, index=True)
    duration = sa.Column(sa.String(2), nullable=False)
    format = sa.Column(sa.String(10), nullable=False)

    user = relationship("User", overlaps="applications")


class Meet(Base):
    __tablename__ = "meet"

    id = sa.Column(sa.Integer, primary_key=True, index=True, autoincrement=True)
    first_user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), nullable=False)
    second_user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), nullable=False)
    first_user_confirm = sa.Column(sa.Boolean, nullable=False, default=False)
    second_user_confirm = sa.Column(sa.Boolean, nullable=False, default=False)
    first_user_rating = sa.Column(sa.String(1), nullable=True)
    second_user_rating = sa.Column(sa.String(1), nullable=True)
    duration = sa.Column(sa.String(10), nullable=False)
    format = sa.Column(sa.String(10), nullable=False)
    meet_date = sa.Column(sa.DateTime, nullable=False, default=datetime.now)

    first_user = relationship("User", foreign_keys="[Meet.first_user_id]", overlaps="first_meets")
    second_user = relationship("User", foreign_keys="[Meet.second_user_id]", overlaps="second_meets")


if __name__ == "__main__":
    try:
        # создаем таблицы
        Base.metadata.create_all(bind=ENGINE)
        print("База данных и таблицы созданы успешно!")
    except Exception as create_tables_error:
        raise create_tables_error
