import numpy as np
from scipy import stats
s=int(input())
num=list(map(int, input().split()))
print(np.mean(num))
print(np.median(num))
print(int(stats.mode(num)[0]))
