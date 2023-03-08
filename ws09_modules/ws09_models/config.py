import os
from ws09_config import ConfigDev, ConfigProd, ConfigLocal

if os.environ.get('CONFIG_TYPE')=='local':
    config = ConfigLocal()
    print('- ws09_models/config: Local')
elif os.environ.get('CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('- ws09_models/config: Development')
elif os.environ.get('CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('- ws09_models/config: Production')