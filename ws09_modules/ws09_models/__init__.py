from .modelsMain import login_manager, sess, engine, text, Base, \
    Users, communityposts, communitycomments, newsposts, newscomments, \
    User_notes, Locations, Weather_history, \
    Oura_token, Oura_sleep_descriptions, User_location_day, \
    Apple_health_steps, Apple_health_export

import os


############################################################################
## This is one of the first files to execute so make dirs here

if not os.path.exists(os.environ.get('DB_ROOT')):
    os.makedirs(os.environ.get('DB_ROOT'))

if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"df_files")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"df_files"))

if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"apple_health")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"apple_health"))

#######################################################################################
## NOTE: Unsure if needed since html files will be stored in templates directory ##
if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"blog_html_files")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"blog_html_files"))

if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"news_html_files")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"news_html_files"))

######################################################################################

##########################################################

print(f'- in ../ws09_modules/ws09_models/__init__.py -')
#Build db
if os.path.exists(os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))):
    print(f'db already exists.')
else:
    Base.metadata.create_all(engine)
    print(f'NEW db created.')
