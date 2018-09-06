# -*- coding: utf-8 -*-

import seaborn as sns
sns.set(color_codes=True)
#%%绘图常用指令

#%%单因素分析
"""
#条形图
sns.distplot(x,bins = bins, kde = False)

"""
#%%两因素分析
"""
#散点图与因素条形图
sns.jointplot(x = c1, y = c2, data = data)
#散点密度图与条形图
sns.jointplot(x = c1, y = c2, kind = "hex", data = data)
"""

#%%离散与连续因素分析（离散、连续属性加一个布尔属性）
"""
#分类散点图（x、y中必有一个为离散属性，一个为连续属性）
sns.stripplot(x = c1, y = c2, data = data, jitter = True)   #散点显示，jitter控制散点分散
sns.swarmplot(x = c1, y = c2, data = data)  #散点显示，散点在离散属性上树状展开

#盒图，在离散维度上统计x,y中的另一个元素，可区分hue属性
sns.boxplot(x = c1, y = c2, data = data,hue = c3)

#小提琴图，在离散维度上统计x,y中的另一个元素，split要求hue属性只有两个值
sns.violinplot(x = c1, y = c2, data = data,hue = c3,split=True)

#条形图（显示值的集中）
sns.barplot(x = c1, y = c2, data = data,hue = c3)

#点图（显示差异性）
sns.pointplot(x = c1, y = c2, data = data,hue = c3)
"""

#%%
if __name__ == "__main__":
    titanic = sns.load_dataset("titanic")
    tips = sns.load_dataset("tips")
    iris = sns.load_dataset("iris")