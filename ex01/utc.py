#+3 +10 15.00
#22.00
#0 +2 12.00
#14.00
#+2 -5 17.00
#15.00
#+2 +12 21.00
#7.00
#+12 -10 21.00
#23.00
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
D = C-A+B
if D >= 24:
   D -= 24
if D <= 0:
    D += 24
print(D)