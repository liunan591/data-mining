# pandas应用指南

使用该文档时，建议结合pandas关联函数的说明信息。在调用具体函数时，跳转到具体的函数声明位置。

## series

```python
s = pandas.Series([1,2,3,4,5], index=['a','b','c','f','e']) #Index相当于字典的key
pandas.Series ( {'a':5} ) #用字典建立对象

#查询对象中的元素
s[['a','b','c']] #直接查询一组key，返回用这组key和对应value组成的新Series对象
s['a'] #直接查询某个key，返回value
#head(n), tail(n) #取出头n行或尾n行的方法，默认n=5
#index    values #两个对象属性，可以取得key列表和values

#元素统计方法
len(s) #Series长度,包括NaN
s.count() #Series长度，不包括NaN
s.unique() #返回不重复values值
s.value_counts() #value出现次数统计
```

## DataFrame

### create

```python
df = pandas.DataFrame()
df = pandas.read_xxx()
```

### base info & data describe

```python
df.shape    #行数、列数
df.dtypes   #数据格式
df.ndim     #数据维度
df.index    #行索引
df.columns  #列索引
df.values  #值 二维ndarray数组

df["列名"].max()  #min,average
df.head()   #取出头n行或尾n行的方法，默认n=5
df.tail()
df.info()   #信息概览：行数、列数、列索引、列非空值个数、列类型、内存占用
df.describe() #快速统计：计数，均值、标准差、最大值、最小值、四分位数
```

### index

#### define

```python
index = pd.Index(['e', 'd', 'a', 'b'])
index = pd.Index(['e', 'd', 'a', 'b'], name='something')
index = pd.DatetimeIndex
columns = pd.Index(['A', 'B', 'C'], name='cols')
df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)

# 多重索引
index = pd.MultiIndex.from_product([range(3), ['one', 'two']], names=['first', 'second'])
# 查看当前级别索引包含的元素
In [60]: index.levels[1]
Out[60]: Index(['one', 'two'], dtype='object', name='second')
# 平铺所需级别的索引
In [59]: index.get_level_values(0)
Out[59]: Int64Index([0, 0, 1, 1, 2, 2], dtype='int64', name='first')

index.set_levels(["a", "b"], level=1) # 设定指定层次的索引
```

#### change

```python
df.index #获取index
df.index.rename('xx',inplace=True) # 为索引重命名
df.rename_axis(['a', 'b']) # 重命名索引或者列名

# 指定index：覆盖原有index
df.index = ['x','y']   
# 指定columns：覆盖原有columns
df.columns = pandas.MultiIndex.from_tuples([('c', 'e'), ('d', 'f')], 							names=['level_1', 'level_2'])
# 指定某一列作为index 可以传入数组，设定复合索引
df.set_index("Country",drop=False)  # 将列作为索引的同时，不删除该列
df.set_index(['a', 'b'], append=True) # 保留原有索引，新增两列索引
# reset_index, 与 set_index相反，他会将索引还原为列，重建一个简单索引
# reset_index 可选参数drop，如果为true，则只丢弃索引
df.reset_index()

# 重新排列index， columns，可以新增行列，缺失值默认为NaN
# 换句话刷 用 df 去匹配给定的行列形成新的数据
df.reindex(labels=None, index=None, columns=None, axis=None, method=None, copy=True, level=None, fill_value=nan, limit=None, tolerance=None)   


df.swaplevel()  #交换复合index的位置
df.droplevel('a') # 删除复合索引中的 a 列索引
df.droplevel('level2', axis=1) # 删除复合列名中的 level2 列名索引
```

#### boolean operation

```python
# union (|)  intersection (&) difference symmetric_difference(^)

In [305]: a = pd.Index(['c', 'b', 'a'])
In [306]: b = pd.Index(['c', 'e', 'd'])

In [307]: a | b
Out[307]: Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

In [308]: a & b
Out[308]: Index(['c'], dtype='object')

In [309]: a.difference(b)
Out[309]: Index(['a', 'b'], dtype='object')
    
In [312]: a.symmetric_difference.(b) # 取出删除所有重复项后的索引（不包含重复的，c 出现于 a,b 中，但是结果中不含c）
Out[312]: Index(['a', 'b', 'd', 'e'], dtype='object')

In [313]: idx1 ^ idx2
Out[313]: Index(['a', 'b', 'd', 'e'], dtype='object')
```

### sort

```python
df.sort_values("列名", inplace = True)    #替换原有列，从小到大
df.sort_values("列名", inplace = True, ascending = False)    #替换原有列，从大到小
```

### merge

