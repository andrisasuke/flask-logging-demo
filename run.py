from flask import Flask, jsonify
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app_logger = logging.getLogger('flask-logging-demo')
file_handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=1)
handler = logging.StreamHandler()
file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s ,%(module)s:%(lineno)d'
    ))
handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(message)s ,%(module)s:%(lineno)d'
    ))
app_logger.addHandler(file_handler)
app_logger.addHandler(handler)
app_logger.setLevel(logging.DEBUG)

@app.route('/log')
def log_demo():
    app_logger.debug('this is debug log')
    app_logger.info('this is info log')
    app_logger.error('this is error log')
    return jsonify(message='Ok')

if __name__ == '__main__':
    app.run()