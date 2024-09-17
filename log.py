import logging
import os
import sys

log_dir = 'logs'
log_path = os.path.join(log_dir, 'log.txt') # this will join the path logs/log.txt
os.makedirs(log_dir, exist_ok=True) # this will create the directoy

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_path), # Writes logs to a file
                        logging.StreamHandler(sys.stdout) # writes logs in the console
                    ]
                    )
logger = logging.getLogger('chicken_fecal')

logger.info('start of looging')
