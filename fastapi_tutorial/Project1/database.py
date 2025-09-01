from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , Session , declarative_base



# Sqlite db

SQLALCHEMY_DATABASE_URL =  "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL 

)

SessionLocal = sessionmaker(autocommit = False ,autoflush=False , bind=engine )
Base = declarative_base()