from src.components.data_splitting import DataSplitting
from src.config.configuration import ConfigurationManager
from log import logger

class DataSplittingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        split_config = config.get_data_spllitting()
        data_splitter = DataSplitting(config=split_config)
        data_splitter.split_data()