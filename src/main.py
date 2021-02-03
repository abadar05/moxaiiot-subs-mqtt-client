#!/usr/bin/env python 3
"""
Subscribe messages from broker
"""

__author__ = "Amjad B."
__license__ = "MIT"
__version__ = '1.0'
__status__ = "beta"


import json
import sys
import logging
from subscribe import MqttBaseCLass

logger = logging.getLogger(__name__)


def read_ext_config():
    """
    Configuration
    """
    try:
        with open("config.json") as json_data_file:
            cfg_obj = json.load(json_data_file)
            logger.debug("Read External Config: {}".format(cfg_obj)) 
            return cfg_obj
    except IOError as e:
        logger.error(e)

obj_ext_configuration = read_ext_config()

def main():

    mqtt = MqttBaseCLass(conf = obj_ext_configuration)
  
    mqtt.init_mqtt_client()
    mqtt.connect_mqtt_broker()
    mqtt.subscribe_mqtt()
    
if __name__ == '__main__':
    main()


