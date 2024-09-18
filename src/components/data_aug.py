from log import logger
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img # type: ignore
import numpy as np
from pathlib import Path
from src.entity import DataAugConfig

# from keras.preprocessing.image import ImageDataGenerator
class DataAugmentation:
    def __init__(self,config:DataAugConfig):
        self.config = config

    def augment_data(self):

        for path in [
            self.config.train_data_aug,
            self.config.test_data_aug,
            self.config.val_data_aug
        ]:
            Path(path).mkdir(parents=True, exist_ok=True)

        train_data= self.config.train_data
        test_data=self.config.test_data
        val_data=self.config.val_data
        train_data_aug=self.config.train_data_aug
        test_data_aug=self.config.test_data_aug
        val_data_aug=self.config.val_data_aug
        horizontal_flip=self.config.horizontal_flip
        vertical_flip=self.config.vertical_flip
        rotation_range=self.config.rotation_range
        zoom_range=float(self.config.zoom_range)
        shear_range=self.config.shear_range
        width_shift_range=self.config.width_shift_range
        height_shift_range=self.config.height_shift_range
        target_size=tuple(self.config.target_size)

        train_datagen = ImageDataGenerator(
            rescale=1./255,
            horizontal_flip=horizontal_flip,
            vertical_flip=vertical_flip,
            rotation_range=rotation_range,
            zoom_range=zoom_range,
            shear_range=shear_range,
            width_shift_range=width_shift_range,
            height_shift_range=height_shift_range
        )

        test_datagen = ImageDataGenerator(
            rescale=1./255
        )

        val_datagen = ImageDataGenerator(
            rescale=1./255
        )

        train_data_aug = train_datagen.flow_from_directory(
            train_data,
            target_size=target_size
        )

        test_data_aug = test_datagen.flow_from_directory(
            test_data,
            target_size=target_size
        )

        val_data_aug = val_datagen.flow_from_directory(
            val_data,
            target_size=target_size
        )

        return train_data_aug, test_data_aug, val_data_aug
    
        

