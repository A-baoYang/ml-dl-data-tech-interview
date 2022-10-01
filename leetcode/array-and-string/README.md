# Array and String

### 前言

- Array 是資料結構中的基本模組之一
- String 是由字符數組成的，所以他和 Array 相似

### 集合、列表、數組

- 集合
  - 由一個或多個確定元素所構成的整體
  - 當中的元素類型不一定相同
  - 當中的元素沒有順序性
- 列表
  - 一種數據項構成的有限序列，按照一定的線性順序排列而成的數據項集合
  - 有順序性且長度可變
  - 常見的表現形式： array, linked list
  - 特殊形式： queue, stack
- 數組
  - 是列表的表現方式之一
  - 在不同的語言中有不同差異，例如在 Python 中叫做 list，其中的元素類型必須一致
- 如何區分列表 v.s. 數組？
  - 數組
    - 會用 **索引** 標示位置，從 0 起算
    - 數組中的元素在內存中是連續儲存的、每個元素佔用同樣大小內存
  - 列表
    - 沒有索引
    - 數組中的元素在內存中的位置不一定連續, ex: linked list

### 數組操作
- 讀取
  - O(1)
- 查找
  - O(N)
- 加入
  - 直接加在最後 時間複雜度: O(1)
  - 加在指定位置 時間複雜度: O(N) 因為要改其他元素的位置
- 刪除
  - 直接刪除最後 時間複雜度: O(1)
  - 刪除指定位置元素 時間複雜度: O(N) 因為要改其他元素的位置

### 二維數組(矩陣)

即 List of list

### 字符串
- 由零個或多個字符組成的有限序列，是一種用來表示文本的數據類型
- 字符串的操作比其他類型更複雜(ex: 比較、連接)

比較操作
- 可否用 `==` 來比較兩個字串
  - Ｏ：Python, C++ 
  - Ｘ：Java (比較的是 是否是同一個 object)

連接操作
- 字符串是否可變
  - Ｏ：C++ 
  - Ｘ：Python, Java

### 字符串匹配算法 KMP
Knuth-Morris-Pratt 算法
- 是一種改進的字符串匹配算法，用來「快速匹配字串」
- 利用匹配失敗後的訊息，盡量減少模式串與主字串的匹配次數
- 時間複雜度 : O(m+n)

白話版本
- 目標字串：ACTGPACTKACTGPACY
- 比對字串：ACTGPACY
- KMP 思路
  - 利用比對字串中重複的部分，當作 **比對失敗後下一步要重新開始的位置**
  - i, j 雙指針，i 指在目標字串、j 指在比對字串，如果目標字串中的字符有出現在比對字串內，但不在目前位置，此時比對錯誤後，下一步把 j 移到比對字串有相對字符的位置，i 不變繼續往後比對
  - 如果目標字串中的字符沒有在比對字串內，此時比對錯誤後，如果位置落在比對字串中本身有最長公共前綴後綴的字符上，則 j 移到另一個重複字符+1，i 不動，繼續往後比對

- 如何構造下一步的比對位置
![](https://pic.leetcode-cn.com/8cd158c08b74130068b580d6d8830ecb700af1e84897ac07a6c533b9c6c0c6a6-8.png)

![](https://i.imgur.com/wirmYGe.png)

- 圖解過程
![](https://pic.leetcode-cn.com/c3dde6e8b72414a720ca76849b4aee32a5ab4833a58388637cae2ad657d4130d-4.gif)
![](https://pic.leetcode-cn.com/98463d52c63ba4ca59d2099f00fe59b42a8669a7bc38349817899001d442c550-5.png)
![](https://pic.leetcode-cn.com/bce64b7c2d5632cf519725dc61818d60357464f16b7a6472bb7becc2db0e8438-7.png)

### 雙指針

- 一個數組
  - 反向雙指針：從兩端向中間迭代、常用於排序
    ![](https://pic.leetcode-cn.com/84f9f1fce23655fcc653179b26d9800edf54858f790be1bc7573eb228f2aac00-2.gif)
  - 同向雙指針：快慢指針、可節省空間使用、設計不同移動條件來解題
    ![](https://pic.leetcode-cn.com/353657e00bf49ad5c6aeb8e97414d1d610083acdb580e7c2b0fe036a523129f5-4.gif)

### 總結

其他的類似數組：
- String
- Hash Table
- Linked List
- Queue
- Stack

常見算法：
- 二分搜尋
- 指針
  - 單指針
  - 雙指針
    - 快慢指針
    - 與貪心算法相關
- 滑動窗口