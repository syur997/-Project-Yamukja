import joblib
import pandas as pd
import asyncio
import time

class CatClassifier:
    
    def __init__(self):
        self.pipe = joblib.load("lightgbmClassifier.joblib")
        
    def classifier(self, X):
        self.y = self.pipe.predict(X)
        return self.y
    
if __name__ == "__main__":
    start = time.time()
    cat = CatClassifier()
    a = pd.read_csv("../../Mango_data(latlng)/원본/강서구_latlng.csv")
    y = cat.classifier(a[["category"]])
    end = time.time()
    print(y)
    print(f"{end-start:.2f}")
