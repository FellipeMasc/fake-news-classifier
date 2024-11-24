
from loader import DataFrameLoader
from pipelines import algorithms
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
# df_loader = DataFrameLoader("./datascience/data/Fake.csv", "./datascience/data/True.csv")
# df = df_loader.fit_transform(X=None)
mlflow.set_tracking_uri("../mlruns")
df = pd.read_csv("./datascience/data/processed_data.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["class"], test_size=0.2, random_state=42, stratify=df["class"]
)

mlflow.set_experiment("fake_news_classifier_prod")

for algorithm_name, pipeline in algorithms.items():
    with mlflow.start_run(run_name=algorithm_name):
        pipeline.fit(X_train, y_train)

        best_params = pipeline.best_params_
        mlflow.log_params(best_params)

        best_estimator = pipeline.best_estimator_
        y_pred = best_estimator.predict(X_test)
        test_score = best_estimator.score(X_test, y_test)
        test_accuracy = accuracy_score(y_test, y_pred)
        test_precision = precision_score(y_test, y_pred, average='weighted')
        test_recall = recall_score(y_test, y_pred, average='weighted')
        test_f1 = f1_score(y_test, y_pred, average='weighted')

        # Registrando métricas no MLflow
        mlflow.log_metric("test_accuracy", test_accuracy)
        mlflow.log_metric("test_precision", test_precision)
        mlflow.log_metric("test_recall", test_recall)
        mlflow.log_metric("test_f1", test_f1)

        mlflow.sklearn.log_model(best_estimator, f"{algorithm_name}_model")

        print(f"{algorithm_name}:")
        print(f"Best Parameters: {best_params}")
        print(f"Test Accuracy: {test_score}")