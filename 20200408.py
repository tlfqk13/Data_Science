from typing import List
from typing import Tuple
from typing import Callable

Vector=List[float]

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