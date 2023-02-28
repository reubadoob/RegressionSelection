
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def random_forest_regression(dataset_file, test_size=0.2, random_state=0, n_estimators=10, criterion='mse'):
    # Importing the dataset
    dataset = pd.read_csv(dataset_file)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Training the Random Forest Regression model on the whole dataset
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=10, random_state=0)
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)

    # Evaluating the Model Performance
    from sklearn.metrics import r2_score
    score = r2_score(y_test, y_pred)

    return score



