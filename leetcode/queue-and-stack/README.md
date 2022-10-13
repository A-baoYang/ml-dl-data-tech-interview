# Queue & Stack

- Queue: FIFO 先入先出
- Stack: LIFO 後入先出

## Queue 隊列

![](https://pic.leetcode-cn.com/44b3a817f0880f168de9574075b61bd204fdc77748d4e04448603d6956c6428a-%E5%87%BA%E5%85%A5%E9%98%9F.gif)

動作 
- 增: insert, enqueue
- 刪: delete, dequeue

結構
- 單向隊列
  - 相較起來比較低效
- 循環隊列
  - 使用固定大小的數組和 2 指針分別指向起始和結束位置
  - 可重用之前浪費的空間
  - `head` 指針指向隊列要 dequeue 的位置
  - `tail` 指針指向隊列要 enqueue 的位置
  - 通過這兩指針判斷目前 queue 是滿 or 空

## 廣度優先搜尋 BFS

- 是一種遍歷或搜尋數據結構（樹或圖）的算法
- 例如找到從起點到終點的最短路徑
- 距離 root 越近的節點先走到，依次遍歷與 root 距離 1 步, 2 步, 3 步 ... 的節點
- 節點的處理順序是 先進先出 (FIFO)\
- 使用 hash table 確保 **永遠不會訪問一個節點兩次**；除非數據結構中完全沒有循環




