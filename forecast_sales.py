from neuralprophet import NeuralProphet
def forecast_sales(store_pd):
    m = NeuralProphet(
        growth="linear",
        #changepoints=None, # list of dates that may include change points (None -> automatic )
        #n_changepoints=5,
        changepoints_range=0.95,
        trend_reg=0,
        trend_reg_threshold=False,
        yearly_seasonality="auto",
        weekly_seasonality="auto",
        daily_seasonality="auto",
        seasonality_mode="additive",
        seasonality_reg=0,
        n_forecasts=180,
        n_lags=180,
        batch_size=32,
        num_hidden_layers=2,
        d_hidden=4,     # Dimension of hidden layers of AR-Net
        #ar_sparsity=None,  # Sparcity in the AR coefficients
        learning_rate=0.01,
        epochs=1000,
        loss_func="Huber",
        normalize="auto",  # Type of normalization ('minmax', 'standardize', 'soft', 'off')
        impute_missing=True
        #log_level=None, # Determines the logging level of the logger object
    )
    m = m.add_country_holidays("UZ", mode="additive") # adding holidays to the model as data anomalies
    m.fit(store_pd, freq='D')
    future = m.make_future_dataframe(store_pd, periods=180, n_historic_predictions=True)
    forecast = m.predict(future)
    latest_forecast = m.get_latest_forecast(forecast)
    return latest_forecast