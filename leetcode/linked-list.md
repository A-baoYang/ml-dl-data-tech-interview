# Linked List

什麼是 Linked List

- 是一種線性數據結構
- 链表中的每个元素实际上是一个单独的对象，而所有对象都通过每个元素中的引用字段链接在一起。
- 链表有两种类型：单链表和双链表

實作
- 了解单链表和双链表的结构；
- 在单链表或双链表中实现遍历、插入和删除；
- 分析在单链表或双链表中的各种操作的复杂度；
- 在链表中使用双指针技巧（快指针慢指针技巧）；
- 解决一些经典问题，例如反转链表；
- 分析你设计的算法的复杂度；
- 积累设计和调试的经验。

### Single Linked List

特性
- 使用头结点(第一个结点)来表示整个列表
- 想要获得第 i 个元素，我们必须从头结点逐个遍历
- 按索引来访问元素平均要花费 O(N) 时间，其中 N 是链表的长度
- 链表的好处展現在插入和删除操作

add_node
- 不需要将所有元素移动到插入元素之后，可以在 O(1) 时间复杂度中将新结点插入到链表中，这非常高效

delete_node 
- 找到要刪除節點的前一個 prev，將其指標指向下下個；如果是最後一位，則指向 `None`
- 找出 next 只消 O(1) 
- 缺點是找出 prev 要需从头结点遍历链表，平均时间是 O(N) N 是链表的长度
- 空间复杂度为 O(1)，因为我们只需要常量空间来存储指针


### Desigin Linked List

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        # 加速: 初始設置一個空節點
        self.head = Node()
        # 加速: 直接紀錄個數
        self.length = 0
    
    def get(self, index: int) -> int:
        # 假如長度大於一個以上，就一直往後找到 position == index 為止
        if index < self.length:
            cur_node = self.head
            for i in range(index):
                cur_node = cur_node.next
            return cur_node.next.val
        return -1 

    def addAtHead(self, val: int) -> None:
        # 直接指定為 head node 
        self.head.val = val
        # 創一個空節點
        null_node = Node()
        # 空節點後面接剛剛新增的節點
        null_node.next = self.head
        self.head = null_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        null_node = self.head
        while null_node:
            if null_node.next == None:
                null_node.next = Node(val)
                break
            null_node = null_node.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        insert_node = Node(val)
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            pass
        else:
            cur_node = self.head
            for i in range(index):
                cur_node = cur_node.next
                
            next_node = cur_node.next
            cur_node.next = Node(val)
            cur_node.next.next = next_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            cur_node = self.head
            for i in range(index):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next

            self.length -= 1
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```
![](https://i.imgur.com/Si4lQEk.png)

### Double Pointer
1. 两个指针从不同位置出发：一个从始端开始，另一个从末端开始；
2. 两个指针以不同速度移动：一个指针快一些，另一个指针慢一些。

> Cases using Double ppinter:

### circular linked list

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```

