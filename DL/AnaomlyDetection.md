# Anomaly Detection

> Binary Classification with extremely imbalance class 
- 用於極度不平衡類別預測上，例如 洗錢戶是少數用戶可能只佔所有正常用戶不到 1%，此時一般的單分類模型表現不一定好，可以利用對單類別學習特徵後以 Loss 值排序預測為異常值的樣本

> An unsupervised data processing technique to detect anomalies from the dataset

## Types of anomalies
- Outliers: 
  - Short/small anomalous patterns that appear in a non-systematic way in data collection.
- Change in Events: 
  - Systematic or sudden change from the previous normal behavior.
- Drifts:
  - Slow, undirectional, long-term change in the data.


## Algorithms (Unsupervised)
  - AutoEncoder
  - DBSCAN
  - Isolation Forest
  - Local Outlier Factor
  - Robust Covariance
  - One-Class SVM
  - One-Class SVM (SGD)

## AutoEncoder

LSTM AutoEncoder Example 
- noted that the author use the Linear output layer which is not a classic autoencoder
  - Should be the original shape as input data so that we can count loss
https://curiousily.com/posts/time-series-anomaly-detection-using-lstm-autoencoder-with-pytorch-in-python/


## Cases
- Fraud Detection 
  - Panel data
  - Predict if the data sample is outlier among whole dataset (偵測行為總體數據的異常)
  https://github.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/blob/master/fraud_detection.ipynb
- ECG/disease Anomaly Detection 
  - Time series data
  - Predict if next time point is outlier (anomaly) (偵測下個時間點的數值是否異常)
  https://github.com/BLarzalere/LSTM-Autoencoder-for-Anomaly-Detection/blob/master/Sensor%20Anomaly%20Detection.ipynb
- Handle cases with high-class imbalance
- Improve robustiness



### References
- https://towardsdatascience.com/effective-approaches-for-time-series-anomaly-detection-9485b40077f1