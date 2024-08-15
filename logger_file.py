import logging
from logging.handlers import TimedRotatingFileHandler

import os


class Setuplogger:
    def __init__(self, year, folder_name):
        # Create log file if not present in the Logs directory
        curr_dir = os.getcwd()

        log_parent_dir = os.path.join(curr_dir, "Logs")
        if not os.path.exists(log_parent_dir):
            os.makedirs(log_parent_dir)

        file_log_year_dir = os.path.join(log_parent_dir, str(year))
        if not os.path.exists(file_log_year_dir):
            os.makedirs(file_log_year_dir)

        file_log_folder_dir = os.path.join(file_log_year_dir, folder_name)
        if not os.path.exists(file_log_folder_dir):
            os.makedirs(file_log_folder_dir)

        self.logPath = os.path.join(
            file_log_folder_dir, f"Zipher_{year}_{folder_name}.log"
        )

        with open(self.logPath, "w"):
            pass

    def createLogger(self):
        # Create a logging object
        logger = logging.getLogger()
        if not logger.hasHandlers():
            # Create a TimedRotatingFileHandler object for creating and writing into new logfile after midnight
            handler = TimedRotatingFileHandler(
                self.logPath, when="midnight", interval=2
            )

            # Setup the format of log
            format = "%(asctime)s :: %(msecs)d :: [%(filename)s :: %(lineno)d] :: %(levelname)s :: %(message)s"
            formatter = logging.Formatter(fmt=format, datefmt="%m-%d-%y-%H:%M:%S")

            handler.setFormatter(formatter)
            # handler.setLevel(logging.INFO)

            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

        return logger
