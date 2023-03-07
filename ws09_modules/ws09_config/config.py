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
        self.DB_ROOT = os.environ.get('DB_ROOT')
        # self.DB_DOWNLOADS = f"{self.WS_ROOT_DB}db_downloads"# <-- commented out until I figure out why we need it?
        self.APPLE_HEALTH_DIR = f"{self.DB_ROOT}apple_health"# <-- store Apple Health compressed
        self.DF_FILES_DIR = f"{self.DB_ROOT}df_files"# <-- store pkl files for dashbaord data item
        self.BLOG_HTML_FILES = f"{self.DB_ROOT}blog_html_files"# <-- store blog word documents
        self.NEWS_HTML_FILES = f"{self.DB_ROOT}news_html_files"# <-- store blog word documents
        
        self.SQL_URI = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME')}"

        #Email stuff
        self.MAIL_SERVER = env_dict.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = env_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = env_dict.get('EMAIL')
        self.MAIL_PASSWORD = env_dict.get('EMAIL_PASSWORD')

        #web Guest
        self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = env_dict.get('GUEST_PASSWORD')

        # Directory Paths
        self.WEB_ROOT = os.environ.get('WEB_ROOT')

        #Location
        self.LOCATION_API_KEY = env_dict.get('LOCATION_API_KEY')
        self.LOCATION_API_URL_BASE = env_dict.get('LOCATION_API_URL_BASE')  

        #Visual crossing - weather history
        self.VISUAL_CROSSING_TOKEN = env_dict.get('VISUAL_CROSSING_TOKEN')
        self.VISUAL_CROSSING_BASE_URL = env_dict.get('VISUAL_CROSSING_BASE_URL')
        self.DAYS_HIST_LIMIT_STD = 30

        #Oura
        self.OURA_API_URL_BASE = env_dict.get('OURA_API_URL_BASE')

        #APPLE_HEALTH
        self.APPLE_HEALTH_CAT_NAMES = env_dict.get('APPLE_HEALTH_CAT_NAMES')
        self.APPLE_SUBPROCESS_ROOT = os.environ.get('APPLE_SUBPROCESS_ROOT')



        #############################
        # Probably not needed ########
        # ############################################
        # # Directory Paths
        # self.API_ROOT = os.environ.get('API_ROOT')

        # #### Sub project directories - WEB ###
        
        # self.SCHED_LOGS_DIR = f"{self.WEB_ROOT}scheduler/"
        # self.WEB_LOGS_DIR = f"{self.WEB_ROOT}web/logs"
        # self.API_LOGS_DIR = f"{self.WEB_ROOT}api/logs"


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()

    DEBUG = True
    # TEMPLATES_AUTO_RELOAD = False
    ## removed 2023-03-06: not clear why I had it but it certainly no good for working on the front end.
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
