def predict_price(time_horizon):
    if time_horizon == "1 Month":
        return "Welcome to the 1 Month prediction"
    elif time_horizon == "3 Months":
        return "Welcome to the 3 Months prediction"
    elif time_horizon == "6 Months":
        return "Welcome to the 6 Months prediction"
    else:
        return ""
