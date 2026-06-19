import sys

from src.logger import Logger
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


_logger_obj = Logger("TrainPipeline")
logger = _logger_obj.get_logger()


class TrainPipeline:
    
    def __init__(self):
        self.ingestion = DataIngestion()
        self.transformation = DataTransformation()
        self.trainer = ModelTrainer.with_default_config()
    
    def run_pipeline(self):
        """
        Runs the full training pipeline end-to-end.

        Returns:
            Tuple of best model name and its evaluation metrics
        """
        try:
            logger.info("=" * 50)
            logger.info("TRAIN PIPELINE STARTED!")
            logger.info("=" * 50)

            # Step 1 — Data Ingestion
            train_path, test_path = self.ingestion.initiate_data_ingestion()

            # Step 2 — Data Transformation
            train_arr, test_arr, _ = self.transformation.initiate_data_transformation(
                train_path, test_path
            )

            # Step 3 — Model Training
            best_model_name, metrics = self.trainer.initiate_model_trainer(
                train_arr, test_arr
            )

            logger.info("=" * 50)
            logger.info("TRAIN PIPELINE COMPLETED!")
            logger.info(f"Best Model: {best_model_name}")
            logger.info(f"Metrics: {metrics}")
            logger.info("=" * 50)

            return best_model_name, metrics

        except Exception as e:
            logger.error("Train Pipeline Failed!")
            raise CustomException(e, sys)
        