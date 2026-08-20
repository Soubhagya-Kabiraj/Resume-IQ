import os
import joblib

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

model = joblib.load(
    os.path.join(
        BASE_DIR,
        "ml_engine",
        "model.pkl"
    )
)

vectorizer = joblib.load(
    os.path.join(
        BASE_DIR,
        "ml_engine",
        "vectorizer.pkl"
    )
)

encoder = joblib.load(
    os.path.join(
        BASE_DIR,
        "ml_engine",
        "label_encoder.pkl"
    )
)

def predict_role(resume_text):
    # Convert text into TF-IDF feature
    text_vector = vectorizer.transform(
        [resume_text]
    )
    # Prediction
    prediction = model.predict(
        text_vector
    )
    # Convert number back to category
    role = encoder.inverse_transform(
        prediction
    )[0]
    # Confidence score
    probability = model.predict_proba(
        text_vector
    )
    confidence = float(max(probability[0]) * 100)
    return {
        "role": role,
        "confidence": round(confidence, 2)
    }