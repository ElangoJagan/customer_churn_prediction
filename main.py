from src.utils import save_object, load_object

# Test saving and loading
data = {"name": "Elango", "project": "Customer Churn"}

save_object("artifacts/test_object.pkl", data)
loaded_data = load_object("artifacts/test_object.pkl")

print(f"Original:  {data}")
print(f"Loaded:    {loaded_data}")
print(f"Match:     {data == loaded_data}")