# Data Sets

## Dynamical2D:
- `GeneratePoints`:<br>
Generate a set of points in $[0,1]\times [0,1]$ defined by the dynamical system :
$$
x_{n+1} = x_n + r(1-y_n) \mod{1}
$$
$$
y_{n+1} = y_n + r(1-x_n) \mod{1}
$$
where $(x_0, y_0)$ and $r$ is given. If `x0` and/or `y0`, is not specified, then they are initialized to random values.<br>
- `animate_r`: <br>
Animate the dynamical system with fixed initial conditions and varying $r$ values.
- `animate_X`: <br>
Animate the sequence $(X_n,Y_n)_{n=0} ^{N-1}$ 
