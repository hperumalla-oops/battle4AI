import random
import matplotlib.pyplot as plt
from math import sin, exp

def f(x):
    return 5*x**2 - 7*x + 3*sin(x) - exp(x)

y_val=[]
x=0

max_iter=1000
x_val=[]
step=1

for _ in range(max_iter):
    x_new=x+random.randint(-step,step)/100
    x_val.append(x_new)
    y_val.append(f(x_new))
    x=x_new

print("global maxima:",x,"at f(x):", f(x))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('hill climbing')
plt.plot(x_val,y_val)
plt.grid(True)
plt.show()
