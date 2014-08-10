import os

DEBUG = False
SECRET_KEY = 'YOUR-OWN-SECRET'
MAILGUN_KEY = 'foo-bar'
MAILGUN_DOMAIN = 'somegood.org'

db_path = os.path.abspath(os.path.join(os.path.basename(__file__), "../"))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///%s/somegood.db' % (db_path))

SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_POST_LOGIN_VIEW = 'dashboard'
SECURITY_RECOVERABLE = True
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_EMAIL_SENDER = "admin@somegood.org"
SECURITY_DEFAULT_REMEMBER_ME = True
SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to SomeGood.org"

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'postmaster@somegood.org'
MAIL_PASSWORD = 'password'
