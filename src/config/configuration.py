import os
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity import DataIngestionConfig, DataSplittingConfig



class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.data_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        # create_directories([config.local_data_file]) -> this peace of code is not working bcoz it create folders and files as directories

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        
        return data_ingestion_config


    def get_data_spllitting(self) -> DataSplittingConfig:
        config = self.config.data_splitting

        create_directories([config.root_dir])

        data_splitting_config = DataSplittingConfig(
            root_dir=config.root_dir,
            raw_data_dir=config.raw_data_dir,
            output_data=config.output_data,
            ratio=self.params.ratio
        )

        return data_splitting_config