import mlflow
from datascience.loader import wordopt
import mlflow.pyfunc
import mlflow.sklearn
import pickle
import os

def predict_with_model(input_data : str, model_name : str) -> list:
    model_uri = ''
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_uri = os.path.join(root_path, 'models', model_name + '.pkl')
    model = None
    with open(model_uri, "rb") as f:
        model = pickle.load(f)
    
    input_data = wordopt(input_data)
    prediction_probabilities = model.predict_proba([input_data])
    true_fact_prob = float(prediction_probabilities[0][1])
    fake_news_prob = float(prediction_probabilities[0][0])
    return [{
        "True Fact Probability": str(true_fact_prob),
        "Fake News Probability": str(fake_news_prob),
    }, f"True Fact Probability:{true_fact_prob}, Fake News Probability:{fake_news_prob}"]
    