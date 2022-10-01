# Hash Table

> Status : `Ongoing`

---

### Hash Table 的原理

- Hash Table 是一種數據結構，使用 hash function 組織數據，因此能支持快速**插入**和**搜尋**
- 使用 hash function : **將 key 映射到 bucket**
  1.  when `insert`: hash function 決定要將 key 分配儲存到哪個 bucket
  2.  when `search`: hash table 使用**相同的** hash function 來查找對應的 bucket，接著**只在特定的 bucket 搜尋**，因此它可以做到快速
- hash function example: `y = x % 7`

### 設計 Hash Table 的注意事項

1. 如何定義好的 hash function
   - 如何盡可能將 key 分配到 bucket 中
   - 取決於 **key 的範圍**和 **bucket 數量**
   - 完美的 hash function 是做到 key 和 bucket 的一對一映射；但現實中不可能無限擴增 bucket，須在 bucket 的容量和數量間權衡
2. 衝突解決算法: 如何處理同一個 bucket 中的 key 
   - 假設儲存最大 key 數的 bucket 有 N 個 key，若 N 很小，可以用 array 儲存，但若 N 很大或是變動的，就需要用 AVL Tree 來儲存 (Adelson-Velsky and Landis Tree)

### Hash Table 的複雜度分析

- 若總共有 M 個 key，則空間複雜度為 $O(M)$
- 若每個 bucket 的 array 大小（儲存的 key 數）為 N，則加入 key 的時間複雜度為 $O(1)$；搜尋的時間複雜度為 $O(N)$
- 若使用 AVL Tree，則最壞情況下，加入 key 和搜尋的時間複雜度為 $O(logN)$

---

後面的範例
- hast set 的表示法是 `{1,2,3,...}`
- hast map 的表示法是 `{0: 0, "g": 1, 3: 5,..}`

---

### 設計二元樹的 key 
1. 當陣列中的排序不重要時，可以用 **排序後的陣列** 當作 key
2. 如果只關心每個值和第一個值的的偏移量，可以用 **偏移量** 當作 key
3. 在二元樹中，用 **子樹的序列化** 表達當作 key

   ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/09/06/screen-shot-2018-02-28-at-143858.png)

4. 在矩陣中，用 **行索引** 或 **列索引** 當作 key
5. 在矩陣中，順對角線的算法是 i + j，逆對角線順序的算法是 i - j

   ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/09/06/screen-shot-2018-02-28-at-140029.png)

6. 在數獨中，用 **行索引和列索引的組合** 來標示元素屬於哪個區塊

   ![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/09/06/screen-shot-2018-02-28-at-145454.png)

---

### 總結

通過 Hash Table 解題的邏輯過程：

![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/09/03/screen-shot-2018-03-09-at-163557.png)
