from src.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

# Create config objects
ingestion_config = DataIngestionConfig()
transformation_config = DataTransformationConfig()
trainer_config = ModelTrainerConfig()

# Print them — @dataclass gives __repr__ automatically!
print(ingestion_config)
print(transformation_config)
print(trainer_config)