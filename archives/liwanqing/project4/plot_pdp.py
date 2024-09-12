import pandas as pd
import warnings
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.inspection import partial_dependence
from sklearn.inspection import plot_partial_dependence
from time import time
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import QuantileTransformer
from sklearn.neural_network import MLPRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.isotonic import IsotonicRegression
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, ExtraTreesRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import SGDRegressor, BayesianRidge, ARDRegression, PassiveAggressiveRegressor
from sklearn.linear_model import ElasticNet, HuberRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
warnings.filterwarnings("ignore")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
# California Housing data preprocessing
df = pd.read_excel('0408stata制造业.xlsx')
columns = ["人工智能能力", "研发支出合计", "政府干预程度", "劳动生产率", "互联网基础条件",
           "技术人员人数占比", "董事会人数", "总资产同比增长率", "总市值", "总资产"]
df_selected = df[columns]
df_selected['人工智能能力'] = df_selected['人工智能能力'].astype('float64')
# df_selected = df_selected.apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
df_selected = df_selected.apply(lambda x: (x-x.mean())/x.std())
# 分离特征和目标变量
X = df_selected.drop("总资产", axis=1)
y = df_selected["总资产"]
y -= y.mean()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
models = {
    # "RandomForest": RandomForestRegressor(random_state=42),
    # "GradientBoosting": GradientBoostingRegressor(random_state=42),
    # "LinearRegression": LinearRegression(),
    # "Ridge": Ridge(),
    # "Lasso": Lasso(),
    # "SVR": SVR(),
    "DecisionTree": DecisionTreeRegressor(random_state=42),
    "KNeighbors": KNeighborsRegressor(),
    "MLP": MLPRegressor(random_state=42, max_iter=500),
    "GaussianProcess": GaussianProcessRegressor(),
    "AdaBoost": AdaBoostRegressor(random_state=42),
    "Bagging": BaggingRegressor(random_state=42),
    "ExtraTrees": ExtraTreesRegressor(random_state=42),
    "KernelRidge": KernelRidge(),
    "SGD": SGDRegressor(),
    # "BayesianRidge": BayesianRidge(),
    # "ARD": ARDRegression(),
    "PassiveAggressive": PassiveAggressiveRegressor(),
    "ElasticNet": ElasticNet(),
    "Huber": HuberRegressor()
}
# Multi-layer perceptron
# print("Training MLPRegressor...")
# tic = time()
for name, model in models.items():
    print(name)
    est = make_pipeline(QuantileTransformer(), model)
    est.fit(X_train, y_train)
    # print(f"done in {time() - tic:.3f}s")
    # print(f"Test R2 score: {est.score(X_test, y_test):.2f}")

    # 2D interaction plots
    # features = ['人工智能能力', '政府干预程度', ('人工智能能力', '政府干预程度')]
    features = [('人工智能能力', '政府干预程度')]
    # print('Computing partial dependence plots...')
    # tic = time()
    _ = plt.figure(figsize=(12, 4), dpi=433)
    _, ax = plt.subplots(ncols=1, figsize=(6, 4))
    display = plot_partial_dependence(
        est, X_train, features, kind='average', n_jobs=3, grid_resolution=20,
        ax=ax,
    )
    # print(f"done in {time() - tic:.3f}s")
    display.figure_.suptitle(name)
    display.figure_.subplots_adjust(wspace=0.4, hspace=0.3)
    plt.show()
# # 个体条件期望图(Individual Conditional Expectation Plot)
# print('Computing partial dependence plots...')
# tic = time()
# features = ['MedInc', 'AveOccup', 'HouseAge', 'AveRooms']
# display = plot_partial_dependence(
#        est, X_train, features, kind="individual", subsample=50,
#        n_jobs=3, grid_resolution=20, random_state=0
# )
# # average / individual
#
# print(f"done in {time() - tic:.3f}s")
# display.figure_.suptitle(
#     'Individual Conditional Expectation Plot\n'
# )
# display.figure_.subplots_adjust(hspace=0.3)
#
# # both = PDP + ICE
# print('Computing partial dependence plots...')
# tic = time()
# features = ['MedInc', 'AveOccup', 'HouseAge', 'AveRooms']
# display = plot_partial_dependence(
#        est, X_train, features, kind="both", subsample=50,
#        n_jobs=3, grid_resolution=20, random_state=0
# )
# # average / individual
#
# print(f"done in {time() - tic:.3f}s")
# display.figure_.suptitle(
#     'Individual Conditional Expectation Plot\n'
# )
# display.figure_.subplots_adjust(hspace=0.3)

# # 部分依赖图(Partial Dependence Plot)
# print('Computing partial dependence plots...')
# tic = time()
# features = ['MedInc', 'AveOccup', 'HouseAge', 'AveRooms']
# display = plot_partial_dependence(
#        est, X_train, features, kind="average", subsample=50,
#        n_jobs=3, grid_resolution=20, random_state=0
# )
#
#
# print(f"done in {time() - tic:.3f}s")
# display.figure_.suptitle(
#     'Partial Dependence Plot\n'
# )
# display.figure_.subplots_adjust(hspace=0.3)
