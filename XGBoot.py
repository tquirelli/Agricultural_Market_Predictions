from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import make_scorer

def initialize_train_model():
    # Instanciate model
    model_xgb = XGBRegressor(max_depth=10, n_estimators=300, learning_rate=0.1)
    return model_xgb

def mape_score():
    mape = make_scorer(lambda y_true, y_pred: mean_absolute_percentage_error(y_true, y_pred))
    return mape
