# -*- coding: utf-8 -*-
#%%
import matplotlib.pyplot as plt

"""
plt.cla() Clear an axis
plt.clf() Clear the entire figure
plt.close() Close a window
"""
#%%绘制线图
def plot(x,y,save_file = None):
    #prepare data x,y
    #create plot
    fig = plt.figure(figsize=(3,3)) #创建并设置图幅大小
    #plot pane
    ax = fig.add_subplot(111) #row-col-num
    #plot content
    ax.plot(x, y, color='lightblue', linewidth=3)
    ax.scatter([2,4,6],[5,15,25],color='darkgreen',marker='^')
    #set axis
    ax.set(xlim=[1, 6.5],ylim=[-1.5,30])
    ax.set(title='An Example Axes',ylabel='Y-Axis',xlabel='X-Axis')
    #设置x坐标显示的斜度
    plt.xticks(rotation=45)
    #save
    if save_file:
        plt.savefig(save_file)
    #show plot
    plt.show()
    """子图绘制
    ax1 = fig.add_subplot(221) 
    ax3 = fig.add_subplot(212)
    lines = ax3.plot(x,y)
    ax1.scatter(x,y)"""
    
    """绘制其它类型的图
    ax.bar(x,y,width) #条形图
    ax.barh(x,y,width) #横着的条形图
    
    ax.scatter(x,y) #绘制散点图
    
    ax.hist(x) #绘制柱形图，柱的个数自动设定
    ax.hist(x，bins = 4) #绘制柱形图，柱的个数为4
    ax.hist(x，range = (4,6)) #绘制柱形图，范围在4到6
    
    ax.boxplot(x) #绘制盒图
    ax.boxplot(x,y,z) #绘制盒图
    
    """


#%%绘制条形图
def
fig3, axes = plt.subplots(nrows=2,ncols=2)


axes[1,0].barh([0.5,1,2.5],[0,1,2]) #Plot horiontal rectangles (constant height)
axes[0,0].axhline(0.45) #Draw a horizontal line across axes
axes[0,1].axvline(0.65) #Draw a vertical line across axes
axes2[0].fill(x,y,color='blue') #Draw filled polygons
axes2[1].fill_between(x,y,color='yellow') #Fill between y-values and 0
