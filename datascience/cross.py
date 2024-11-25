from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd
from pipelines import algorithms
from loader import wordopt


seed = 17
df = pd.read_csv("./datascience/data/processed_data.csv")
X = df["text"]
y = df["class"]
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed) # Validação Cruzada de 10 pastas estratificada
X = X.apply(wordopt)


result = {}
for alg, clf in algorithms.items():
  result[alg] = cross_val_score(clf, X, y, cv=cv)

result = pd.DataFrame.from_dict(result)