from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import FunctionTransformer, Pipeline
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import make_scorer, accuracy_score
import pandas as pd
import numpy as np


scorer = make_scorer(accuracy_score)

seed = 42 
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
gscv = StratifiedKFold(n_splits=3, shuffle=True, random_state=seed)

def pipeline_decision_tree():
    pass
    

algorithms = {
    'decision_tree':
        Pipeline([
            ('vectorizer', TfidfVectorizer(max_features=10000)), 
            ('tree', DecisionTreeClassifier(
                max_depth=2,               # Limita a profundidade
                min_samples_split=5,      # Mínimo de 10 amostras para dividir
                min_samples_leaf=5,        
                random_state=seed   
            ))
        ])
    ,
    'logistic_regression': 
        Pipeline([
            ('vectorizer', TfidfVectorizer(max_features=10000)),
            ('logreg', LogisticRegression(random_state=seed, penalty='l2', C=0.1, solver='lbfgs', max_iter=1000))
        ])
    ,
    'gradient_boosting': Pipeline(
        [
            ('vectorizer', TfidfVectorizer(max_features=10000)),
            ('gradient_boosting', GradientBoostingClassifier(random_state=0, n_estimators=40, max_depth=2, learning_rate=0.01))
        ]
    )
}
