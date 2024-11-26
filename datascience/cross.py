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

#GradientBoosting : F1 Score: 0.8761606708524834 +/- 0.004671511655284488 array([0.87888942, 0.87090559, 0.8714044 , 0.87627261, 0.88333134])
