from src.components.model_building import ModelBuilding
from src.config.configuration import ConfigurationManager
from log import logger

class ModelBuildingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_config = config.get_model_building()
        model_build = ModelBuilding(config=model_config)
        model_build.Model_Building()