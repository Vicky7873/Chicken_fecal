from src.components.data_aug import DataAugmentation
from src.config.configuration import ConfigurationManager

class DataAugPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_aug_config = config.get_data_aug()
        data_au = DataAugmentation(config=data_aug_config)
        data_au.augment_data()