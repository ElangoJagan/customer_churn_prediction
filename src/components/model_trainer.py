import sys
import os
import numpy as np
from typing import Any, Dict, Tuple

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, roc_auc_score)

from src.logger import Logger
from src.exception import CustomException
from src.entity.config_entity import ModelTrainerConfig
from src.utils import save_object

_logger_obj = Logger('ModelTrainer')
logger = _logger_obj.get_logger()


class ModelTrainer:
    
    """
    Model Trainer component.
    Trains multiple models, evaluates them, picks the best one.

    New OOP Concept Learned: @classmethod
    → Alternative constructor using cls
    → Useful for creating object with default settings
    """
    def __init__(self, config):
        self.config= config if config else ModelTrainerConfig()
        logger.info('ModelTrainer initialized with Config')
        
    @classmethod
    def with_default_config(cls):
        
        """
        Alternative constructor — creates ModelTrainer
        with default config automatically.

        New OOP Concept: @classmethod
        → cls refers to ModelTrainer class itself
        → returns a new ModelTrainer object

        Returns:
            ModelTrainer instance with default config
        """
        logger.info('creating modeltrainerwith default config')
        default_config=ModelTrainerConfig()
        return cls(default_config)
    
    def get_models(self):
        """
        Returns dictionary of models to train and compare.

        Returns:
            Dictionary mapping model name to model object
        """
        models= {
            'LogisticRegression': LogisticRegression(max_iter = 1000),
            'RandomForest':RandomForestClassifier(random_state= 42),
            'XGBoost':XGBClassifier(random_state = 42, eval_metric = 'logloss'),
        }
        logger.info(f'models to train{list(models.keys())}')
        return models
    
    def evaluate_model(self,y_true, y_pred):
        """
        Calculates evaluation metrics for a model's predictions.

        Args:
            y_true: Actual target values
            y_pred: Predicted target values

        Returns:
            Dictionary of metric name to score
        """
        try:
            metrics = {
                'accuracy': accuracy_score(y_true, y_pred),
                'precision':precision_score(y_true, y_pred),
                'recall': recall_score(y_true, y_pred),
                'f1_score':f1_score(y_true, y_pred),
                'roc_auc': roc_auc_score(y_true, y_pred),
            }
            return metrics
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_model_trainer(self, train_arr, test_arr):
        """
        Main method — trains all models, picks best by F1 score,
        saves the best model.

        Args:
            train_arr: Training data array (features + target)
            test_arr: Testing data array (features + target)

        Returns:
            Tuple of best model name and its metrics
        """
        try:
            logger.info("="*50)
            logger.info('Model Trainer has Started')
            logger.info("="*50)
            
            #Step1: split x and y
            x_train, y_train = train_arr[:,:-1], train_arr[:,-1]
            x_test, y_test = test_arr[:, :-1], test_arr[:,-1]
            
            
            #step 2: get models to try
            models = self.get_models()
            
            #Step3: train each model, eva;uate and storethe result
            report: Dict[str, Dict[str, float]]={}
            trained_models: Dict[str, Any]  = {}
            
            for model_name, model in models.items():
                logger.info(f'Training Model: {model_name}')
                
                model.fit(x_train, y_train)
                y_pred= (model.predict(x_test))
                
                metrics = self.evaluate_model(y_test, y_pred)
                report[model_name]= metrics
                trained_models[model_name] =model
                
                logger.info(f"{model_name} → {metrics}")
            
            #step4 : pick best model based on f1 score
            # (F1 balances precision + recall — good for imbalanced data!)
            
            best_model_name = max(report, key=lambda name: report[name]['f1_score'])
            
            best_model = trained_models[best_model_name]
            best_metrics= report[best_model_name]
            
            logger.info("=" * 50)
            logger.info(f"Best Model: {best_model_name}")
            logger.info(f"Best Metrics: {best_metrics}")
            logger.info("=" * 50)
            
            #step 5: save the best model 
            save_object(self.config.model_path, best_model)
            
            logger.info('ModelTraining Completed!')
            logger.info('='*50)
            
            return best_model_name, best_metrics
        
        except Exception as e:
            logger.info('ModelTrainer Failed')
            raise CustomException(e,sys)            
            
            