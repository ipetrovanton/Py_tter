import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'The-World-is-not-enough'
    # обязательно добавить ?check_same_thread=False к app.db, иначе можно немножко очень сильно
    # отхватить головняка
    # при коммитах записей в БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db?check_same_thread=False')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = '1'
    MAIL_USERNAME = 'hoolilogs'
    MAIL_PASSWORD = 'zapvzdafe'
    ADMINS = 'hoolilogs@gmail.com'
    POSTS_PER_PAGE = 3