#3661
#01:01:01
#2345
#00:39:05
#8723
#02:25:23
import datetime


T = int(input())
A = T%60
B = (T//60)%60
C = T//60//60
t = datetime.time(C,B,A)
print(t)
