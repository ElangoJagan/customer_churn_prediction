from src.exception import CustomException
from src.logger import Logger
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

ingestion = DataIngestion()
train_path, test_path = ingestion.initiate_data_ingestion()


transformation = DataTransformation()
train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(train_path, test_path)

print(train_arr.shape)
print(test_arr.shape)