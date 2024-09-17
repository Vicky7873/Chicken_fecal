import os
import sys
from pathlib import Path
from log import logger



list_of_dirs = [
     ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"src/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/components/__init__.py",
    f"src/logging/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for dir_path in list_of_dirs:
    dir_path = Path(dir_path) # this will convert the string to Path
    dir_path.parent.mkdir(parents=True, exist_ok=True) # this will make the directory
    if not dir_path.exists(): # this will again check if the directory exists or not if exists then it will not create
        with open(dir_path, 'w') as f: # this will create the file
            pass
        logger.info(f"created {dir_path}")