#  reference  https://medium.com/@rahulkumar_33287/logger-error-versus-logger-exception-4113b39beb4b


import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.mkdir(logs_path, exist_ok = True)

LOG_FILE_PATH = os.join.path(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO
)

