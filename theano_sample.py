import theano.tensor as T
from theano import function
from theano import pp

# 値→関数→適応
"""
Theanoは
値を定義し、
式を作って、関数としてコンパイルし、
適応することができる
"""

## スカラー
x = T.dscalar("x")
y = T.dscalar("y")
z = x + y 
pp(z)
f = function([x,y], z)
f(2,5)

## ベクター
x = T.dvector("x")
y = T.dvector("y")
z = x + y
f = function([x,y], z)
f([1, 2], [3, 4])

## 行列
x = T.dmatrix("x")
y = T.dmatrix("y")
z = x + y
f = function([x,y],z)

f([[1, 2],[3, 4]],[[10, 20],[30,40]])

## numpyのarrayも扱える
import numpy
f(numpy.array([[1,2], [3,4]]), numpy.array([[10,20],[30, 40]]))


# 微分
x = T.dscalar("x")
y = x ** 2
dx = T.grad(y,x)
pp(dx)
f = function([x],[y,dx])
f(3) #>>> [9, 6]


# GPUのチェックコード
from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()
t1 = time.time()
print("Looping %d times took %f seconds" % (iters, t1 - t0))
print("Result is %s" % (r,))
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print('Used the cpu')
else:
    print('Used the gpu')