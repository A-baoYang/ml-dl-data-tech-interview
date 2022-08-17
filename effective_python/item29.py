# 情境：概括式常見於 「需要在多個地方參考相同的計算」

stock = {"nails": 125, "screws": 35, "winguts": 8, "washers": 24}
order = ["screws", "winguts", "clips"]


def get_batches(count, size):
    return count // size


# 直覺但最不簡潔
result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)
# {'screws': 4, 'winguts': 1}

# 使用字典概括式，更簡潔了一點
found = {
    name: get_batches(stock.get(name, 0), 8)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}
print(found)
# {'screws': 4, 'winguts': 1}


# 上面這方法有問題 `get_batches(stock.get(name, 0), 8)` 重複了影響可讀性，且可能因參數設置不一致產生不同結果
has_bug = {
    name: get_batches(stock.get(name, 0), 4)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}
print("Expected: ", found)
print("Found: ", has_bug)
# >>>
# Expected:  {'screws': 4, 'winguts': 1}
# Found:  {'screws': 8, 'winguts': 2}


# 使用 walrus operator := 將指定式加入概括式一部分，消除多餘呼叫
found = {
    name: batches for name in order if (batches := get_batches(stock.get(name, 0), 8))
}
print(found)
# >>>
# {'screws': 4, 'winguts': 1}

# 要注意定義指定式的位置
# result = {name: (tenth := count // 10) for name, count in stock.items() if tenth > 0}
# >>>
# Traceback ...
# NameError: name 'tenth' is not defined


# 移到條件式內
result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(result)
# >>>
# {'nails': 12, 'screws': 3, 'washers': 2}

# 如果一個概括式 在值的部分使用 walrus 、且沒有條件式
# 他會將迴圈變數洩漏到外圍範疇 (containing scope, 作法21)
half = [(last := count // 2) for count in stock.values()]
print(f"last item of {half} is {last}")

# 這情況類似於 for loop 會發生的
for count in stock.values():
    pass
print(f"last item of {list(stock.values())} is {count}")

# 但如果概括式沒有使用 walrus，就不會有洩漏的情形
half = [count // 2 for count in stock.values()]
print(half)
print(count)


# 最好不要洩漏迴圈變數，建議只在一個概括式的條件部分使用 walrus
# 使用迭代器 (iterator) 而非 dict
found = (
    (name, batches) for name in order if (batches := get_batches(stock.get(name, 0), 8))
)
print(next(found))
print(next(found))

# 都在使用但不知道叫這個名稱 XD


# 指定運算式讓概括式和產生器運算式 能在同一個概括式的其他地方重複使用來自條件式的值，改善可讀性與效能
# 應避免在概括式或產生器運算式的條件式外部使用一個指定運算式
