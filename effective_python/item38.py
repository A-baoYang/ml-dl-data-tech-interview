"""
Python 的許多內建 API 都允許我們傳入一個函式來自動行為，例如 defaultdict
因為函式比類別物件更容易描述和定義，且因為 Python 有 first-class 函式：函式與方法可被到處傳遞或參考
API 會在他們執行時使用 hooks 來 callback 我們的程式碼
以下舉例： `len()` 這個內建函式當作 key 進行排序

"""
names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
names.sort(key=len)
print(names)


"""

在 Python 中很多 hooks 都是無狀態的函式，具有定義完善的引數和回傳值
例如 defaultdict，它允許我們傳入一個函式，在每次存取到缺少的 key 時被呼叫
這個傳入的函式需要回傳要賦予那個缺少的 key 應有的預設值
如作者所定義的 `log_missing()` 函式

"""

from collections import defaultdict


def log_missing():
    """
    當 key 不存在於 defaultdict 時會印出 Key added
    並自動創建 key: value, value = 0
    """
    print("Key added")
    return 0


"""
給訂一個初始字典 及 一組想要增加到初始字典的值組
執行看看 los_missing 函式會印出幾次 Key added 
"""

current = {"green": 12, "blue": 3}
increments = [
    ("blue", 17),
    ("orange", 9),
    ("red", 5),
]
result = defaultdict(log_missing, current)

print("Before:", dict(result))
for key, amount in increments:
    result[key] += amount
print("After: ", dict(result))

"""
現在我們在優化一下這個方法
把「計算 key added 次數」的功能加到傳入 defaultdict 的函式中
"""


def increment_with_report(current, increments):
    """
    將上面那個實作包成函式，並印出有新增幾個 key
    """
    added_count = 0

    def missing():
        """
        使用 nonlocal 操作從外層函式捕捉的變數
        """
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count


result, count = increment_with_report(current, increments)
print(result, count)
assert count == 2

"""
>>> 程式回傳了我們預想的結果，計算 Key Added 為兩次
"""

"""
不過這有一個問題是閱讀性不佳
所以有另一種做法是定義一個 Class 封裝我們想要追蹤紀錄的狀態
像這樣使用輔助類別的方式會比用 increment_with_report 更清楚
"""


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        """
        將 log_missing() 和 increment_with_report 中的 missing() 結合
        自動新增 key 值時，同時計算新增的次數，存到物件的內建變數 added
        """
        self.added += 1
        return 0


"""
在 Python 中因為 first-class function 的緣故
CountMissing.missing 方法依然可以被傳入 defaultdict 中，當作預測值的 hook
如下範例
"""

counter = CountMissing()
result = defaultdict(counter.missing, current)  # Method ref
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(result)
print(counter.added)

"""
但是光看這個類別，沒看過 defaultdict 的使用範例前，沒辦法立即了解它的用途
(誰構建 CountMissing 物件、誰呼叫 missing 方法、這個類別未來需要新增其他公開方法嗎？)
因此要釐清這個情況，Python 允許 Class 內定義 `__call__` 特殊方法
`__call__` 能讓一個物件像函式一樣被呼叫
能以這種方式執行的所有物件被統稱為 callables
"""


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        """
        使用 BetterCountMissing 可直接被呼叫並執行定義好的功能
        """
        self.added += 1
        return 0


counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)
print(callable(counter))

counter = BetterCountMissing()
result = defaultdict(counter, current)  # Relies on __call__
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(result)
print(counter.added)


"""
- 不需要定義並實體化那個 class，就可以單純使用函式作為 Python 中元件之間的介面
- Python中隊函式和方法的參考是 first-class 的、表示他們可被用在運算式中
- `__call__` 特殊方法能讓一個 class 的實體像是普通的 Python 函式那樣被呼叫
- 當我們需要一個函式來維護狀態，可考慮定義一個提供 `__call__` 方法的 class
"""
