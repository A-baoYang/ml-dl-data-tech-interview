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

## ML Model Hyperparameters Tuning

- Isolation Forest
  - `n_estimator`: The larger, the more complex the model is
  - `contamination`: How much percentage/portion of the input data points are outliers in the input trainset
- Local Outlier Factor
  - `novelty` 
    - `True`: Find outliers in new dataset(testset) (Novelty Detection) 
      - `contamination`: Set a very small number for 
    - `False`: Input trainset has outliers (Outlier Detection)
  - `n_neighbors`: larger produces better results at the expense of increased fitting time, `n_neighbors=20` work well when outliers below 10%
- One Class SVM : typically sensitive to outliers and hence not very good for outlier detection, but can be used for flagging outliers by fine-tuning the hyperparameter called “Nu” to handle outliers by preventing overfitting.
  - `kernel`
    - `rbf`: outliers not separable with a linear boundary
    - `linear`: outliers are separable with a linear boundary

> References:
- https://support.altair.com/csm?id=community_blog&sys_id=b71da727dba60d90e8863978f49619ec
- https://pub.towardsai.net/an-in-depth-guide-to-local-outlier-factor-lof-for-outlier-detection-in-python-5a6f128e5871
- https://www.cnblogs.com/wj-1314/p/10461816.html


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