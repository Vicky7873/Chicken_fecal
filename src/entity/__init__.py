from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataSplittingConfig:
    root_dir: Path
    raw_data_dir: Path
    output_data: Path
    ratio: tuple
    

@dataclass(frozen=True)
class DataAugConfig:
    root_dir: Path
    train_data: Path
    test_data: Path
    val_data: Path
    train_data_aug: Path
    test_data_aug: Path
    val_data_aug: Path
    horizontal_flip: bool
    vertical_flip: bool
    rotation_range: int
    zoom_range: float
    shear_range: float
    width_shift_range: float
    height_shift_range: float
    target_size: tuple

@dataclass(frozen=True)
class ModelBuildingConfig:
    root_dir: Path
    model_save: Path
    units: int
    activation: str
    input_shape: tuple


@dataclass(frozen=True)
class ModelcheckpointConfig:
    root_door: Path
    model_save: Path
    monitor: str
    save_best_only: bool
    save_weights_only: bool
    verbose: int
    patience: int
    restore_best_weights: bool
    factor: float
    min_lr: float
    existing_model: Path


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    score: Path  