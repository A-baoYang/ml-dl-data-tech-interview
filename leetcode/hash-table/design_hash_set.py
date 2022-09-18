import math


class CustomHashSet:
    def __init__(self, key_range) -> None:
        # 初始化 table & bucket
        # key range : 0 <= k <= 10^6
        self.bucket_num = int(math.sqrt(key_range)) + 9
        self.table = [[] for _ in range(self.bucket_num)]

    def hash_func(self, key):
        # 分配 key 要儲存到哪個 bucket
        return key % self.bucket_num

    def add(self, key):
        hashkey = self.hash_func(key)
        if key not in self.table[hashkey]:
            self.table[hashkey].append(key)

    def remove(self, key):
        hashkey = self.hash_func(key)
        if key in self.table[hashkey]:
            self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash_func(key)
        return key in self.table[hashkey]
