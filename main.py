from src.pipeline.predict_pipeline import PredictPipeline

# Sample customer data
sample_input = {
    "age": 35,
    "gender": "Male",
    "location": "Urban",
    "contract_type": "Month-to-Month",
    "monthly_charges": 75.5,
    "total_charges": 1200.0,
    "data_usage_gb": 20.5,
    "call_minutes": 450,
    "num_complaints": 3,
    "issues_resolved": 1,
    "satisfaction_score": 2
}

pipeline = PredictPipeline()
result = pipeline.predict(sample_input)

print(f"\n🔮 Prediction: {result}")
print(f"Churn: {'YES' if result[0] == 1 else 'NO'}")