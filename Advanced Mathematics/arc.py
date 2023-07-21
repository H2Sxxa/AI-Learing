import numpy as np

#正反函数相消
#sin(x) = y
#arcsin(y)= x
#arcsin(sin(x))=x
print(np.arcsin(np.sin(1)) == 1.0)
#这样也是一样成立
print(np.sin(np.arcsin(np.arcsin(np.sin(1)))) == 1.0)

'''


'''