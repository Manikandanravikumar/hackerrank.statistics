s = int(input())
x = list(map(int, input().split()))
w=list(map(int, input().split()))
sum_w=0
for i in range(s):
    sum_w += x[i]*w[i]
print(round(sum_w/sum(w),1))

