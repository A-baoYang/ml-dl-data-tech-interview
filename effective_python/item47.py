"""
Python 的 object hook 使編寫用於將系統粘合在一起的通用代碼變得容易。
例如，假設我想將數據庫中的記錄表示為 Python 對象，數據庫已經設置了它的模式，我使用與這些記錄對應的對象的代碼也必須知道數據庫的樣子。
然而，在 Python 中， 將 Python 對象連接到數據庫的代碼，不需要顯式指定記錄的模式；它可以是通用的。
這怎麼可能？ instance attributes、`@property` methods、descriptors 皆不能這樣做，因為它們都需要提前定義。
使用 `__getattr__` 特殊方法，這種動態行為成為可能。
如果一個類定義了 `__getattr__` ，那每次在對象的實例字典中找不到屬性時，都會調用該方法：
"""

#%%
class LazyRecord:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = f"Value for {name}"
        setattr(self, name, value)
        return value


"""
如下，我訪問了缺少的屬性 foo。
這會導致 Python 調用上面的 `__getattr__` 方法，該方法會改變實例字典`__dict__`
"""
#%%
data = LazyRecord()
print("Before:", data.__dict__)
print("foo: ", data.foo)
print("After: ", data.__dict__)

"""
>>>
Before: {'exists': 5}
foo:  Value for foo
After:  {'exists': 5, 'foo': 'Value for foo'}

"""

"""
接著，我將日誌記錄添加到 `LazyRecord` ，以顯示實際調用 `__getattr__` 的時間。
請注意我如何調用 `super().__getattr__()` 來實現 superclass 的 `__getattr__` 來獲取真實的屬性值並避免無限遞歸
(Ref - "Item 40: Initialize Parent Classes with super")
"""

#%%
class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f"* Called __getattr__({name!r}), " f"populating instance dictionary")
        result = super().__getattr__(name)
        print(f"* Returning {result!r}")
        return result


#%%
data = LoggingLazyRecord()
print("exists: ", data.exists)
print("First foo: ", data.foo)
print("Second foo: ", data.foo)

"""
>>>
exists:  5
* Called __getattr__('foo'), populating instance dictionary
* Returning 'Value for foo'
First foo:  Value for foo
Second foo:  Value for foo
"""

"""
`exists` 屬性存在於實例字典中，因此 `__getattr__` 永遠不會被調用。
`foo` 屬性最初不在實例字典中，所以調用 `__getattr__` 。
對 foo 的 `__getattr__` 的調用也會執行一個 `setattr` ，它將 `foo` 填充到實例字典中。
這就是為什麼我第二次訪問 foo 時，它沒有記錄對 __getattr__ 的調用。

這種行為對於惰性訪問無模式數據 (lazy accessing schemaless data) 特別有用。
`__getattr__` 運行一次以完成加載屬性的艱苦工作；所有後續訪問都會檢索現有結果。

假設我也想要這個數據庫系統中的紀錄。下次用戶訪問某個屬性時，想知道數據庫中對應的記錄是否還有效，紀錄是否還處於打開狀態。 
此時 `__getattr__` 鉤子不會讓我可靠地執行此操作，因為它將使用對象的實例字典作為現有屬性的快速路徑。

為了啟用這個更高級的用例，Python 有另一個稱為 `__getattribute__` 的 object hook。
每次訪問 object 上的屬性時都會調用此特殊方法，即使在屬性字典中確實存在該屬性的情況下也是如此。
這使我能夠執行像是檢查每個屬性訪問...有關全局狀態之類的事情。
需要注意的是，這樣的操作會產生大量開銷並對性能產生負面影響，但有時這是值得的。

以下我將 `ValidatingRecord` 定義為每次調用 `__getattribute__` 時記錄：
"""


#%%
class ValidatingRecord:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print(f"* Called __getattribute__({name!r})")
        try:
            value = super().__getattribute__(name)
            print(f"* Found {name!r}, returning {value!r}")
            return value
        except AttributeError:
            value = f"Value for {name}"
            print(f"* Setting {name!r} to {value!r}")
            setattr(self, name, value)
            return value


#%%
data = ValidatingRecord()
print("exists: ", data.exists)
print("First foo: ", data.foo)
print("Second foo: ", data.foo)

"""
>>>
* Called __getattribute__('exists')
* Found 'exists', returning 5
exists:  5
* Called __getattribute__('foo')
* Setting 'foo' to 'Value for foo'
First foo:  Value for foo
* Called __getattribute__('foo')
* Found 'foo', returning 'Value for foo'
Second foo:  Value for foo
"""

"""
如果動態訪問的屬性不應該存在，我可以引發 `AttributeError` 導致 Python 的標準缺失
`__getattr__` 和 `__getattribute__` 的屬性行為：
"""


#%%
class MissingPropertyRecord:
    def __getattr__(self, name):
        if name == "bad_name":
            raise AttributeError(f"{name} is missing")


#%%
data = MissingPropertyRcord()
data.bad_name

"""
>>>
Traceback (most recent call last):
  File "item47.py", line 137, in <module>
    data.bad_name
  File "item47.py", line 133, in __getattr__
    raise AttributeError(f"{name} is missing")
AttributeError: bad_name is missing
"""

