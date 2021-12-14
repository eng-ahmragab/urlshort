
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config #this will first load the .env file








# create an app instance.
app = Flask(__name__)



#FLASK_ENV: set this to "development" or "production"
app_env = os.environ.get("FLASK_ENV")
config_env = app_env.capitalize()

app.config.from_object(f"config.{config_env}Config")

print("[*] Running app with config:", config_env)






#create flask exension instances
db = SQLAlchemy()

#initialize flask exension instances with the app instance
db.init_app(app)


#import models
from app import models
#Create the db schema: this creates the DB and tables if doesn't exist, then opens it
db.create_all(app=app)


#import the views
from app  import views

