"""
    - Topic :Methods
    - Source Link : https://www.pythontutorial.net/python-oop/python-methods/

"""

#%%

"""
    Methods
    - function inside class : function
    - call the function via an instance : method
"""


class Request:
    def send():
        print("Sent")


# %%
print(Request.send)  # <function Request.send at 0x7fa877f3c940>
req = Request()
print(req.send)
# <bound method Request.send of <__main__.Request object at 0x7fa87778df40>>

# %%


class Request:
    def send(*args):
        print("Sent", args)


# %%
Request.send()  # Sent ()
# %%

req = Request()

req.send()
# Sent (<__main__.Request object at 0x7fa877409d30>,)
# %%
