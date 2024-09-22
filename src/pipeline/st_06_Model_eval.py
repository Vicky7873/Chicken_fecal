from src.config.configuration import ConfigurationManager
from src.components.Model_evaluation import ModelEvaluation
from log import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_model_evaluation_config()

        data_confog = ConfigurationManager()
        aug_config = data_confog.get_data_aug()

        model_eval = ModelEvaluation(config = eval_config, evl_config = aug_config)
        model_eval.model_evaluate()
        model_eval.save_score()

    

STAGE_NAME = "Model Evaluation Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e