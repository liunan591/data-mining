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
df = pandas.DataFrame([s,s,s]) #使用Series建立，每一行为一个series
df = pandas.DataFrame([s1,s2]) #使用列表的列表建立，每一行为一个列表anaaffsfsdfa
df = pandas.DataFrame({"a":s1,"b":s2}) #使用字典结合列表建立，每一列为一个列表，字典key作为新对象的列的标题

#基础属性
df.shape    #行数、列数

#索引
#获取index：df.index
#指定index ：df.index = ['x','y']
#重新设置index : df.reindex(list("abcedf"))
#指定某一列作为index ：df.set_index("Country",drop=False) 可以传入数组，设定复合索引
#返回index的唯一值：df.set_index("Country").index.unique()

#查看对象中的元素
df.columns #返回列名称列表，.tolist()可以将结果转化为list
df.iloc[0:6] #类似于数组切片 按行 数字索引
df.iloc[0:6,0:3]   #取前六行，前三列，等价于df.iloc[0:6,[0,1,2]]
df.loc["w",["A","B"]] #取索引为w行的A、B列 名称索引
df[df["A"]>100] #布尔索引，取df["A"]>100的行信息
df["列名"]    #根据列名定位列，中括号里边可以传list
#要遍历数据帧(DataFrame)中的行，可以使用以下函数 -
    # iteritems() - 迭代(key，value)对
    # iterrows() - 将行迭代为(索引，系列)对
    # itertuples() - 以namedtuples的形式迭代行
for index, row in df.iterrows(): #以行遍历整个数据，返回值为每行数据的数组
    print(row.values)
    
#列编辑
df['four']=df['one']+df['three']    #通过列的对应计算增加新列
del df['one']   #通过删除索引删除列
df.pop('two')   #通过出栈删除列
df.pipe(func,arg2)  #以df中的每一个元素依次为输入，与第二个后边传入的参数进行功能为func的计算
df.apply(func,axis=0)  #按行或者列执行某个函数
df['col1'].map(lambda x:x*100)
df.applymap(lambda x:x*100)
#行编辑
df.loc['b'] #通过行标签查看行
df.iloc[2]  #通过行索引查看行
df = df.append(df2) #增加行
df = df.drop(0) #删除索引为0的行

#元素统计方法
df.shape    #返回数据行数和列数组成的元素
df.dtypes   #数据格式
df.ndim     #数据维度
df.index    #行索引
df.columns  #列索引
df.values  #值 二维ndarray数组

#特征
df["列名"].max()  #min,average
df.head()   #取出头n行或尾n行的方法，默认n=5
df.tail()
df.info()   #信息概览：行数、列数、列索引、列非空值个数、列类型、内存占用
df.describe() #快速统计：计数，均值、标准差、最大值、最小值、四分位数

#计算+-*/
df["列名"]/1000   #对列进行除以1000的操作
df["列名"]*df["列名"]    #对应位置运算


#排序
df.sort_values("列名", inplace = True)    #替换原有列，从小到大
df.sort_values("列名", inplace = True, ascending = False)    #替换原有列，从大到小


#合并
df.join(df)     #按行索引合并信息
df.merge(right, how='inner', on=None, left_on=None, right_on=None, 
         left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), 
         copy=True, indicator=False, validate=None)
df.merge(df,left_on="",right_on="",how="inner") #按指定列合并列
# inner outer left right    合并过程中的确实值nan补全

df.append

#%%3.数据探索

#查找空值及处理
df.isnull()
pandas.isnull(df)

#分组
grouped = df.groupby(by="columns_name")
grouped = df.groupby(by=["Country","State/Province"])
grouped = df["Country"].groupby(by=[df["Country"],df["State/Province"]])
#grouped是一个DataFrameGroupBy对象，是可迭代的
#grouped中的每一个元素是一个元组
#元组里面是（索引(分组的值)，分组之后的DataFrame）

#分类处理
df.pivot_table(index,values,aggfunc)