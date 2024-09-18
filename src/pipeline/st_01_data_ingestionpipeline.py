from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

class DataIngestionPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_config = config.get_data_ingestion_config()
        data_load_config = DataIngestion(config=data_config)
        data_load_config.download_raw_data()
        data_load_config.extract_zip_file()