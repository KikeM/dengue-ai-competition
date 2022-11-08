class TransformerDropColumn:
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X, y=None):
        return X.drop(columns=self.columns)

    def fit(self, X, y=None):
        return self

    def fit_transform(self, X, y=None):
        return self.transform(X=X)