```python
# 按行索引合并信息 -> 'DataFrame'   
df.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)  
df.merge(right, how='inner', on=None, left_on=None, right_on=None, 
         left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), 
         copy=True, indicator=False, validate=None)
df.merge(df,left_on="",right_on="",how="inner") #按指定列合并列
# inner outer left right    合并过程中的确实值nan补全
```

### view

```python
#查看对象中的元素
df.columns #返回列名称列表，.tolist()可以将结果转化为list
df.iloc[0:6] #类似于数组切片 按行 数字索引
df.iloc[0:6,0:3]   #取前六行，前三列，等价于df.iloc[0:6,[0,1,2]]
df.loc["w",["A","B"]] #取索引为w行的A、B列 名称索引 的 df对象

# 灵活查看多重索引的
In [56]: idx = pd.IndexSlice
In [57]: dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']]
In [58]: dfmi.loc['A1', (slice(None), 'foo')]

dflookup.lookup(list(range(0, 10, 2)), ['B', 'C', 'A', 'B', 'D']) # 取指定行列数据的数组
df["列名"]    #根据列名定位列，中括号里边可以传list
df.query
#布尔索引
df[df["A"]>100] #布尔索引，取df["A"]>100的行信息
df[df>100] #布尔索引，取df中所有>100的元素正常显示，其他元素填充为Nan
df[::-1] #数据按行切片
df.isin([1,2,3]) # 返回布尔值
df.isin([1,2,3]) & x # 布尔值可以进行运算，注意><号的优先级低于& | 需要加括号
df.isnull() # df.isna
df.where #  可以查找符合条件的值，并对不符合的进行赋值，df.mask

#要遍历数据帧(DataFrame)中的行，可以使用以下函数 -
    # iteritems() - 迭代(key，value)对
    # iterrows() - 将行迭代为(索引，系列)对
    # itertuples() - 以namedtuples的形式迭代行
for index, row in df.iterrows(): #以行遍历整个数据，返回值为每行数据的数组
    print(row.values)
    
df.sample() # 数据采样
```



### change

```python
# 全局编辑
# 对于df中的每一个元素进行加110操作，可以后接pipe方法
df.pipe(lambda x,y:x+y, 110) 

df.applymap(lambda x:x*100)
df.apply(lambda x,y:x+y, 110,axis=0)  #按行或者列执行某个函数
df.drop_duplicates(ignore_index=True)
df.drop(index='cow', columns='small') # 可以传入数组，删除多行多列
dfc.loc[0, 'A'] = 11 # 指定位置修改

# 计算+-*/
df["列名"]/1000   #对列进行除以1000的操作
df["列名"]*df["列名"]    #对应位置运算

#列编辑
df['four']=df['one']+df['three']    #通过列的对应计算增加新列
del df['one']   #通过删除索引删除列
df.pop('two')   #通过出栈删除列
dfmi.loc[:, ('one', 'second')] = value
#行编辑
df = df.append(df1) #增加行
df.loc[3] = {'c':1, 'x':2} # 可以是增加行，也可以是编辑行
df.loc[3] = [1,2]
df.loc[5] = 5



```



### note

1. 索引使用建议

```python
dfmi.loc[:, ('one', 'second')]
dfmi.loc[:, [('one', 'second'),('one', 'first')]]
优于
dfmi['one']['second']
```

在数据直接更改时，建议用loc方案


    

### group

#查找空值及处理
df.isnull()
pandas.isnull(df)

grouped = df.groupby(by="columns_name")
grouped = df.groupby(by=["Country","State/Province"])
grouped = df["Country"].groupby(by=[df["Country"],df["State/Province"]])
grouped.count() #分组中非na值的数量
#sum mean median非na值的统计 std无偏标准差，分母为n-1，var方差 min max
grouped.agg(func)   #对每一个分类的每一列进行一次func计算
#grouped是一个DataFrameGroupBy对象，是可迭代的
#grouped中的每一个元素是一个元组
#元组里面是（索引(分组的值)，分组之后的DataFrame）

#分类处理
df.pivot_table(index,values,aggfunc)

### time

import pandas as pd
#生成时间序列
#pd.date_range(start=None, end=None, periods=None, freq='D')
#start、end、periods生成periods个等间距的时间
#start、end、freq生成freq间隔的时间序列
pd.date_range("2019-08-10 8:00:00","20190830",periods=5) #等分五段
#D日 B工作日 H小时 T/min分 S秒 L/ms毫秒 U微秒 M每月最后一天 BM每月最后一个工作日
#MS每月第一天 BMS每月第一个工作日 W每周周日 
pd.date_range("2019-08-10","20190830",freq="2W") #时间段内的所有周日，每两个取一个

#时间序列转化
index = index=pd.date_range("20190810","20190830",periods=10)
df = pd.DataFrame(list(range(10)),index=index)
df.resample("5D") #等同于group