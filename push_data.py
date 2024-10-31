import os
import sys
import json

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

import certifi
ca = certifi.where()

import pandas as pd 
import numpy as numpy
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):

        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb (self,records,database,collection):
        try : 

            mongo_client = pymongo.MongoClient(mongo_uri)
            db = mongo_client[database]
            col = db[collection]
            col.insert_many(records)

            return len(records)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == "__main__":

    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "NS"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)

    print(no_of_records)






