import joblib
from schema import Request

class MLPredictor():
    def __init__(self):
        self.model = joblib.load("model.sav")
        self.mapping_label = {0:"Setosa", 1:"Versicolor", 2:"Virginica"}

    def predict(self, req:Request):
        res = self.model.predict([[req.sepal_length, req.sepal_width , req.petal_length, req.petal_width]])
        label = self.mapping_label[res[0]]
        return label