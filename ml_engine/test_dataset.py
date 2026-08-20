import pandas as pd


# Load dataset

data = pd.read_csv(
    "../dataset/ResumeDataset.csv"
)


print("Dataset Loaded")

print(data.head())


print("\nDataset Shape:")
print(data.shape)


print("\nCategory Distribution:")
print(data["Category"].value_counts())


print("\nMissing Values:")
print(data.isnull().sum())