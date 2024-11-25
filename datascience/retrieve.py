import mlflow
from datascience.loader import wordopt
import mlflow.pyfunc
import mlflow.sklearn

def predict_with_model(input_data : str, model_name : str) -> list:
    model_uri = ''
    if model_name == 'decision_tree':
        model_uri = 'runs:/00094c16ae434ab188fd5d69e5cfa486/decision_tree_model'
    elif model_name == 'gradient_boosting':
        model_uri = 'runs:/3b7cbbaee86c4755add7901f2a8e4f23/gradient_boosting_model'
    else:
        model_uri = 'runs:/6371b8cd38a345bdb02913f98e4c0bec/logistic_regression_model'
    model = mlflow.sklearn.load_model(model_uri)
    
    input_data = wordopt(input_data)
    prediction_probabilities = model.predict_proba([input_data])
    true_fact_prob = float(prediction_probabilities[0][1])
    fake_news_prob = float(prediction_probabilities[0][0])
    return [{
        "True Fact Probability": str(true_fact_prob),
        "Fake News Probability": str(fake_news_prob),
    }, f"True Fact Probability:{true_fact_prob}, Fake News Probability:{fake_news_prob}"]
    