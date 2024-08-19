import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s]')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "store_index.py",
    "static",
    "templates/chat.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    #seperate file and folders
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info (f" Created dir : {filedir} now creating {filename} ")
    if ( not os.path.exists (filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as f:
            pass
        logging.info (f" Creating file: {filepath}  ")
    else:
        logging.info(f" {filename} already exists ")
