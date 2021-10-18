from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_USERNAME = 'root'
SQLALCHEMY_DATABASE_PASSWORD = 'm1nfroy900'
SQLALCHEMY_DATABASE_HOST = 'localhost'
SQLALCHEMY_DATABASE_PORT = '3306'
SQLALCHEMY_DATABASE_DBNAME = 'react_to_do'

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    SQLALCHEMY_DATABASE_USERNAME,
    SQLALCHEMY_DATABASE_PASSWORD,
    SQLALCHEMY_DATABASE_HOST,
    SQLALCHEMY_DATABASE_PORT,
    SQLALCHEMY_DATABASE_DBNAME
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
