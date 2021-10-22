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

engine = create_engine(
    'mysql://b59d42804a0a0c:684d3aba@us-cdbr-east-04.cleardb.com:3306/heroku_05f8632f076a9b3', connect_args={'connect_timeout': 10})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
