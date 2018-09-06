# -*- coding: utf-8 -*-
import re

#%%排除字符
regular = r"[^ab]\w+"   #非a或b字符开始的字符串
print(re.search(regular,"dbc"))

#%%匹配所有字符串
regular = r"[\d\D]+"
print(re.search(regular,"dbc"))

#%%忽略优先量词，表示优先匹配后方内容，在量词后加？
regular = r"\d+?\d{3}"
print(re.search(regular,"123456"))  #匹配1234
regular2 = r"\d+\d{3}"      #不推荐写法，\d重复出现，效率低
print(re.search(regular2,"123456")) #全部匹配

#%%引用分组
regular = r"""(?x)     #多行注释模式
^(\d{6})    #前6位，地域信息
(\d{8})     #7-14位，生日信息
(\d{3})     #顺序码
([\dxX])    #校检码
$"""
print(re.search(regular,""))

#%%非捕获分组，在括号开始时加上?:
regular = r"(?:(\d)\1)"     #第一个括号不计入分组
print(re.search(regular,"220"))  

#%%反向引用
regular = r"((\d)\2)"
print(re.search(regular,"220"))  

regular2 = r"((\d)\2)"
print(re.sub(regular2,"\g<1>33","220"))

#%%单词边界\b，非单词边界\B
regular = r"\b\w+\b"
print(re.findall(regular,"hello world")) 

#注意！ 反向引用中的断言（eg：\b）都会被忽略
regular2 = r"(\b\w+\b)\s+\1"
print(re.search(regular2,"hello helloworld"))

#匹配重复单词
regular3 = r"(\b\w+\b)\s+\b\1\b"
print(re.search(regular3,"hello hello world"))

#%%环视，环视并不匹配字符
'''
(?=xxx)     向右环视
(?<=xxx)    向左环视
(?<!xxx)    向左环视，不为xxx
(?!xxx)     向右环视，不为xxx
'''
regular = r"(?=abc)\w+"
print(re.search(regular,"hello abc")) 

regular2 = r"(?<=l)o"
print(re.search(regular2,"hello abc")) 

regular3 = r"(?<=ll)(?<=ll)o"   #此处两个环视都为对o左侧相同位置的环视
print(re.search(regular3,"hello abc")) 

#%%环视嵌套
regular = r"(?=abc(?=\b))\w+"   #此处\b环视是在abc之后的位置
print(re.search(regular,"hello abc"))

#%%匹配模式(?模式表达式)
'''
'''
#1.不区分大小写
regular = r"(?i)ello"
print(re.search(regular,"hEllo abc")) 

#2.单行模式，点号匹配一切字符
regular1 = r"(?s).*abc"
print(re.search(regular1,"hello abc\nabc")) 

#3.多行模式，^$可以匹配行的开头和结尾
regular2 = r"(?m)^\d.*"
print(re.search(regular2,"1.hEllo\n2.abc")) 
#3.1可以替换^$为行头行尾添加信息
print(re.sub(r"(?m)$",". ","1.hEllo\n2.abc"))

#4.注释模式
regular3 = r"""(?x)
(\d{4})-    #年
(\d{1,2})-  #月
(\d{1,2})   #日
"""
print(re.search(regular3,"2018-2-25").groups()) 
