from src.config.configuration import ConfigurationManager
from src.components.Model_evaluation import ModelEvaluation

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