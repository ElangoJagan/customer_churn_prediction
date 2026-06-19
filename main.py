from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import pandas as pd

# Step 1 — Data Ingestion
ingestion = DataIngestion()
train_path, test_path = ingestion.initiate_data_ingestion()

# Step 2 — Data Transformation
transformation = DataTransformation()
train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(
    train_path, test_path
)

# 🔍 DEBUG CHECK — added AFTER train_arr/test_arr exist!
print("Train array shape:", train_arr.shape)
print("Duplicate rows in train (after SMOTE):", pd.DataFrame(train_arr).duplicated().sum())
print("Test array shape:", test_arr.shape)
print("Duplicate rows in test:", pd.DataFrame(test_arr).duplicated().sum())

train_df_check = pd.DataFrame(train_arr)
test_df_check = pd.DataFrame(test_arr)
overlap = pd.merge(train_df_check, test_df_check, how='inner')
print("Rows in test that EXACTLY match a row in train:", len(overlap))

# Step 3 — Model Training
trainer = ModelTrainer.with_default_config()
best_model_name, best_metrics = trainer.initiate_model_trainer(train_arr, test_arr)

print(f"\n🏆 Best Model: {best_model_name}")
print(f"📊 Metrics: {best_metrics}")