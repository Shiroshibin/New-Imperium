from sqlalchemy.orm import DeclarativeBase, Session

from web_app.settings.constants import ENGINE


class DBSession:
    """
        Контекстный менеджер для соединения с БД.
        При успехе: совершает коммит.
        При неудаче: делает откат изменений и выдаёт ошибку
    """

    def __enter__(self):
        self.session = Session(bind=ENGINE)
        return self.session

    def __exit__(self, *args, **kwargs):
        try:
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()


class Base(DeclarativeBase):
    """Базовый класс для моделей"""

    @classmethod
    def query(cls, *args, **kwargs):
        with DBSession() as db:
            return db.query(cls, *args, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        with DBSession() as db:
            new_object = cls(**kwargs)
            db.add(new_object)
        return cls.query().filter_by(**kwargs).first()

    @classmethod
    def delete(cls, pk: int):
        with DBSession() as db:
            table_object = db.query(cls).get(pk)
            db.delete(table_object)

    @classmethod
    def update(cls, instance_id: int, **kwargs):
        with DBSession() as db:
            table_object = db.query(cls).get(instance_id)
            if table_object:
                for key in kwargs:
                    setattr(table_object, key, kwargs[key])
