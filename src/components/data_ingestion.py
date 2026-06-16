import sys
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from src.logger import Logger
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig

_logger_obj = Logger('DataIngestion')
logger = _logger_obj.get_logger()

class DataIngestion:
    
    """
    Data Ingestion component.
    Loads 3 data sources, merges them and splits into train/test.

    New OOP Concept Learned: @staticmethod
    → Used for helper/utility methods inside class
    → Does not need self or cls
    → Called directly on class or object
    """
    def __init__(self):
        self.config = DataIngestionConfig()
        logger.info('DataINitialized with Config')
        
    @staticmethod
    def load_data(path):
        
        """
        Loads a CSV file from given path.
        Static method — does not need self!

        Args:
            path: Path to CSV file

        Returns:
            Loaded DataFrame
        """
        try:
            logger.info(f'Loading data from {path}')
            df= pd.read_csv(path)
            return df
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def validate_data(df, name):
        
        """
        Validates if dataframe is not empty.
        Static method — does not need self!

        Args:
            df: DataFrame to validate
            name: Name of the data source

        Returns:
            True if valid, raises exception if not
        """
        try:
            if df.empty:
                raise ValueError(f'{name} is empty')
            logger.info(f"{name} validation passed — {df.shape[0]} rows")
            return True
        except Exception as e:
            logger.error(f"Validation failed for {name}")
            raise CustomException(e,sys)
    
    def merge_data(self, demographics:pd.DataFrame, usage:pd.DataFrame, support:pd.DataFrame)->pd.DataFrame:
        """
        Merges 3 dataframes on customer_id.

        Args:
            demographics: Customer demographics data
            usage: Customer usage data
            support: Customer support data

        Returns:
            Merged DataFrame
        """ 
        try:
            logger.info('Merging 3 data sources')
            merged = demographics.merge(usage, on='customer_id')
            merged = merged.merge(support, on='customer_id')
            logger.info(f"Merge successful — shape: {merged.shape}")
            return merged
        except Exception as e:
            logger.error('Error merge data sources')
            raise CustomException(e,sys)
        
    def save_data(self, df, path):
        """
        Saves dataframe to CSV file.

        Args:
            df: DataFrame to save
            path: Path to save CSV
        """
        try:
            os.makedirs(os.path.dirname(path), exist_ok =True)
            df.to_csv(path, index= False)
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self):
        """
        Main method — runs full data ingestion pipeline.
        Loads → Validates → Merges → Splits → Saves

        Returns:
            Tuple of train and test data paths
        """
        try:
            logger.info("="*50)
            logger.info("Data Ingestion Started!")
            logger.info("="*50)
            
            #Step 1: Loadd 3 resources
            demographics = self.load_data(self.config.source1_path)
            usage = self.load_data(self.config.source2_path)
            support = self.load_data(self.config.source3_path)
            
            #Step2: Validate all resources
            self.validate_data(demographics, 'Demographics')
            self.validate_data(usage, 'Usage')
            self.validate_data(support, 'Support')
            
            #Step 3 : merge all data sources 
            merged_df = self.merge_data(demographics, usage, support)
            
            #Step 4: save merged data 
            self.save_data(merged_df, self.config.merged_data_path)
            
            #Ste5:split into train test split 
            logger.info("Splitting data into train and test sets")
            train_df, test_df = train_test_split(merged_df, test_size = 0.2, random_state = 42)
            
            logger.info(f"Train shape: {train_df.shape}")
            logger.info(f"Test shape:  {test_df.shape}")
            
            #Step 6:  Save train + test data
            self.save_data(train_df,self.config.train_data_path )
            self.save_data(test_df, self.config.test_data_path)
            
            logger.info("="*50)
            logger.info("Data Ingestion Completed!")
            logger.info("="*50)
            
            return self.config.train_data_path, self.config.test_data_path
        
        except Exception as e:
            logger.error('Data Ingestion Failed')
            raise CustomException(e,sys)
        
            
            