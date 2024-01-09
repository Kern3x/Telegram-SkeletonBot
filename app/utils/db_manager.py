from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import config


base_config = config.get("base")


class DBManager:
    Base = declarative_base()
    Session = sessionmaker()
    engine = create_engine(base_config.DB_URL)

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)