![](https://i.imgur.com/bXNzNj1.png)

### circular linked list II

```python
class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        # 將 fast 移回 head，找環狀起點
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
```

![](https://i.imgur.com/VUke4jv.png)

### Intersection of Two Linked Lists

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointerA, pointerB = headA, headB
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        return pointerA

```
![](https://i.imgur.com/nfDsvDa.png)


### 删除链表的倒数第n个节点

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # fast 先行 n 步, fast & slow 再一起遍歷全部 linked list
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
```

![](https://i.imgur.com/CgebQFV.png)

## 複雜度分析

- 如果只使用指针，而不使用任何其他额外的空间，那么空间复杂度将是 O(1)
- 時間複雜度則與 运行循环的次数 有關
  - 如果没有循环，快指针需要 N/2 次才能到达链表的末尾，其中 N 是链表的长度
  - 如果存在循环，则快指针需要 M 次才能赶上慢指针，其中 M 是列表中循环的长度
  - M <= N 且每次循环為常量级的时间，因此時間複雜度是 O(N)
  - 对所有情况进行分析，並考虑最糟糕的情况。


### 反转链表 Reversed Linked List

思路
- 按原始顺序迭代结点，并将它们逐个移动到列表的头部
複雜度分析
- 每个结点只移动一次，因此 时间复杂度为 O(N)， N 是链表的长度
- 只使用常量级的额外空间，因此 空间复杂度为 O(1)

```python

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new, cur = None, head
        while cur:
            nextnode = cur.next  # nextnode: 2
            cur.next = new  # 1->2 -> 1->None
            new = cur  # new: None -> new: 1
            cur = nextnode  # cur: 1 -> cur: 2
        return new

```

![](https://i.imgur.com/QjnWDkI.png)


### 移除链表中相符元素

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 空鏈表則跳出
        if not head:
            return 
        # 添加 null head
        null_as_head = ListNode(None, next=head)
        cur = null_as_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return null_as_head.next
```

![](https://i.imgur.com/HLFwFYk.png)


### 奇偶鏈表

```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        odd = head
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head
```
[ref](https://leetcode.cn/problems/odd-even-linked-list/solution/zui-po-su-de-xiang-fa-dai-ma-zhu-shi-fei-chang-xia/)

![](https://i.imgur.com/ki2oUEF.png)

### 回文链表

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]

```
[ref](https://leetcode.cn/problems/aMhZSa/solution/hui-wen-lian-biao-by-leetcode-solution-3q3r/)

![](https://i.imgur.com/8u6oHRl.png)

#### 小結

- 同时使用多个指针
  - 记住需要跟踪哪些结点，并且可以自由地使用几个不同的结点指针来同时跟踪这些结点
- 由於單鏈表沒有記憶前一節點，你需要跟踪当前结点的前一个结点
  

### 双链表 Double Linked List
- 与单链接列表类似，我们将使用头结点来表示整个列表
- 与单链表不同的是，双链表的每个结点中都含有两个引用字段 (`prev`, `next`)

!!!! 待理解 double linked list 寫法
```python
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    def get(self, index: int) -> int:
        if index + 1 and index < self.size:
            cur = self.dummy_head.next
            pos = 0
            while pos < index:
                cur = cur.next
                pos += 1
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, next=self.dummy_head.next)
        self.dummy_head.next.prev = new_node
        self.dummy_head.next = new_node
        new_node.prev = self.dummy_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.dummy_tail.prev.next = new_node
        new_node.prev = self.dummy_tail.prev
        new_node.next = self.dummy_tail
        self.dummy_tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        cur = self.dummy_head.next
        pos = 0 
        if index + 1 and index <= self.size:
            while cur.next and pos < index:
                cur = cur.next
                pos += 1
            new_node.next = cur 
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.dummy_head.next
        pos = 0
        if index + 1 and index < self.size:
            while pos < index:
                cur = cur.next
                pos += 1
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.size -= 1
```

![](https://i.imgur.com/iDWoCyH.png)

## 結論
Single & Double linked list
- 它们都无法在常量时间内随机访问数据。
- 它们都能够在 O(1) 时间内在给定结点之后或列表开头添加一个新结点。
- 它们都能够在 O(1) 时间内删除第一个结点。
- 刪除的部分
  - 在单链表中，它无法获取给定结点的前一个结点，因此在删除给定结点之前我们必须花费 O(N) 时间来找出前一结点。
  - 在双链表中，这会更容易，因为我们可以使用“prev”引用字段获取前一个结点。因此我们可以在 O(1) 时间内删除给定结点。
- 如果你需要经常添加或删除结点，链表可能是一个不错的选择。
- 如果你需要经常按索引访问元素，数组可能是比链表更好的选择。

![](https://i.imgur.com/i2WmoVG.png)

## 綜合練習

### 合并两个有序链表

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        cur_new = dum
        while list1 and list2:
            if list1.val < list2.val:
                cur_new.next = list1
                list1 = list1.next
            else:
                cur_new.next = list2
                list2 = list2.next
            cur_new = cur_new.next

        cur_new.next = list1 if list1 else list2
        return dum.next
```

![](https://i.imgur.com/TrMMzGs.png)

### 两数相加

```python
class Solution:
    def reverseLinkedList(self, head):
        if not head: return head
        pre, cur = None, head
        count = 1
        while cur.next:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
            count += 1
        return pre, count

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 先加完再倒敘輸出
        l1_val, l2_val = [], []
        while l1:
            l1_val.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_val.append(str(l2.val))
            l2 = l2.next
        sum_val = int("".join(l1_val[::-1])) + int("".join(l2_val[::-1]))
        sum_val = [int(i) for i in str(sum_val)][::-1]

        cur = ret = ListNode()
        for i in range(len(sum_val)):
            cur.next = ListNode(sum_val[i])
            cur = cur.next
        return ret.next
```

![](https://i.imgur.com/0hd2Gdg.png)

### 扁平化多级双向链表

```python
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            # 遇到子節點
            if cur.child:
                child = cur.child
                next_item = cur.next
                cur.next = child
                cur.child = None  # 要記得將子節點移除
                child.prev = cur
                # 找到子節點的最尾端
                while child.next:
                    child = child.next
                # 接上前一層 在子節點之後 還沒走過的節點們
                if next_item:
                    next_item.prev = child
                child.next = next_item
            cur = cur.next
        return head
```

![](https://i.imgur.com/iX7Ryse.png)

### 复制带随机指针的链表

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        # 複製所有節點，insert 到原本節點之後
        while cur:
            cur.next = Node(cur.val, cur.next, random=None)
            cur = cur.next.next  # 因為後一個是複製的節點、所以要跳一個
        
        # 如此一來可以根據原節點 random pointer 所指向的位置，判斷新節點的 random pointer 要指向哪邊
        cur, copyHead = head, head.next
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next  # 因為後一個是複製的節點、所以要跳一個
        
        # 輸出前要將複製節點與原有節點的連結分開
        # 這邊蠻抽象不易懂
        cur, cur_ = head, copyHead
        while cur and cur_:
            cur.next = cur_.next
            cur = cur.next
            if cur:
                cur_.next = cur.next
            cur_ = cur_.next
        return copyHead
```

![](https://i.imgur.com/Yy8AvZv.png)

### 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, head: Optional[ListNode]) -> int:
        if not head: return 0
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        return length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        # 計算 linked list 長度
        length = self.get_len(head)
        # 使用快慢指針取得倒數第 k 個，名為 start 
        fast, slow = head, head
        k = k % length
        if not k: return head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        
        start_head = slow.next
        # 要將 start 原節點前面的 link 取消
        slow.next = None
        # 將 start 後面移到開頭
        fast.next = head
        return start_head
```
[ref](https://leetcode.cn/problems/rotate-list/solution/fu-xue-ming-zhu-wen-ti-chai-fen-fen-xian-z4dr/)

![](https://i.imgur.com/Q8pc5DF.png)

---

Finished!

![](https://i.imgur.com/J0VxWX7.png)
