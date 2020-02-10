#!/usr/bin/env python
# coding: utf-8

# In[1]:


from py_mini_racer import py_mini_racer
import pandas as pd


# In[2]:


ctx = py_mini_racer.MiniRacer()


# In[3]:


# 使用l10n.js而不是l10n.json，是因为js可以加注释，纯json不能加注释
with open("l10n.js") as f:
    js_code = f.read();
    ctx.eval(js_code)
json = ctx.eval("json") # list


# In[4]:


# 列出所有语言 以及extension_id
extensions = set()
for lang in json:
    print("lang:",lang)
    extension_ids = []
    for text_id, text in json[lang].items():
        extension_id = text_id.split(".")[0]
        if extension_id in extension_ids:
            continue
        else:
            extension_ids.append(extension_id)
            print("  ",extension_id)


# In[5]:


# 使用pandas, 输出为xlsx
json['jp'] = {}
df = pd.DataFrame(json)


# In[6]:


df.to_excel("l10n.xlsx")

