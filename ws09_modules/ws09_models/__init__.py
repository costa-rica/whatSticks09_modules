from .modelsMain import login_manager, sess, engine, Base, \
    Users, communityposts, communitycomments, newsposts, newscomments, \
    User_notes, Locations, Weather_history, \
    Oura_token, Oura_sleep_descriptions, User_location_day, \
    Apple_health_steps, Apple_health_export

from ws09_config import ConfigDev, ConfigProd, ConfigLocal
import os


if os.environ.get('CONFIG_TYPE')=='local':
    config = ConfigLocal()
elif os.environ.get('CONFIG_TYPE')=='dev':
    config = ConfigDev()
elif os.environ.get('CONFIG_TYPE')=='prod':
    config = ConfigProd()

########################################################
## Check/make key directories here becuase
## This is one of the first files to fire
if not os.path.exists(os.path.join(config.PROJ_DB_PATH)):
    os.makedirs(os.path.join(config.PROJ_DB_PATH))

# if not os.path.exists(os.path.join(config.DB_DOWNLOADS)):
#     os.makedirs(os.path.join(config.DB_DOWNLOADS))

if not os.path.exists(os.path.join(config.DF_FILES_DIR)):
    os.makedirs(os.path.join(config.DF_FILES_DIR))

if not os.path.exists(os.path.join(config.WORD_DOC_DIR)):
    os.makedirs(os.path.join(config.WORD_DOC_DIR))

if not os.path.exists(os.path.join(config.APPLE_HEALTH_DIR)):
    os.makedirs(os.path.join(config.APPLE_HEALTH_DIR))
##########################################################

print(f'- in ../ws09_modules/ws09_models/__init__.py -')
#Build db
if os.path.exists(os.path.join(config.PROJ_DB_PATH,'ws09.db')):
    print(f'db already exists.')
else:
    Base.metadata.create_all(engine)
    print(f'NEW db created.')
