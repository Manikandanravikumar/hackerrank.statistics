import statistics as st
n = int(input())
values = list(map(int, input().split()))
freqs = list(map(int, input().split()))
s=[]
for i in range(n):
    s+=[values[i]]*freqs[i]
N = sum(freqs)    
s.sort()
if n%2 != 0:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2+1:])
else:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])
ir = round(float(q3-q1), 1)
print(ir)
