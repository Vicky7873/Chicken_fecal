# Chicken_fecal

1. Create an ENV
conda create -n chkn python=3.12 -y
2. activate the env
cmd: conda activate chkn
3. create an temp.py
cmd: touch temp.py -> having project str
4. create requirements.txt
cmd: touch requirements.txt
cmd: pip install -r requirements.txt
5. declare src as a package
setup.py
6. Data Ingestion EXP and modular coding added
7. Splitting the data set



# Workflows
 1. Update config.yaml
here we will store the config things example data set path to get the data/store the data etc
2. Update params.yaml
3. Update entity
entity is nothing but the return type of a function
entity where we just store the data paths only, once configuration manager will execute then it will return the and store the data as per the entity data storage path
4. Update the configuration manager in src config
configuration manager where we will read the config/params yaml and and return the data to the entity folder, this will used in pipeline 
5. update the components
this .py file will zip unzip the data and store the data into the respective folder, once the configuration manager will execute then it will return the and store the data as per the entity data storage path
6. update the pipeline

7. update the main.py
to run the pipe line we need write the pieace of code
8. update the app.py

