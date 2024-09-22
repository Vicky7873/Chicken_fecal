import os
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity import DataIngestionConfig, DataSplittingConfig,DataAugConfig,ModelBuildingConfig,ModelcheckpointConfig,ModelEvaluationConfig



class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.data_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        # create_directories([config.local_data_file]) -> this peace of code is not working bcoz it create folders and files as directories

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        
        return data_ingestion_config


    def get_data_spllitting(self) -> DataSplittingConfig:
        config = self.config.data_splitting

        create_directories([config.root_dir])

        data_splitting_config = DataSplittingConfig(
            root_dir=config.root_dir,
            raw_data_dir=config.raw_data_dir,
            output_data=config.output_data,
            ratio=self.params.ratio
        )

        return data_splitting_config
    

    def get_data_aug(self) -> DataAugConfig:
        config = self.config.data_aug
        params = self.params.AUGMENTATION

        model_config = DataAugConfig(
            root_dir=config.root_dir,
            train_data= config.train_data,
            test_data=config.test_data,
            val_data=config.val_data,
            train_data_aug=config.train_data_aug,
            test_data_aug=config.test_data_aug,
            val_data_aug=config.val_data_aug,
            horizontal_flip=params.horizontal_flip,
            vertical_flip=params.vertical_flip,
            rotation_range=params.rotation_range,
            zoom_range=params.zoom_range,
            shear_range=params.shear_range,
            width_shift_range=params.width_shift_range,
            height_shift_range=params.height_shift_range,
            target_size=params.target_size
        )

        return model_config
    

    def get_model_building(self) -> ModelBuildingConfig:
        config = self.config.Model_Building
        params = self.params.Model_Building
        model_config_one = ModelBuildingConfig(
            root_dir=config.root_dir,
            model_save=config.model_save,
            units = params.units,
            activation=params.activation,
            input_shape=params.input_shape
        )
        return model_config_one
    


    def get_model_checkpoint_config(self) -> ModelcheckpointConfig:
        config = self.config.Model_Checkpoint
        create_directories([config.root_dir])

        modelcheckpoint_config = ModelcheckpointConfig(
            root_door = config.root_dir,
            model_save= config.model_save,
            monitor = self.params['Model_Checkpoint']['monitor'],
            save_best_only = self.params['Model_Checkpoint']['save_best_only'],
            save_weights_only = self.params['Model_Checkpoint']['save_weights_only'],
            verbose = self.params['Model_Checkpoint']['verbose'],
            patience = self.params['Early_stopping']['patience'],
            restore_best_weights = self.params['Early_stopping']['restore_best_weights'],
            factor= self.params['ReduceLROnPlateau']['factor'],
            min_lr= self.params['ReduceLROnPlateau']['min_lr'],
            existing_model=config.existing_model
        )

        return modelcheckpoint_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.Model_Evaluation
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            score = config.score,
            mlflow_uri='https://dagshub.com/Vicky7873/Chicken_fecal.mlflow',
            all_params=self.params
        )
        return model_evaluation_config