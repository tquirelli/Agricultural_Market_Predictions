

def get_num_months(prediction_horizon):
    if prediction_horizon == "1 Month":
        return 1
    elif prediction_horizon == "3 Months":
        return 3
    elif prediction_horizon == "6 Months":
        return 6
    else:
        return None



prediction_horizon="1 Month"





print(get_num_months("1 Month"))
