import os
import sys
import pandas as pd
import joblib
from typing import Any, Dict

from src.logger import Logger
from exception import CustomException

_logger_obj = Logger('Utils')
logger = _logger_obj.get_logger()

def save_object(file_path, obj):
    """
    Saves any Python object (model, preprocessor) to disk
    using joblib serialization.

    Args:
        file_path: Path where object should be saved
        obj: Python object to save (model, preprocessor etc)
    """
    try:
        logger.info('Save Object Started')
        dir_path = os.dirname(file_path)
        os.makedirs(dir_path, exist_ok= True)
        
        logger.info('saving obj to filepath: {file_path}')
        joblib.dump(obj, file_path)
        logger.info('object saved')
        
    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path):
    
    """
    Loads a saved Python object from disk.

    Args:
        file_path: Path of the saved object

    Returns:
        Loaded Python object
    """
    try:
        obj= joblib.load(file_path)
        return obj
    
    except Exception as e:
        raise CustomException(e,sys)
    
