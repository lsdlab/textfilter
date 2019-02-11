# 敏感关键词过滤输入

https://github.com/observerss/textfilter

添加 setup.py 后可以 pip 安装

`pip install git+https://github.com/lsdlab/textfilter.git`

```python
from textfilter import DFAFilter
f = DFAFilter()
f.add("sexy")
f.filter("hello sexy baby")
hello **** baby
```
