import pandas as pd
import numpy as np
import os

np.random.seed(42)
n = 1000

# Source 1 — Customer Demographics
demographics = pd.DataFrame({
    "customer_id": range(1, n + 1),
    "age": np.random.randint(18, 70, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "location": np.random.choice(["Urban", "Rural", "Suburban"], n),
    "contract_type": np.random.choice(["Month-to-Month", "One Year", "Two Year"], n),
})

# Source 2 — Customer Usage
usage = pd.DataFrame({
    "customer_id": range(1, n + 1),
    "monthly_charges": np.round(np.random.uniform(20, 100, n), 2),
    "total_charges": np.round(np.random.uniform(100, 5000, n), 2),
    "data_usage_gb": np.round(np.random.uniform(1, 50, n), 2),
    "call_minutes": np.random.randint(0, 1000, n),
})

# Source 3 — Customer Support
support = pd.DataFrame({
    "customer_id": range(1, n + 1),
    "num_complaints": np.random.randint(0, 10, n),
    "issues_resolved": np.random.randint(0, 10, n),
    "satisfaction_score": np.random.randint(1, 5, n),
    "churn": np.random.choice([0, 1], n, p=[0.85, 0.15]),
})

# Save to data/raw/
os.makedirs("data/raw", exist_ok=True)
demographics.to_csv("data/raw/customer_demographics.csv", index=False)
usage.to_csv("data/raw/customer_usage.csv", index=False)
support.to_csv("data/raw/customer_support.csv", index=False)

print("✅ All 3 data sources created successfully!")
print(f"Demographics shape: {demographics.shape}")
print(f"Usage shape:        {usage.shape}")
print(f"Support shape:      {support.shape}")