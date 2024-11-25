
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import re
import string

def wordopt(text):
    text = re.sub(r'^\w+\s+\((Reuters)\)\s+-\s+', '',text)
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text



class DataFrameLoader(BaseEstimator, TransformerMixin):
    def __init__(self, fake_path, true_path):
        self.fake_path = fake_path
        self.true_path = true_path


    def fit(self, X=None, y=None):
        return self

    def transform(self, X=None):
        df_fake = pd.read_csv(self.fake_path)
        df_true = pd.read_csv(self.true_path)
        df_fake["class"] = 0
        df_true["class"] = 1

        df_merge = pd.concat([df_fake, df_true], axis=0)
        df = df_merge.drop(["title", "subject", "date"], axis=1)
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        df["text"] = df["text"].apply(wordopt)
        return df