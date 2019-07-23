---
title: 'Insert title here'
key: ae3238dcc7feb9adecfee0c395fc8dc8
---

## 2D Numpy Arrays

```yaml
type: TitleSlide
key: 0cc8abf493
```

`@lower_third`
name: Full Name
title: Instructor

`@script`


---

## Type of Numpy Arrays

```yaml
type: FullSlide
key: 1b9db47fd2
```

`@part1`
```py
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
type(np_height)
```

```out
numpy.ndarray
```

```py
type(np_weight)
```

```out
numpy.ndarray
```

`@script`


---

## 2D Numpy Arrays

```yaml
type: FullSlide
key: ebb550dcba
```

`@part1`
```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
```

```out
                          [65.4, 59.2, 63.6, 88.4, 68.7]])
```

```py
np_2d
```

```out
array([[  1.73,   1.68,   1.71,   1.89,   1.79],
       [ 65.4 ,  59.2 ,  63.6 ,  88.4 ,  68.7 ]])
```

```py
np_2d.shape
```

```out
2 rows, 5 columns
```

```py
np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
```

```out
                  [65.4, 59.2, 63.6, 88.4, \"68.7\"]])

```

`@script`


---

## Subsetting

```yaml
type: FullSlide
key: e0062fa1e4
```

`@part1`
0                       1                        2                      3                       4
 0                       1                        2                      3                       4

```py
np_2d[0]
```

```out
array([ 1.73,  1.68,  1.71,  1.89,  1.79])
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0,2]
```

```out
1.71
```

`@script`


---

## Subsetting

```yaml
type: FullSlide
key: 5417c722e9
```

`@part1`
0                       1                        2                      3                       4
 0                       1                        2                      3                       4

```py
np_2d[0]
```

```out
array([ 1.73,  1.68,  1.71,  1.89,  1.79])
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0,2]
```

```out
1.71
```

```py
np_2d[:,1:3]
```

```out
array([[  1.68,   1.71],
       [ 59.2 ,  63.6 ]])
```

`@script`


---

## Subsetting

```yaml
type: FullSlide
key: e71d2fc8b8
```

`@part1`
0                       1                        2                      3                       4
 0                       1                        2                      3                       4

```py
np_2d[0]
```

```out
array([ 1.73,  1.68,  1.71,  1.89,  1.79])
```

```py
np_2d[0][2]
```

```out
1.71
```

```py
np_2d[0,2]
```

```out
1.71
```

```py
np_2d[:,1:3]
```

```out
array([[  1.68,   1.71],
       [ 59.2 ,  63.6 ]])
```

```py
np_2d[1,:]
```

```out
array([ 65.4,  59.2,  63.6,  88.4,  68.7])
```

`@script`


---

## Let's practice!

```yaml
type: FinalSlide
key: 6047b27c09
```

`@script`
