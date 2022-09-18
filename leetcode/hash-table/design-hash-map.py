import math


class CustomHashMap:
    def __init__(self) -> None:
        # 初始化 table & bucket
        # key range : 0 <= k <= 10^6
        self.bucket_num = int(math.sqrt(10 ** 6)) + 9
        self.table = [[] for _ in range(self.bucket_num)]

    def hash_func(self, key):
        # 分配 key 要儲存到哪個 bucket
        return key % self.bucket_num

    def put(self, key, value):
        hashkey = self.hash_func(key)
        for entry in self.table[hashkey]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key):
        hashkey = self.hash_func(key)
        for entry in self.table[hashkey]:
            if entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key):
        hashkey = self.hash_func(key)
        for entry in self.table[hashkey]:
            if entry[0] == key:
                self.table[hashkey].remove(entry)
                return
