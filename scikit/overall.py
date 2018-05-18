#估计器 （Estimator）：用于分类、聚类和回归分析。
  '''
  Function:
    fit() ：训练算法，设置内部参数。该函数接收训练集及其类别两个参数。
    predict() ：参数为测试集。预测测试集类别，并返回一个包含测试集各条数据类别的数组。
   '''
#转换器 （Transformer）：用于数据预处理和数据转换。

#流水线 （Pipeline）：组合数据挖掘流程，便于再次使用。

#%% read data and train 
import os
import numpy as np
import csv
data_filename = os.path.join(data_folder, "Ionosphere","ionosphere.data")
X = np.zeros((351, 34), dtype='float')
y = np.zeros((351,), dtype='bool')
with open(data_filename, 'r') as input_file:
    reader = csv.reader(input_file)
    for i, row in enumerate(reader):
      data = [float(datum) for datum in row[:-1]]
      X[i] = data
      y[i] = row[-1] == 'g' #if g ,return 1
# split data      
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)
# train data
from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier()
estimator.fit(X_train, y_train)
# predict
y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print("The accuracy is {0:.1f}%".format(accuracy))
# cross validation
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(estimator, X, y, scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("The average accuracy is {0:.1f}%".format(average_accuracy))

# try different parameters for estimator
avg_scores = []
all_scores = []
parameter_values = list(range(1, 21))  # Include 20
for n_neighbors in parameter_values:
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(estimator, X, y, scoring='accuracy')
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)
from matplotlib import pyplot as plt
plt.plot(parameter_values, avg_scores, '-o')

# preprocessing
from sklearn.preprocessing import MinMaxScaler
X_transformed = MinMaxScaler().fit_transform(X)#X_transformed 与X 行列数相等，为同型矩阵。然而，前者每列值的值域为0到1。
"""
为使每条数据各特征值的和为1，使用sklearn.preprocessing.Normalizer 。
为使各特征的均值为0，方差为1，使用sklearn.preprocessing.StandardScaler ，常用作规范化的基准。
为将数值型特征的二值化，使用sklearn.preprocessing.Binarizer ，大于阈值的为1，反之为0。
"""
# example
X_transformed = MinMaxScaler().fit_transform(X_broken)
estimator = KNeighborsClassifier()
transformed_scores = cross_val_score(estimator, X_transformed, y, scoring='accuracy')
print("The average accuracy for is {0:.1f}%".format(np.mean(transformed_scores) * 100))

#%% pipline
from sklearn.pipeline import Pipeline
#build pipline每一步都用元组（‘名称’，步骤）来表示
scaling_pipeline = Pipeline([('scale', MinMaxScaler()),
                             ('predict', KNeighborsClassifier())])
scores = cross_val_score(scaling_pipeline, X_broken, y, scoring='accuracy')
print("The pipeline scored an average accuracy for is {0:.1f}%".format(np.mean(transformed_scores) * 100))

#%% read data
import pandas as pd
dataset = pd.read_csv(data_filename)
dataset = pd.read_csv(data_filename, parse_dates=["Date"], skiprows=[0,])#跳过标题后的第一行
dataset.columns = ["Date", "Score Type", "Visitor Team", "VisitorPts", "Home Team", "HomePts", "OT?", "Notes"]
dataset["HomeWin"] = dataset["VisitorPts"] < dataset["HomePts"]
y_true = dataset["HomeWin"].values


