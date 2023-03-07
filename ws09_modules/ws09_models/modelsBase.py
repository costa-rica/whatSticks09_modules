from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
# from ws09_config import ConfigDev, ConfigProd, ConfigLocal
from .config import config
import os

# if os.environ.get('CONFIG_TYPE')=='local':
#     config = ConfigLocal()
#     print('* modelsBase: Development - Local')
# elif os.environ.get('CONFIG_TYPE')=='dev':
#     config = ConfigDev()
#     print('* modelsBase: Development')
# elif os.environ.get('CONFIG_TYPE')=='prod':
#     config = ConfigProd()
#     print('* modelsBase: Configured for Production')

Base = declarative_base()
engine = create_engine(config.SQL_URI, echo = False, connect_args={"check_same_thread": False})
Session = sessionmaker(bind = engine)
sess = Session()


