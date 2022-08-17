"""
    - Topic : Class variable
    - Source Link :https://www.pythontutorial.net/python-oop/python-class-variables/
"""

#%%
"""
    Get values of class variables
"""


class HtmlDocument:
    extension = "html"
    version = "5"


#%%
print(HtmlDocument.extension)  # html
print(HtmlDocument.version)  # 5
print(HtmlDocument.media_type)  # AttributeError

# %%
"""
    Use getattr() to get class variables
    - can specify a default value if the class variable not exist
"""
extension = getattr(HtmlDocument, "extension")
print(extension)  # html
version = getattr(HtmlDocument, "version")
print(version)  # 5

media_type = getattr(HtmlDocument, "media_type", "text/html")
print(media_type)  # text/html

# %%
"""
    Set values for class variables
"""

HtmlDocument.version = 10

setattr(HtmlDocument, "version", 10)

print(HtmlDocument.version)  # 10
# %%

HtmlDocument.media_type = "text/html"

setattr(HtmlDocument, "media_type", "text/html")

print(HtmlDocument.media_type)  # text/html

# %%
"""
    Delete class variables
"""

delattr(HtmlDocument, "version")

# del HtmlDocument.version

print(HtmlDocument.version)  # AttributeError

# %%
"""
    storage of class variables
"""

from pprint import pprint


class HtmlDocument:
    extension = "html"
    version = "5"

    def render():
        print("Rendering the html doc...")


HtmlDocument.media_type = "text/html"

pprint(HtmlDocument.__dict__)

# mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
#               '__doc__': None,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
#               'extension': 'html',
#               'media_type': 'text/html',
#               'version': '5'})

# %%
# __dict__ not allow to change
HtmlDocument.__dict__["released"] = 2008
# TypeError: 'mappingproxy' object does not support item assignment

# %%
