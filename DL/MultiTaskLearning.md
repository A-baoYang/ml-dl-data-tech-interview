# Multi-Task Learning

## Use Cases
- 同時有大類別、小類別時的分類(有一個分類框架、像是電商大品類、小品類) 
https://towardsdatascience.com/https-medium-com-noa-weiss-the-hitchhikers-guide-to-hierarchical-classification-f8428ea1e076

## Variants
1. Flat Classifier: 最直觀是直接對小類別訓練；但大類別的資訊其實也可以幫助小類別分類，如果只訓練 leaf class 就會 miss 掉 parent class 的資訊
2. Hierarchically-structured Local Classifiers: 對每一棵子樹訓練分類器，該棵子樹只能吃符合母類別的資料 
3. **Multi-task classification**
    - Implement reference: https://towardsdatascience.com/multi-task-learning-with-pytorch-and-fastai-6d10dc7ce855
4. 傳輸上一個 task 的 loss 到下一個 task
    - HMCN
      - source: [NeuralNLP-NeuralClassifier](https://github.com/Tencent/NeuralNLP-NeuralClassifier/blob/b4fa04ffb70cb4f3f2effdb07d455f5e3fc393ea/model/classification/hmcn.py)