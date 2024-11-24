import mlflow
from loader import wordopt
import mlflow.pyfunc
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def predict_with_model(input_data : str, model_name : str) -> str:
    """
    Predicts the output using a model from MLflow.

    Parameters:
    model_uri (str): The URI of the model in MLflow.
    input_data (pd.DataFrame or np.ndarray): The input data for prediction.

    Returns:
    The prediction result.
    """
    model_uri = ''
    if model_name == 'decision_tree':
        model_uri = 'runs:/cecf204ee62a426188f753cb9950693f/decision_tree_model'
    else:
        model_uri = 'runs:/68e32882d055448284ba657960970164/logistic_regression_model'
    # Load the model
    model = mlflow.pyfunc.load_model(model_uri)
    
    #format input data
    input_data = wordopt(input_data)
    
    # Predict the input data
    predictions = model.predict([input_data])
    
    return predictions

predict_with_model("Hillary suports Trump", "decision_tree")