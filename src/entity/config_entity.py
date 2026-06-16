from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    """
    Configuration for Data Ingestion component.
    Holds all file paths needed for loading and merging data.

    New OOP Concept Learned: @dataclass
    → automatically creates __init__, __str__, __repr__
    → clean typed config object instead of messy dicts!
    """
    # Raw data source paths
    source1_path: str = "data/raw/customer_demographics.csv"
    source2_path: str = "data/raw/customer_usage.csv"
    source3_path: str = "data/raw/customer_support.csv"

    # Processed data paths
    merged_data_path: str = "data/processed/merged_data.csv"
    train_data_path: str = "data/processed/train.csv"
    test_data_path: str = "data/processed/test.csv"


@dataclass
class DataTransformationConfig:
    """
    Configuration for Data Transformation component.
    Holds preprocessor path and transformation settings.
    """
    preprocessor_path: str = "artifacts/preprocessor.pkl"
    test_size: float = 0.2
    random_state: int = 42
    target_column: str = "churn"


@dataclass
class ModelTrainerConfig:
    """
    Configuration for Model Trainer component.
    Holds model save path and evaluation threshold.
    """
    model_path: str = "artifacts/model.pkl"
    metrics_path: str = "artifacts/metrics.json"
    expected_accuracy: float = 0.75






'''from dataclasses import dataclass
from src.logger import Logger
from pathlib import Path

@dataclass
class DataIngestionConfig:
    """
    Configuration for Data Ingestion component.
    Holds all file paths needed for loading and merging data.

    New OOP Concept Learned: @dataclass
    → automatically creates __init__, __str__, __repr__
    → clean typed config object instead of messy dicts!
    """
    source1_path = Path("data/raw/customer_demographics.csv")
    source2_path = Path("data/raw/customer_usage.csv")
    source3_path = Path("data/raw/customer_support.csv")
    
    # Processed data paths
    merged_data_path: Path = Path("data/processed/merged_data.csv")
    train_data_path: Path = Path("data/processed/train.csv")
    test_data_path: Path = Path("data/processed/test.csv")
    
@dataclass
class DataTransformationConfig:
    """
    Configuration for Data Transformation component.
    Holds preprocessor path and transformation settings.
    """
    preprocessor_path = Path("artifacts/preprocessor.pkl")
    test_size:float = 0.2
    random_state = 42
    target_column = 'churn'
    
@dataclass
class ModelTrainerConfig:
    """
    Configuration for Model Trainer component.
    Holds model save path and evaluation threshold.
    """
    
    model_path = Path("artifacts/model.pkl")
    metrics_path =Path("artifacts/metrics.json")
    expected_accuracy = 0.75
'''