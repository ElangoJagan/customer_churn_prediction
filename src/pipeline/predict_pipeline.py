import sys
from abc import ABC, abstractmethod
from typing import Dict, Any
import pandas as pd
import numpy as np

from src.logger import Logger
from src.exception import CustomException
from src.utils import load_object
from src.entity.config_entity import DataTransformationConfig, ModelTrainerConfig

_logger_obj = Logger("PredictPipeline")
logger = _logger_obj.get_logger()

class BasePipeline(ABC):
    """
    Abstract Base Class — defines the contract that
    ANY prediction pipeline MUST follow.

    New OOP Concept Learned: ABC (Abstract Base Class)
    → abstractmethod forces child classes to implement predict()
    → ensures consistency across the project!
    """
    
    @abstractmethod
    def predict(self,input_data): 
        """Every pipeline MUST implement this method."""
        pass

class PredictPipeline(BasePipeline):
    """
    Loads saved model and preprocessor, makes predictions
    on new customer data.
    """
    def __init__(self):
        try:
            model_config = ModelTrainerConfig()
            transformation_config = DataTransformationConfig()
            logger.info('Loading Model and preprocessor')
            self.model = load_object(model_config.model_path)
            self.preprocessor = load_object(transformation_config.preprocessor_path)
            logger.info('Model and preprocessor load successfully')
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def predict(self,input_data):
        """
        Predicts churn for a single customer.

        Args:
            input_data: Dictionary of customer features

        Returns:
            Prediction array (0 = no churn, 1 = churn)
        """
        try:
            logger.info('Prediction Started')
            
            #step1: dict to df
            input_df = pd.DataFrame([input_data])
            
            #Step 2: transform using same preprocessor as training
            transformed_data = self.preprocessor.transform(input_df)
            
            #step3: predict using loaded model
            prediction = self.model.predict(transformed_data)
            
            logger.info(f'prediction result: {prediction}')
            return prediction
        except Exception as e:
            logger.error('Prediction Failed')
            raise CustomException(e,sys)
        
