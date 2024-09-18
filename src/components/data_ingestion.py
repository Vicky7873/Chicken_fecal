import zipfile
import os
import glob
import gdown
from log import logger
from src.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    def download_raw_data(self):
        source_url = self.config.source_URL
        file_id = source_url.split("/")[-2]
        prefix = 'https://drive.google.com/uc?/export=download&id='
        output_path = self.config.local_data_file
        local_data_dir = Path(output_path).parent
        if not os.path.exists(local_data_dir):
            os.makedirs(local_data_dir)
        gdown.download(prefix+file_id, output_path)
        logger.info(f"raw data downloaded at: {output_path}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        if not os.path.exists(unzip_path):
            os.makedirs(unzip_path)
        logger.info(f" creating directory: {unzip_path}")
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"zip file extracted at: {unzip_path}")
        
