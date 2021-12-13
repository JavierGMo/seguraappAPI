#Aqui tienes que colocar tus credenciales de tu base de datos
from .default import *


APP_ENV = APP_ENV_PRODUCTION
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tu_userdb:tu_passworddb@localhost/tu_DB'
