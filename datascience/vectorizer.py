import mlflow.pyfunc
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Classe customizada
class TfidfVectorizerWrapper(mlflow.pyfunc.PythonModel):
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer

    def predict(self, context, model_input):
        return self.vectorizer.transform(model_input)
df = pd.read_csv("./datascience/data/processed_data.csv")
# Treinar o TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=1000)
vectorizer.fit(df["text"])

# Salvar o TfidfVectorizer como um modelo no MLflow
with mlflow.start_run(run_name="save_vectorizer_model"):
    mlflow.pyfunc.log_model(
        artifact_path="tfidf_vectorizer",
        python_model=TfidfVectorizerWrapper(vectorizer)
    )