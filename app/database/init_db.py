from config import config
from app.utils.db_manager import DBManager

# import models by --  from app.models import ...


dev_config = config.get("development")


class DataController:
    def __init__(self) -> None:
        self.models = dict()
        self.db_manager = DBManager()

    def add_new(self, model, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            session.add(self.models.get(model)(**kwargs))
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def get_first(self, model, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            return session.query(self.models.get(model)).filter_by(**kwargs).first()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def get_all(self, model, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            return session.query(self.models.get(model)).filter_by(**kwargs).all()
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def get_count(self, model):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            return session.query(self.models.get(model)).count()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def edit_first(self, model, values: dict, operation=None, oper_val=None, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            record = session.query(self.models.get(model)).filter_by(**kwargs).first()

            for key, value in values.items():
                current_value = getattr(record, key)

                if operation == "+":
                    setattr(record, key, current_value + oper_val)

                elif operation == "-":
                    setattr(record, key, current_value - oper_val)

                else:
                    setattr(record, key, value)

            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def delete_first(self, model, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            session.query(self.models.get(model)).filter_by(**kwargs).delete()
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def edit_all(self, model, values: dict, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            session.query(self.models.get(model)).filter_by(**kwargs).update(values)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()

    def delete_all(self, model, **kwargs):
        session = self.db_manager.Session(bind=self.db_manager.engine)

        try:
            session.query(self.models.get(model)).filter_by(**kwargs).delete()
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
