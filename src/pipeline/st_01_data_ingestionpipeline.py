from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from log import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_config = config.get_data_ingestion_config()
        data_load_config = DataIngestion(config=data_config)
        data_load_config.download_raw_data()
        data_load_config.extract_zip_file()

# this particular peace of code is to run the dvc.yaml
if  __name__  =="__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Started<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Completed<<<<<<<<\n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e