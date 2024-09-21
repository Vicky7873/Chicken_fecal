from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.models import load_model
from src.components.data_aug import DataAugmentation
from src.entity import DataAugConfig
from src.config.configuration import ConfigurationManager
from src.entity import ModelcheckpointConfig

class Model_train_with_Callbacks:
    def __init__(self,config:ModelcheckpointConfig,data_config: DataAugConfig):
        self.config = config
        self.data_config = data_config

    @staticmethod
    def get_the_model_chceckpoint(self):
        model_check = ModelCheckpoint(
        filepath = self.config.model_save,
        monitor = self.config.monitor,
        verbose = self.config.verbose,
        save_best_only = self.config.save_best_only,
        save_weights_only=self.config.save_weights_only

    )

        early_stopping = EarlyStopping(
            monitor = self.config.monitor,
            patience =self.config.patience,
            verbose = self.config.verbose,
            restore_best_weights = self.config.restore_best_weights
        )

        reduce_lr = ReduceLROnPlateau(
            monitor=self.config.monitor,
            factor=self.config.factor,
            patience=self.config.patience,
            min_lr=self.config.min_lr,
    )
        return [model_check, early_stopping, reduce_lr]
    
    def model_training(self):
        model = load_model(self.config.existing_model)
        model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

        obj = DataAugmentation(config=self.data_config)  
        train_data, test_data, val_data = obj.augment_data()

        cb = self.get_the_model_chceckpoint(self)

        history = model.fit(train_data,epochs=1,validation_data=val_data,callbacks=cb)
        model.save(self.config.model_save)
        history.history
        return history, model