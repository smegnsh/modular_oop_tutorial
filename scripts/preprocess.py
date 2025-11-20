from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_data(df: pd.DataFrame, target_col: str = "Loan_Status"):
    """
    Basic preprocessing: fill missing values, encode categorical features.
    """
    df = df.copy()

    # Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)

    # Fill missing categorical values with mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Encode categorical variables
    label_encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df.drop(columns=[target_col])
    y = df[target_col]

    return X, y, label_encoders