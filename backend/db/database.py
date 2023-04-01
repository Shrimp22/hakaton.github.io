from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = None

SQLALCHEMY_DATABASE_URL = "sqlite:///./hakaton.db"

engine = create_engine(
        # check_same_thread is only needed for SQLite
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()