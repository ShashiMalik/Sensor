from sensor_package.exception import SensorException
import os
import sys
from sensor_package.logger import logging


def test_exception():   
    try:
        logging.info("Error occured")
        a =1/0
    except Exception as e:
        raise SensorException(e,sys)
        #raise e

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)