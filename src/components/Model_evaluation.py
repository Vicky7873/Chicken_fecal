from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.models import load_model
from src.components.data_aug import DataAugmentation
from src.entity import DataAugConfig
from src.config.configuration import ConfigurationManager
from src.utils.common import save_json
from pathlib import Path
from src.entity import ModelEvaluationConfig
import mlflow
import dagshub


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig,evl_config:DataAugmentation):
        self.config = config
        self.data_config = evl_config

    def model_load(self):
        model = load_model(self.config.model_path)
        return model

    def model_evaluate(self):
        model = self.model_load()
        obj = DataAugmentation(self.data_config)
        train_data, test_data, val_data = obj.augment_data()

        self.train_acc = model.evaluate(train_data, verbose=0)[1]
        self.test_acc = model.evaluate(test_data, verbose=0)[1]
        
        print(f"Training Accuracy: {self.train_acc * 100:.2f}%")
        print(f"Testing Accuracy: {self.test_acc * 100:.2f}%")

    def save_score(self):
        scores = {
            "train_acc": self.train_acc,
            "test_acc": self.test_acc
        }
        json_path = self.config.score
        save_json(path = Path(json_path), data = scores)

    def log_model_mlfow(self):

        dagshub.init(repo_owner='Vicky7873', repo_name='Chicken_fecal', mlflow=True)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_experiment("Mlflow Bhiki")

        with mlflow.start_run():
            mlflow.log_metric("train_acc", self.train_acc)
            mlflow.log_artifact(self.config.score)
            

            for param_name, param_value in self.config.all_params.items():
                mlflow.log_param(param_name, param_value)

            # Register the model in the MLflow Model Registry
            model = self.model_load()
            mlflow.keras.log_model(model, "model", registered_model_name="VGG16Model")
            
            # Logging the model as an artifact
            mlflow.keras.log_model(model, "model")