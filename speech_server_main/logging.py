'''
Created on 04-Apr-2018

@author: ashwani pandey
'''

import logging
from speech_server_main.config import config

logging.basicConfig(filename="./speech_server_main/logs/deepspeech_server.log", format='%(levelname)s %(asctime)s %(message)s')
def log(message, log_level="warning"):
    
    set_debug = config.ConfigDeepSpeech().get_config("debug")
    if set_debug == "1":
        logging.getLogger(None).setLevel(logging.DEBUG)
    if log_level == "debug":
        logging.debug(message)
    elif log_level == "info":
        logging.info(message)
    elif log_level == "error":
        logging.error(message)
    else:
        logging.warning(message)