from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.models import load_model
from src.components.data_aug import DataAugmentation
from src.entity import DataAugConfig
from src.config.configuration import ConfigurationManager
from src.utils.common import save_json
from pathlib import Path
from src.entity import ModelEvaluationConfig


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