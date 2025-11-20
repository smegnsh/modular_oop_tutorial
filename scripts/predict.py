from .model import load_model
import pandas as pd

def predict(model_path: str, X: pd.DataFrame):
    """
    Make predictions using a saved model.
    """
    model = load_model(model_path)
    predictions = model.predict(X)
    return predictions