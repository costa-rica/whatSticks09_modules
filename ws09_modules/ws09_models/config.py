import os
from ws09_config import ConfigDev, ConfigProd, ConfigLocal

if os.environ.get('CONFIG_TYPE')=='local':
    config = ConfigLocal()
    print('* modelsBase: Development - Local')
elif os.environ.get('CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('* modelsBase: Development')
elif os.environ.get('CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('* modelsBase: Configured for Production')