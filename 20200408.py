from typing import List
from typing import Tuple
from typing import Callable
from collections import Counter

Vector = List[float]
'''
def subtract(v:Vector,w:Vector)->Vector:

 assert len(v)==len(w)
 return [v_i-w_i for v_i,w_i in zip(v,w)]

#assert subtract([5,7,9],[4,5,6])==[1,2,3]
print(subtract([5,7,9],[4,5,6]))

Matrix=List[List[float]]

A=[[1,2,3],
   [4,5,6]]

B=[[1.2],
   [3.4],
   [5.6]]

def shape(A: Matrix)->Tuple[int,int]:
    num_rows=len(A)
    num_cols=len(A[0]) if A else 0
    return num_rows,num_cols

print(shape(A))
#assert shape(([1,2,3],[4,5,6]))==(2,3)

def make_matrix(num_rows:int,
                num_cols:int,
                entry_fn:Callable[[int,int],float])->Matrix:
    return[[entry_fn(i,j)]
        for j in range(num_rows)
            for i in range(num_cols)]

def f1(i,j):
    return(i*j)

A1=make_matrix(3,5,f1)
print(A1)


def vector_sum(vectors: List[Vector])-> Vector:
   return[sum(int(i) for i,j in vectors), sum(int(j) for i,j in vectors)]
print((vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]])))
'''


def median(v: List[float])->float:
   s=sorted(v)
   m = s[len(s)//2] if len(v)%2==1 else (s[len(s)//2]+s[len(s)//2-1])/2
   return m


assert median([1,10,2,9,5])==5
assert median([1,9,2,10])==(2+9)/2


num_friends=[1,2,3,4,5,6,7,8,1,1,6,6]
def mode(x: List[float])->List[float]:
    counts=Counter(num_friends)
    n = max(counts.values())
    res=[i for i,c in counts.items() if c == n]
    return res


assert set(mode(num_friends)) == {1, 6}
print(mode(num_friends))