import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import QuantileTransformer
from sklearn.pipeline import make_pipeline
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.isotonic import IsotonicRegression
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, ExtraTreesRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import SGDRegressor, BayesianRidge, ARDRegression, PassiveAggressiveRegressor
from sklearn.linear_model import ElasticNet, HuberRegressor
from sklearn.inspection import PartialDependenceDisplay
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Times New Roman']  # Set font to Times New Roman

# Load data
df = pd.read_excel("0408stata制造业.xlsx")

# Select specific columns
columns = ["人工智能能力", "研发支出合计", "政府干预程度", "劳动生产率", "互联网基础条件", "技术人员人数占比", "董事会人数", "总资产同比增长率", "总市值", "总资产"]
df_selected = df[columns]

# Split features and target
X = df_selected.drop("总资产", axis=1)
y = df_selected["总资产"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize multiple models
models = {
   # "RandomForest": RandomForestRegressor(random_state=42),
#    "GradientBoosting": GradientBoostingRegressor(random_state=42),
#    "LinearRegression": LinearRegression(),
#    "Ridge": Ridge(),
#    "Lasso": Lasso(),
#    "SVR": SVR(),
#     "DecisionTree": DecisionTreeRegressor(random_state=42),
#    "KNeighbors": KNeighborsRegressor(),
   "MLP": MLPRegressor(random_state=42, max_iter=500),
#    "GaussianProcess": GaussianProcessRegressor(),
#    "AdaBoost": AdaBoostRegressor(random_state=42),
#    "Bagging": BaggingRegressor(random_state=42),
#    "ExtraTrees": ExtraTreesRegressor(random_state=42),
#    "KernelRidge": KernelRidge(),
#    "SGD": SGDRegressor(),
#    "BayesianRidge": BayesianRidge(),
#    "ARD": ARDRegression(),
#    "PassiveAggressive": PassiveAggressiveRegressor(),
#    "ElasticNet": ElasticNet(),
#    "Huber": HuberRegressor()
}

# Train models and evaluate
results = {}
for name, model in models.items():
    est = make_pipeline(QuantileTransformer(), model)
    est.fit(X_train, y_train)
    y_pred = est.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    results[name] = {"R2 Score": r2, "MSE": mse, "MAE": mae}
    print(f"{name} - R2 Score: {r2}, MSE: {mse}, MAE: {mae}")

# Select the best performing model
best_model_name = max(results, key=lambda x: results[x]['R2 Score'])
best_model = models[best_model_name]

# Plot Partial Dependence
features = [("人工智能能力", "劳动生产率")]
_ = plt.figure(figsize=(12, 4), dpi=433)
_, ax = plt.subplots(figsize=(6, 4))
display = PartialDependenceDisplay.from_estimator(best_model, X_train, features, ax=ax, kind='average', grid_resolution=20)
plt.suptitle('Partial Dependence of Total Assets on AI Capabilities and Government Intervention')
plt.subplots_adjust(top=0.9)  # Adjust title space
plt.show()



