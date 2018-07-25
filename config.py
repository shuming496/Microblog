import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODEFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [("shuming496", "shuming496@aliyun.com")]

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    POSTS_PER_PAGE = 3

    LANGUAGES = ['en', 'es']

    YOUDAO_TRANSLATOR_APPKEY = os.environ.get('YOUDAO_TRANSLATOR_APPKEY')
    YOUDAO_TRANSLATOR_SECRETKEY = os.environ.get('YOUDAO_TRANSLATOR_SECRETKEY')
