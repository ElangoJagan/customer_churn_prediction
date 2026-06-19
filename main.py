from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# Step 1 — Data Ingestion
ingestion = DataIngestion()
train_path, test_path = ingestion.initiate_data_ingestion()

# Step 2 — Data Transformation
transformation = DataTransformation()
train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(
    train_path, test_path
)

# Step 3 — Model Training
trainer = ModelTrainer.with_default_config()
best_model_name, best_metrics = trainer.initiate_model_trainer(train_arr, test_arr)

print(f"\n🏆 Best Model: {best_model_name}")
print(f"📊 Metrics: {best_metrics}")