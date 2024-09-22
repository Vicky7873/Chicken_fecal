
from src.config.configuration import ConfigurationManager
from src.components.Model_with_callbacks import Model_train_with_Callbacks
from log import logger

class FinalModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            mo_one = config.get_model_checkpoint_config()
            
            # Fetch the data augmentation configuration
# Assuming this gets the data config
            c_2 = config.get_data_aug()  # Fetch the data augmentation config
            
            # Pass both model checkpoint config and data augmentation config
            mo_two = Model_train_with_Callbacks(config=mo_one, data_config=c_2)  
            mo_two.model_training()
        except Exception as e:
            raise e
        
STAGE_NAME = "Final Model Training Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = FinalModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

        