"""
實現通用功能的 Python 代碼通常以
- `hasattr` 內置函數來確定屬性何時存在
- `getattr` 內置函數來檢索屬性值
這些函數也會在調用 `__getattr__` 之前，先在實例字典中查找屬性名稱
"""

#%%
data = LoggingLazyRecord()  # Implements __getattr__
print("Before: ", data.__dict__)
print("Has first foo: ", hasattr(data, "foo"))
print("After: ", data.__dict__)
print("Has second foo: ", hasattr(data, "foo"))

"""
>>>
Before:  {'exists': 5}
* Called __getattr__('foo'), populating instance dictionary
* Returning 'Value for foo'
Has first foo:  True
After:  {'exists': 5, 'foo': 'Value for foo'}
Has second foo:  True
"""

"""
在上面的例子中， `__getattr__` 只被調用一次。
相反，實現 `__getattribute__` 的 class 在每次使用 `hasattr` 或 `getattr` 時，都會調用該方法

"""
#%%
data = ValidatingRecord()  # Implements __getattribute__
print("Has first foo: ", hasattr(data, "foo"))
print("Has second foo: ", hasattr(data, "foo"))

"""
>>>
* Called __getattribute__('foo')
* Setting 'foo' to 'Value for foo'
Has first foo:  True
* Called __getattribute__('foo')
* Found 'foo', returning 'Value for foo'
Has second foo:  True

"""

"""
現在，假設我想在將值分配給我的 Python 對象時，將數據延遲推送回數據庫。
`__setattr__` 一個類似的 object hook 可以做到這一點，讓你攔截任意屬性賦值。
與使用 `__getattr__` 和 `__getattribute__` 檢索屬性不同，不需要兩個單獨的方法。
`__setattr__` 方法總是在每次於實例上分配屬性時被調用（直接或通過 `setattr` 內置函數）
"""


#%%
class SavingRecord:
    def __setattr__(self, name, value):
        # Save some data for the record
        super().__setattr__(name, value)


"""
以下，我定義了 `SavingRecord` 的日誌記錄 subclass ，稱作 `LoggingSavingRecord`。
它的 `__setattr__` 方法總是在每個屬性分配上調用：
"""


#%%
class LoggingSavingRecord(SavingRecord):
    def __setattr__(self, name, value):
        print(f"* Called __setattr__({name!r}, {value!r})")
        super().__setattr__(name, value)


#%%
data = LoggingSavingRecord()
print("Before: ", data.__dict__)
data.foo = 5
print("After: ", data.__dict__)
data.foo = 7
print("Finally:", data.__dict__)

"""
>>>
Before:  {}
* Called __setattr__('foo', 5)
After:  {'foo': 5}
* Called __setattr__('foo', 7)
Finally: {'foo': 7}
"""

"""
`__getattribute__` 和 `__setattr__` 的問題在於它們在對象的每個屬性訪問時都會被調用，即使您可能不希望這種情況發生。
例如，假設我希望對我的對象進行屬性訪問，以實際查找關聯字典中的鍵

"""


#%%
class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, name):
        print(f"* Called __getattribute__({name!r})")
        return self._data[name]


"""
這需要從 `__getattribute__` 訪問 `self._data` 方法。
但是，如果我真的嘗試這樣做，Python 將遞歸直到它達到它的堆棧限制，然後程序會終止並噴 `RecursionError`
"""

#%%
data = BrokenDictionaryRecord({"foo": 3})
data.foo

"""
>>>
* Called __getattribute__('_foo')
* Called __getattribute__('_data')
* Called __getattribute__('_data')
* Called __getattribute__('_data')
...
Fatal Python error: Cannot recover from stack overflow.
Python runtime state: initialized

"""

"""
問題是 `__getattribute__` 訪問 `self._data` 方法導致 `__getattribute__` 再次運行，從而再次訪問 self._data 不斷遞歸
解決方案是使用 `super().__getattribute__` 方法從實例屬性字典中獲取值。這避免了遞歸
"""


#%%
class DictionaryRecord:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        print(f"* Called __getattribute__({name!r})")
        data_dict = super().__getattribute__("_data")
        return data_dict[name]


#%%
data = DictionaryRecord({"foo": 3})
print("foo: ", data.foo)

"""
>>>
* Called __getattribute__('foo')
foo:  3
"""

"""
✦ 使用 `__getattr__` 和 `__setattr__` 延遲加載和保存對象的屬性。 
✦ `__getattr__` 僅在訪問缺少的屬性時才被調用，而 `__getattribute__` 會在每次訪問任何屬性時被調用。 
✦ 通過使用 `super()` 中的方法訪問實例屬性，避免 `__getattribute__` 和 `__setattr__` 中的無限遞歸。

"""

# demo
#%%
class A(object):
    def __init__(self, x):
        self.x = x

    def __getattr__(self, name):
        # `__getattr__` will be called undefined attribute
        print("(__getattr__) get: ", name)
        setattr(self, name, "default")
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        print("(__setattr__) set:", name, "=", value)
        self.__dict__[name] = value
        # super().__setattr__(name, value)

    def __getattribute__(self, name):
        # `__getattribute__` will be called all attributes
        print("(__getattribute__) attribute:", name)
        return super().__getattribute__(name)


#%%
a = A(1)
# %%
print(a.x)
#%%
print(a.y)
#%%
a.y = 2
print(a.y)
