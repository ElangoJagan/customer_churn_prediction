import logging
import os
from datetime import datetime
from typing import Dict 

class Logger:
    
    """
    Logger class with Singleton pattern.
    Ensures only ONE logger instance per module name.

    New OOP Concept Learned: Singleton Pattern
    → _instances dict stores already created loggers
    → If logger exists, return same one (no duplicate!)
    → If logger doesn't exist, create new one and store it
    
    Usage:
        _logger_obj = Logger("data_ingestion")
        logger = _logger_obj.get_logger()
    """
    
    
    # Class variable — shared across ALL instances
    # This is what makes Singleton work!
    
    _instances:Dict[str,logging.Logger]={}
    
    def __init__(self, name:str)->None:
        
        """
        Initialize Logger with a name.

        Args:
            name: Name of the logger (usually filename)
        """
        self.name = name
        self.log_dir = 'logs'
        self.log_file= self._get_log_file_path()
        
    def _get_log_file_path(self)->str:
        
        """
        Creates logs directory and returns log file path
        with current date as filename
        Returns:
            Full path to log file
        """
        os.makedirs(self.log_dir, exist_ok= True)
        log_filename = f'{datetime.now().strftime('%Y_%m_%d')}.log'
        return os.path.join(self.log_dir, log_filename)
    
    def _setup_logger(self)->logging.Logger:
        """
        Sets up logger with file and console handlers.

        Returns:
            Configured logger instance
        """
        
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        
        #Format for Log messages
        formatter = logging.Formatter(
            "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        #File handler -> saves logs to file
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        #Consolde handler -> shows logs in terminal
        console_handler= logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        #Add both handlers  to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def get_logger(self)->logging.Logger:
        """
        Returns logger instance using Singleton pattern.
        Creates new logger only if it doesn't exist yet.

        Returns:
            Logger instance
        """
        
        # Singleton check!
        # If logger already exists → return same one
        # If logger doesn't exist → create new one
        
        if self.name not in  Logger._instances:
            Logger._instances[self.name]=self._setup_logger()
        return Logger._instances[self.name]
        
        