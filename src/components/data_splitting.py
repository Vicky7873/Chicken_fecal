from src.entity import DataSplittingConfig
from log import logger
import splitfolders

"""
This class is responsible for splitting the data into train, validation, and test sets.
"""

class DataSplitting:
    def __init__(self,config: DataSplittingConfig):
        self.config = config

    def split_data(self):
        raw_data_dir = self.config.raw_data_dir
        output_data = self.config.output_data
        ratio = self.config.ratio
        if isinstance(ratio, str):
            ratio = eval(ratio)
            
        splitfolders.ratio(raw_data_dir, output_data, seed=1337, ratio=tuple(ratio))
        logger.info("Data splitting completed")