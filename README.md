# NeuralProphet
Prediction of product sales via NeuralProphet by Meta

We have a set of sales data with a several hundred products. The usual way is to work with a single time series thoroughly.
But in this case we will do the following:
  1. Group the frame by product names or IDs
  2. Split the frame so we will implement the model for each product
  3. Knowing that we have a lot of groups, we will use torch.multiprocessing
  4. Concat the list of dataframes with predictions to a single dataframe


More info about data preparation and example of a model with a single time series prediction to follow...
