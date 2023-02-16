import os
import json
from dotenv import load_dotenv

load_dotenv()


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
    env_dict = json.load(env_file)


class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = env_dict.get('SECRET_KEY')


        self.WS_API_PASSWORD = env_dict.get('WS_API_PASSWORD')
        
        # DB references: dirs created by ws09_models
        self.PROJ_DB_PATH = os.environ.get('PROJ_DB_PATH')
        # self.DB_DOWNLOADS = f"{self.WS_ROOT_DB}db_downloads"# <-- commented out until I figure out why we need it?
        self.APPLE_HEALTH_DIR = f"{self.PROJ_DB_PATH}apple_health"# <-- store Apple Health compressed
        self.DF_FILES_DIR = f"{self.PROJ_DB_PATH}df_files"# <-- store pkl files for dashbaord data item
        self.WORD_DOC_DIR = f"{self.PROJ_DB_PATH}word_docs"# <-- store blog word documents
        
        self.SQL_URI = f"sqlite:///{self.PROJ_DB_PATH}ws09.db"

        #############################
        # Unused for ws09 ...so far #
        #############################

        # #Email stuff
        # self.MAIL_SERVER = env_dict.get('MAIL_SERVER_MSOFFICE')
        # self.MAIL_PORT = env_dict.get('MAIL_PORT')
        # self.MAIL_USE_TLS = True
        # self.MAIL_USERNAME = env_dict.get('EMAIL')
        # self.MAIL_PASSWORD = env_dict.get('EMAIL_PASSWORD')
        # #web Guest
        # self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        # self.GUEST_PASSWORD = env_dict.get('GUEST_PASSWORD')


        # #Location
        # self.LOCATION_API_KEY = env_dict.get('LOCATION_API_KEY')
        # self.LOCATION_API_URL_BASE = env_dict.get('LOCATION_API_URL_BASE')

        # #Oura
        # self.OURA_API_URL_BASE = env_dict.get('OURA_API_URL_BASE')
        
        # #Visual crossing - weather history
        # self.VISUAL_CROSSING_TOKEN = env_dict.get('VISUAL_CROSSING_TOKEN')
        # self.VISUAL_CROSSING_BASE_URL = env_dict.get('VISUAL_CROSSING_BASE_URL')
        # self.DAYS_HIST_LIMIT_STD = 30

        # #APPLE_HEALTH
        # self.APPLE_HEALTH_CAT_NAMES = env_dict.get('APPLE_HEALTH_CAT_NAMES')

        # ############################################
        # # Directory Paths
        # self.WS_ROOT_WEB = os.environ.get('WS_ROOT_WEB')
        # self.WS_ROOT_API = os.environ.get('WS_ROOT_API')


        # #### Previously in child config classes ####
        # # DB references 
        # self.SQL_URI = f"sqlite:///{self.WS_ROOT_DB}ws09.db"




        # #### Sub project directories - WEB ###
        # self.APPLE_SUBPROCESS_DIR = f"{self.WS_ROOT_WEB}apple_service"
        # self.SCHED_LOGS_DIR = f"{self.WS_ROOT_WEB}scheduler/"
        # self.WEB_LOGS_DIR = f"{self.WS_ROOT_WEB}web/logs"
        # self.API_LOGS_DIR = f"{self.WS_ROOT_WEB}api/logs"


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = False
    SCHED_CONFIG_STRING = "ConfigLocal"
    USERS_TESTING_OURA = True
    WS_API_URL_BASE = env_dict.get('WS_API_URL_BASE_LOCAL')


class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

    DEBUG = True
    SQL_URI = env_dict.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    SCHED_CONFIG_STRING = "ConfigDev"
    USERS_TESTING_OURA = False
    WS_API_URL_BASE = env_dict.get('WS_API_URL_BASE_DEVELOPMENT')


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SCHED_CONFIG_STRING = "ConfigProd"
    USERS_TESTING_OURA = False
    WS_API_URL_BASE = env_dict.get('WS_API_URL_BASE_PRODUCTION')


# if os.environ.get('CONFIG_TYPE')=='local':
#     config = ConfigLocal()
#     print('- whatSticks09/ws09_config/config.py: Development - Local')
#     print("config.GUEST_EMAIL")
#     print(config.GUEST_EMAIL)
# elif os.environ.get('CONFIG_TYPE')=='dev':
#     config = ConfigDev()
#     print('- whatSticks09/ws09_config/config.py: Development')
# elif os.environ.get('CONFIG_TYPE')=='prod':
#     config = ConfigProd()
#     print('- whatSticks09/ws09_config/config.py: Configured for Production')