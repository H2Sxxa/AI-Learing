from inspect import getsource
from typing import TYPE_CHECKING, Callable, List, Set

if TYPE_CHECKING:
    class TODO_LIST:
        '''
        # 映射与函数
        
        映射用于反应集合关系，函数在此则充当集合与几何的对应法则
        
        定义域 D()
        
        值域 R()
        
        - [x] 单射
        - [x] 满射
        - [x] 双射
        - [x] 逆映射
        - [x] 函数
        - [x] 反函数
        - [x] 复合映射
        - [x] 复合函数
        '''

def get_setIndex(x:int,setx:Set) -> List[int]:
    return [index for _,index in zip(setx,range(0,len(setx))) if _ == x]

def check_map(setA:Set[int],setB:Set[int],func:Callable[[int],int]=lambda _:_)->None:
    print(setA,"->",setB)
    print(getsource(func).replace("\n",""))
    for i in setA:
        y=func(i)
        if y in setB:
            print(get_setIndex(i,setA),"->",get_setIndex(y,setB))


print("满射，单射，双射（单+满）")
setA:Set = {1,2,3}
setB:Set = {2,3,4}
func = lambda x: x+1

check_map(setA,setB,func)

print("逆映射（仅双射可用）")
refunc = lambda x:x-1

check_map(setB,setA,refunc)

'''
func,refunc都称为函数,同时refunc是func的反函数

A    B
1 -> 1
2 -> 2
3 -> （无法构成映射）

'''

print("复合映射")
'''
funcA: A -> B1
B1是B2的子集
funcB: B2 -> C
则funcA o funcB: A -> C

funcA o funcB称为复合函数
'''
setA:Set={1,2,3}
setB1:Set={2,3,4}
setB2:Set={1,2,3,4}
setC:Set={2,3,4,5}

funcA= lambda x:x+1
funcB= lambda x:x+1

print("A -> B1")
check_map(setA,setB1,funcA)
print("B2 -> C")
check_map(setB2,setC,funcB)
print("A -> C")
check_map(setA,setC,lambda x:funcB(funcA(x)))

