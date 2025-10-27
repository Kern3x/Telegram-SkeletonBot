from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import config


base_config = config.get("base")


class DBManager:
    Base = declarative_base()
    engine = create_engine(base_config.DB_URL)
    Session = sessionmaker(bind=engine)

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)
