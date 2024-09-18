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
    