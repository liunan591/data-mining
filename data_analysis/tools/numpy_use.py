# -*- coding: utf-8 -*-
 
#%%
import numpy as np
 
#%%ndarray (n dimensional array)
#creat array
ar = np.array([[1,2,3], [2,3,4]])    #by list
np.zeros((2,3))                    #by shape and 0
np.ones((2,3))                     #by shape and 1
np.full((2,2), 8)                  #by shape and 8
np.eye(3)                          #by dig(3)
np.random.random((3,2))            #by random and shpae
np.empty((2,3,4))                  #by random and shpae
np.arange(15)                      #by list [0-15] not include 15
#change dtype
#int8\int16\int32\int64     整数
#uint8\uint16\uint31\uint64     无符号整型
#float16\float32\float64\float128 浮点数
#complex64\complex128\complex256 分别为两个32、64、128位浮点数表示的复数
#bool 布尔值
#dtype include intxx floatxx
np.inf  #无穷大
np.nan  #非数字类型 两个nan是不相等的，nan与任何值计算都为nan
int_arr = np.array([1,2,3,4,5])
float_arr = int_arr.astype(np.float64)
int_arr.astype(dtype=float_arr.dtype)
np.round np.around  #四舍五入
#使用astype将float转换为int时小数部分被舍弃
 
#get element
print (ar[1,2])     #get the element in Second row, third column
print (ar[1][2])    #the same to up
print (ar.shape)    #get the shape
br = ar[0:2,2:4]    #if you don't want to change ar by br,br = ar[x,x].copy()
a = np.array([[1,2], [3, 4], [5, 6]])
print (a[[0,1,2], [0,1,0]])
print (a[a>2])
print (a[::2,1])
 
#calculate
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x+y,'\n',np.add(x,y))     #calculate for each element
print(x-y,'\n',np.subtract(x,y))
print(x*y,'\n',np.multiply(x,y))
print(x/y,'\n',np.divide(x,y))
print(np.sqrt(x))
print(x.dot(y),'\n',np.dot(x,y))    #calculate for whole matrix
print(x.sum(),'\n',np.sum(x))   #sum all elements in x
print(np.sum(x, axis=0))        #sum the elements for each column
print(np.sum(x, axis=1))        #sum the elements for each row
print(np.mean(x),'\n',x.mean())
print(np.mean(x, axis=0))
 
#reshape
print(x.T,'\n', x.transpose())
arr = np.arange(16).reshape(2,2,4)
print(arr.swapaxes(1,2),'\n',arr.transpose((0,2,1)))

print(arr.ravel())      #reshape to list
print(arr.flatten())    #reshape to list
"""当操作两个array时，numpy会逐个比较它们的shape，
在下述情况下，两arrays会兼容和输出broadcasting结果：
    1.相等
    2.其中一个为1，（进而可进行拷贝拓展已至，shape匹配）"""
v = np.array([1,2,3]).reshape(3,1)
w = np.array([4,5])
print(v+w)
 
#Logic operation
x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
print(np.where(cond, x_arr, y_arr)) #根据条件赋值
print(np.where(x_arr > 1.3, 1,-1))
print(np.where(x_arr > 1.3, 1,x_arr))
print(x_arr.clip(1.2,1.4))  #设定数组的上下限，若不满足，则变为上下线
 
#connect two matrix
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
np.concatenate([arr1, arr2], axis=0)    #shape = 4,3
np.vstack((arr1, arr2)) # vertical
np.r_[arr1, arr2]
np.concatenate([arr1, arr2], axis=1)    #shape = 6,2
np.hstack((arr1, arr2)) # horizontal
np.c_[arr1, arr2]

#split matrix
np.hsplit(matrix,n) #split to n parts by rows
np.hsplit(matrix,(l1,l2)) #split at the position of l1,l2 
np.vsplit
 
#split array
arr = np.random.rand(5,5)
first, second, third = np.split(arr, [1,3], axis=0) #first(1,5)second(2,5)third(2,5)