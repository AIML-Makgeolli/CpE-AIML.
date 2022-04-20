# -*- coding: utf-8 -*-
"""[kmeans] modelTrain1_ver3 (function version).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TWvO-Kja184Oq9FUOpoizSIbLkK8dKKR
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.model_selection import train_test_split
from numpy import sqrt, array, random, argsort
from sklearn.preprocessing import scale
#from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import pickle


#from google.colab import drive
#drive.mount('/content/gdrive')

df =  pd.read_csv("https://raw.githubusercontent.com/AIML-Makgeolli/CpE-AIDL/main/thesis_database/Crop_recommendation.csv")
df_train = df.drop(['label','rainfall'], axis = 1)
df_train

"""Declaration"""

X_N = df_train[['N']] #.iloc[:100]
X_P = df_train[['P']]
X_K = df_train[['K']]
X_temp = df_train[['temperature']]
X_moist = df_train[['humidity']]
y = df_train[['ph']] #.iloc[:100]

class kMeans():
      def __init__(self):
    return
    
  def input_train(self, X_in, y_in):
    self.X = X_in
    self.y = y_in
    X_train, X_test, y_train, y_test = train_test_split(self.X, self.y,test_size=0.3, random_state=42)
    self.data = pd.concat([X_train, y_train], axis=1).to_numpy()
    return self.data
  def kmeans_test(self,clust):
    self.km = KMeans(n_clusters = clust)
    self.clusters = self.km.fit_predict(self.data)
    self.clust_data = plt.scatter(*zip(*self.data),c=self.clusters)
    
    self.labels = self.km.labels_
    
    print(self.labels)
    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(self.data, self.labels))
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(self.clusters, self.labels))
    print("Completeness: %0.3f" % metrics.completeness_score(self.clusters, self.labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(self.clusters, self.labels))
    print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(self.clusters, self.labels))
    print("Adjusted Mutual Information: %0.3f"% metrics.adjusted_mutual_info_score(self.clusters, self.labels))
    
    return self.clust_data
  
  def outlier(self,threshold):
    self.centroids = self.km.cluster_centers_
    self.points = np.empty((0,len(self.data[0])), float)
    self.distances = np.empty((0,len(self.data[0])), float)
    for i, center_elem in enumerate(self.centroids):
      self.distances = np.append(self.distances, cdist([center_elem],self.data[self.clusters == i], 'euclidean')) 
      self.points = np.append(self.points, self.data[self.clusters == i], axis=0)
      
    percentile = threshold
    self.outliers = self.points[np.where(self.distances > np.percentile(self.distances, percentile))]
    outliers_df = pd.DataFrame(self.outliers,columns =['X','y'])
    return outliers_df

  def kmeans_results(self):
    fig = plt.figure()
    plt.scatter(*zip(*self.data),c=self.clusters)
    plt.scatter(*zip(*self.outliers),marker="o",facecolor="None",edgecolor="g",s=70); 
    plt.scatter(*zip(*self.centroids),marker="o",facecolor="b",edgecolor="b",s=20);

kmeanstest = kMeans()

"""Nitrogen and pH"""

kmeanstest.input_train(X_N,y)

kmeanstest.kmeans_test(3)

kmeanstest.outlier(80)

kmeanstest.kmeans_results()

"""Phosphorous and pH"""

kmeanstest.input_train(X_P,y)

kmeanstest.kmeans_test(3)

kmeanstest.outlier(80)

kmeanstest.kmeans_results()

"""Potassium and ph"""

kmeanstest.input_train(X_K,y)

kmeanstest.kmeans_test(3)

kmeanstest.outlier(80)

kmeanstest.kmeans_results()

"""Temperature and ph"""

kmeanstest.input_train(X_temp,y)

kmeanstest.kmeans_test(3)

kmeanstest.outlier(80)

kmeanstest.kmeans_results()

"""Moisture and pH"""

kmeanstest.input_train(X_moist,y)

kmeanstest.kmeans_test(3)

kmeanstest.outlier(80)

kmeanstest.kmeans_results()