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
    'decision_tree': GridSearchCV(
        Pipeline([
            ('vectorizer', TfidfVectorizer()), 
            ('tree', DecisionTreeClassifier(random_state=seed))
        ]),
        param_grid={
            'vectorizer__max_features': [1000],
            'tree__max_depth': [5, 10],
            'tree__criterion': ['entropy', 'gini']
        },
        scoring=scorer,
        cv=gscv,
        n_jobs=-1,
        error_score='raise'
    ),
    'logistic_regression': GridSearchCV(
        Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('logreg', LogisticRegression(random_state=seed, max_iter=1000))
        ]),
        param_grid={
            'vectorizer__max_features': [500, 1000, 2000],
            'logreg__C': [0.1, 1.0, 10.0],
            'logreg__penalty': ['l2'] 
        },
        scoring=scorer,
        cv=gscv,
        n_jobs=-1,
        error_score='raise'
    )
}
