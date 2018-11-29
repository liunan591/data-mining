# -*- coding: utf-8 -*-

import pandas

#%%1.数据结构Series 类似python的字典
#创建：
s = pandas.Series([1,2,3,4,5], index=['a','b','c','f','e']) #Index相当于字典的key
pandas.Series ( {'a':5} ) #用字典建立对象

#查询对象中的元素
s[['a','b','c']] #直接查询一组key，返回用这组key和对应value组成的新Series对象
s['a'] #直接查询某个key，返回value
#head(n), tail(n) #取出头n行或尾n行的方法，默认n=5
#index    values #两个对象属性，可以取得key列表和values

#元素统计方法
len(s) #Series长度,包括NaN
s.count() #Series长度，不包括NaN
s.unique() #返回不重复values值
s.value_counts() #value出现次数统计

#%%2.数据结构DataFrame
#创建   
pandas.DataFrame([s,s,s]) #使用Series建立，每一行为一个series
df=pandas.DataFrame([s1,s2]) #使用列表的列表建立，每一行为一个列表anaaffsfsdfa
df=pandas.DataFrame({"a":s1,"b":s2}) #使用字典结合列表建立，每一列为一个列表，字典key作为新对象的列的标题

#查看对象中的元素
df.columns #返回列名称列表，.tolist()可以将结果转化为list
df.iloc[0:6] #类似于数组切片
df["列名"]    #根据列名定位列，中括号里边可以传list
for index, row in df.iterrows(): #以行遍历整个数据，返回值为每行数据的数组
    print(row.values)
#df.head(n), df.tail(n) #取出头n行或尾n行的方法，默认n=5

#元素统计方法
df.shape    #返回数据行数和列数组成的元素

#计算+-*/
df["列名"]/1000   #对列进行除以1000的操作
df["列名"]*df["列名"]    #对应位置运算

#特征
df["列名"].max()  #min,average

#排序
df.sort_values("列名", inplace = True)    #替换原有列，从小到大
df.sort_values("列名", inplace = True, ascending = False)    #替换原有列，从大到小

#列编辑
df['four']=df['one']+df['three']    #通过列的对应计算增加新列
del df['one']   #通过删除索引删除列
df.pop('two')   #通过出栈删除列

#行编辑
df.loc['b'] #通过行标签查看行
df.iloc[2]  #通过行索引查看行
df = df.append(df2) #增加行
df = df.drop(0) #删除索引为0的行

#%%3.数据探索

#查找空值及处理
df.isnull()
pandas.isnull(df)

#分类处理
df.pivot_table(index,values,aggfunc)