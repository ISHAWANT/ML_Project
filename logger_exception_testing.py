from src.mlProject import logger
from src.mlProject.exception import CustomException 
from src.mlProject.logger import logging 
import sys 

if __name__=='__main__':
    logging.info('start logging')
    try:
        a=1/0
    except Exception as e:
        logging.info("logging completed")
        raise CustomException(e,sys)