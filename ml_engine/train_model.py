import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import joblib


# Load dataset
data = pd.read_csv("../dataset/ResumeDataset.csv")


print("Dataset Loaded")
print(data.head())

print("\nCategory Distribution:")
print(data["Category"].value_counts())


# Input and Output

X = data["Resume Text"]
y = data["Category"]


# Convert category names into numbers

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)



# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)



# Text to numerical features

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)


X_train_vector = vectorizer.fit_transform(X_train)

X_test_vector = vectorizer.transform(X_test)



# Train ML model

model = LogisticRegression(
    max_iter=1000
)


model.fit(
    X_train_vector,
    y_train
)



# Prediction

y_pred = model.predict(
    X_test_vector
)



# Accuracy

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:", accuracy)


print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=encoder.classes_
    )
)



# Save trained files

joblib.dump(
    model,
    "model.pkl"
)

joblib.dump(
    vectorizer,
    "vectorizer.pkl"
)

joblib.dump(
    encoder,
    "label_encoder.pkl"
)


print("\nModel training completed successfully!")