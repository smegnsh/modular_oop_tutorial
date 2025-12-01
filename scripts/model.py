from sklearn.model_selection import train_test_split   # Import function to split dataset into train and test sets
from sklearn.ensemble import RandomForestClassifier    # Import Random Forest model for classification
import joblib                                          # Import joblib for saving and loading trained models


def train_model(X, y, test_size=0.2, random_state=42):
    """
    Train a Random Forest model.
    """
    # Split the dataset into training and testing parts
    X_train, X_test, y_train, y_test = train_test_split(
        X,              # Features
        y,              # Target labels
        test_size=test_size,          # Percentage of data used for testing
        random_state=random_state     # Seed for reproducibility
    )

    # Create an instance of RandomForestClassifier
    model = RandomForestClassifier(random_state=random_state)

    # Train (fit) the model using training data
    model.fit(X_train, y_train)

    # Return the trained model and the test sets for evaluation
    return model, X_test, y_test


def save_model(model, file_path="loan_model.pkl"):
    # Save the trained model to a file using joblib
    joblib.dump(model, file_path)


def load_model(file_path="loan_model.pkl"):
    # Load the model from disk and return it
    return joblib.load(file_path)
