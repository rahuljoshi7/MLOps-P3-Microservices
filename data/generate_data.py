
import pandas as pd
from sklearn.datasets import load_breast_cancer
from pathlib import Path

# Load the Breast Cancer dataset
dataset = load_breast_cancer()

# Convert features into a DataFrame
df = pd.DataFrame(
    dataset.data,
    columns=dataset.feature_names
)

# Add target column
df["target"] = dataset.target

# Save dataset
output_path = Path(__file__).parent / "breast_cancer.csv"
df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print("Dataset shape:", df.shape)
print(df.head())
