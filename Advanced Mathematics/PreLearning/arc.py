import numpy as np

#正反函数相消
#sin(x) = y
#arcsin(y)= x
#arcsin(sin(x))=x
print(np.arcsin(np.sin(1)) == 1.0)
#这样也是一样成立
print(np.sin(np.arcsin(np.arcsin(np.sin(1)))) == 1.0)

'''
由此，我们只需要根据三角函数表即可求得反三角函数值

x    0   0.5π   π   1.5π   2π
sinx 0    1     0    -1     0


记住反正弦函数的定义域为 [-1,1]，值域 [-0.5π,0.5π]

x        0     1      -1
arcsinx  0    0.5π   -0.5π



# 额外三角函数

    |\    
  a |  \  c
    |____\ 
      b

## 正割 sec

sec(A) = 1/cos(A) = c/b

## 余割 csc

csc(A) = 1/sin(A) = c/a

## 余切 cot

cot(A) = 1/tan(A) = b/a

'''