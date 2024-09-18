from tensorflow.keras.models import Model # type: ignore
from keras.layers import Dense,Flatten # type: ignore
from log import logger
import os
from pathlib import Path
from src.entity import ModelBuildingConfig
from tensorflow.keras.applications.vgg16 import VGG16 # type: ignore

class ModelBuilding:
    def __init__(self, config: ModelBuildingConfig):
        self.config = config

    def Model_Building(self):
        input_shape = tuple(self.config.input_shape)
        model_save = Path(self.config.model_save)

        model_save_dir = model_save.parent

        if not os.path.exists(model_save_dir):
            os.mkdir(model_save_dir)
        
        activation = self.config.activation
        model = VGG16(input_shape=tuple(input_shape), include_top=False, weights='imagenet')
        model.summary()
        for layer in model.layers:
            layer.trainable = False

        # here frezzing the last layers of the model
        x = Flatten()(model.output)
        x = Dense(2, activation=activation)(x)

        model = Model(inputs=model.input, outputs=x)
        model.summary()
        logger.info("Model building completed")
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        model.save(model_save)


        return model