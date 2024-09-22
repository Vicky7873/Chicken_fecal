from src.components.data_aug import DataAugmentation
from src.config.configuration import ConfigurationManager
from log import logger

class DataAugPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_aug_config = config.get_data_aug()
        data_au = DataAugmentation(config=data_aug_config)
        data_au.augment_data()

STAGE_NAME = "Data Augmentation Stage"
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Started<<<<<<<<")
        obj = DataAugPipeline()
        obj.main()
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Completed<<<<<<<<\n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e