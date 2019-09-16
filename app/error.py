from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os

if not app.debug:
    print("Авторизован1")
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr=app.config['ADMINS'],
        toaddrs=app.config['ADMINS'],
        subject='MyBlog Errors',
        credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']),
        secure=()
    )
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    # write logs into file
    if not os.path.exists('logs'):
        os.mkdir('logs')
    # write log files (<10 Mb, save last 100 log-files)
    file_handler = RotatingFileHandler('logs/MyBlog.log', maxBytes=9999999,
                                       backupCount=100)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    # level of log event
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('MyBlog startup')