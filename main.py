from multiple_linear_module import multiple_linear_regression
from polynomial_module import polynomial_regression
from svr_module import svr_model
from random_forrest_module import random_forest_regression
from decision_tree_module import decision_tree_regression
import warnings

warnings.filterwarnings('ignore')

# Prompt user to enter CSV file path
dataset_file = input("Enter the path to the CSV file: ")

# Call the Multiple Linear Function
mlr_score = multiple_linear_regression(dataset_file, test_size=0.2, random_state=0)
print(f"R2 Score for Multiple Linear Regression is {mlr_score}")

# Call the Polynomial Function
poly_score = polynomial_regression(dataset_file, test_size=0.2, random_state=0, degree=4)
print(f"R2 Score for Polynomial Regression is {poly_score}")

# Call the Support Vector Function
svm_score = svr_model(dataset_file, test_size=0.2, random_state=0, kernel='rbf')
print(f"R2 Score for Support Vector Model Regression is {svm_score}")

# Call the Random Forrest Function
rf_score = random_forest_regression(dataset_file, test_size=0.2, random_state=0, n_estimators=10, criterion='mse')
print(f"R2 Score for Random Forrest Regression is {rf_score}")

# Call the Decision Tree Function
dt_score = decision_tree_regression(dataset_file, test_size=0.2, random_state=0, criterion='mse')
print(f"R2 Score for Decision Tree Model Regression is {dt_score}")

scores = {"Multiple Linear Regression": mlr_score,
          "Polynomial Regression": poly_score,
          "Support Vector Model Regression": svm_score,
          "Random Forrest Regression": rf_score,
          "Decision Tree Model Regression": dt_score}

# Find the function with the highest R2 score
best_score = max(scores.values())
best_function = [k for k, v in scores.items() if v == best_score][0]

print(f"The function with the highest R2 score is {best_function} with a score of {best_score}")
