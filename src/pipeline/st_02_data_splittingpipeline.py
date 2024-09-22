from src.components.data_splitting import DataSplitting
from src.config.configuration import ConfigurationManager
from log import logger
from pathlib import Path


class DataSplittingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        split_config = config.get_data_spllitting()
        data_splitter = DataSplitting(config=split_config)
        data_splitter.split_data()


STAGE_NAME = "Data Splitting Stage"

if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Started<<<<<<<<")
        obj = DataSplittingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Completed<<<<<<<<\n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e