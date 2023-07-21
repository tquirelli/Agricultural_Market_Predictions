from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import make_scorer
from numpy import abs, mean, array

def initialize_rf():
    # Instanciate model
    model_rf = RandomForestRegressor(n_estimators=20)
    return model_rf

def mape_score():
    mape = make_scorer(lambda y_true, y_pred: mean_absolute_percentage_error(y_true, y_pred))
    return mape
