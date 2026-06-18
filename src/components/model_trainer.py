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
    