import os
import sys
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, StandardScaler , OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE

from src.exception import CustomException
from src.logger import Logger
from src.entity.config_entity import DataTransformationConfig
from src.utils import save_object

_logger_obj=Logger('Data_Transformation')
logger = _logger_obj.get_logger()

class DataTransformation:
    """
    Data Transformation component.
    Handles encoding, scaling and SMOTE for imbalanced data.

    New OOP Concept Learned: @property
    → Protects private variables
    → Adds validation before access
    → Safe way to expose internal data
    """
    def __init__(self):
        """Initialize DataTransformation with config."""
        self.config = DataTransformationConfig()
        
        self._preprocessor = None # Private variable
        logger.info('DataTransformation Initialized With Config')
    
    @property
    def preprocessor(self):
        
        """
        Property to safely access preprocessor.
        Raises error if preprocessor not built yet!

        New OOP Concept: @property
        → looks like attribute: obj.preprocessor
        → works like method: validates before returning!
        """
        if self._preprocessor is None:
            raise ValueError(
                'Preprocessor not built yet'
                'call initiate data transformation first '
            )
            return self._preprocessor
    
    def get_preprocessor(self) -> ColumnTransformer:
        
        """
        Builds preprocessing pipeline for numerical
        and categorical columns.

        Returns:
            ColumnTransformer preprocessor object
        """
        try:
            logger.info('Building Preprocessor Pipeline')
            
            #Numerical Cols
            numerical_cols = [
                'age',
                'monthly_charges',
                'total_charges',
                'data_usage_gb',
                'call_minutes',
                "num_complaints",
                "issues_resolved",
                "satisfaction_score"
            ]
            
            # categorical_columns
            categorical_cols = [
                'gender',
                'location',
                'contract_type'
            ]
            
            # Combine directly — no separate pipelines!
            preprocessor = ColumnTransformer(transformers=[("numerical", StandardScaler(), numerical_cols),("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_cols)])
            
            logger.info('Preprocessor Pipeline Build successfully')
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def apply_smote(self, x:np.ndarray, y:np.ndarray):
        """
        Applies SMOTE to handle imbalanced dataset.

        Args:
            X: Feature array
            y: Target array

        Returns:
            Resampled X and y arrays
        """
        try:
            logger.info("="*50)
            logger.info("Applying SMOTE for imbalanced data")
            logger.info(f"Before SMOTE — X: {x.shape}, y: {y.shape}")
            logger.info(
                f"Before SMOTE — Class distribution: "
                f"{dict(zip(*np.unique(y, return_counts=True)))}"
            )

            smote = SMOTE(random_state=42)
            X_resampled, y_resampled = smote.fit_resample(x, y)

            logger.info(
                f"After SMOTE — X: {X_resampled.shape}, "
                f"y: {y_resampled.shape}"
            )
            logger.info(
                f"After SMOTE — Class distribution: "
                f"{dict(zip(*np.unique(y_resampled, return_counts=True)))}"
            )
            logger.info("="*50)

            return X_resampled, y_resampled

        except Exception as e:
            logger.error("Error applying SMOTE")
            raise CustomException(e, sys)
        
    
    def initiate_data_transformation(
        self,
        train_path:str, 
        test_path:str
    ):
        """
        Main method — runs full transformation pipeline.
        Loads → Preprocesses → SMOTE → Returns arrays

        Args:
            train_path: Path to train CSV
            test_path: Path to test CSV

        Returns:
            Tuple of train array, test array, preprocessor path
        """
        try:
            logger.info("="*50)
            logger.info("Data Transformation Started!")
            logger.info("="*50)
            
            #step: 1 Load train & Test Data 
            train_df = pd.read_csv(train_path)
            test_df= pd.read_csv(test_path)
            
            logger.info(f"Train shape: {train_df.shape}")
            logger.info(f"Test shape:  {test_df.shape}")
            
            #step:2 separate features and target 
            target = self.config.target_column
            
            
            x_train = train_df.drop(columns = [target, 'customer_id'])
            y_train = train_df[target]
            x_test = test_df.drop(columns = [target, 'customer_id'])
            y_test = test_df[target]
            
            #Step 3: Build and fit preprocessor
            self._preprocessor = self.get_preprocessor()
            x_train_transformed = self._preprocessor.fit_transform(x_train)
            x_test_transformed = self._preprocessor.transform(x_test)
            logger.info('Preprocessing done')
            save_object(self.config.preprocessor_path, self._preprocessor)
            logger.info('Preprocessor saved')
            
            #Step 4: Apply SMOTE:
            
            X_train_resampled, y_train_resampled = self.apply_smote(
                x_train_transformed, y_train.values
            )
            
            #Step 5:combine x and  y back
            train_arr = np.c_[X_train_resampled, y_train_resampled]
            test_arr= np.c_[x_test_transformed, y_test.values]
            
            logger.info("="*50)
            logger.info("Data Transformation Completed!")
            logger.info("="*50)
            
            return(
                train_arr, test_arr, self.config.preprocessor_path
            )
        except Exception as e:
            raise CustomException(e,sys)
            