# helpers

classes/interpolate.py

```py
x = np.array([1,4])
y = np.array([0.003,0.18])

inter = Interpolate(x, y)

# lin: linear interpolation
lin_interpolate = inter.lin()
print(lin_interpolate(2)) # 0.062 -> x=2
print(lin_interpolate(3)) # 0.121 -> x=3

# log: logaritmic interpolation
inter.log_degree = 2
log_interpolate = inter.log()
print(log_interpolate(2)) # 0.0915 -> x=2
print(log_interpolate(3)) # 0.1432 -> x=3

# exp: exponential interpolation
exp_interpolate = inter.exp()
print(exp_interpolate(2)) # 0.01174 -> x=2
print(exp_interpolate(3)) # 0.04597 -> x=3

# min: fixed percentage increase
min_interpolate = inter.min()
min_interpolate = inter.min()
print(min_interpolate(10)) # 0.0033 -> %10 increase
print(min_interpolate(50)) # 0.0045 -> %50 decrease

# max: fixed percentage decrease
max_interpolate = inter.max()
print(max_interpolate(10)) # 0.162 -> %10 decrease
print(max_interpolate(50)) # 0.09 -> %10 decrease
```
