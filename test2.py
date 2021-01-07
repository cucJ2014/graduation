import re
mystr = '今天的天气真好，天气真的好'

pattern = re.compile('真')
res = pattern.search(mystr)
print(res)

# search结果
# <_sre.SRE_Match object; span=(3, 5), match='天气'>
# 只有一个结果，返回的是Match object，可以用search[0]得到该字符串

find = re.findall(pattern, mystr)
print(find)