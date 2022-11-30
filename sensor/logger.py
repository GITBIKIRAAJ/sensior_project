import logging
import os
from datetime import datetime
import os

#logfile name
Logfile_name= f"{datetime.now().strftime('%m%d%Y__%H_%M_%S')}.log"

Log_file_dir = os.path.join(os.getcwd(),"logs")

#created a folder if not availabe
os.makedirs(Log_file_dir,exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(Log_file_dir,Logfile_name)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)


