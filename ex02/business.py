#100 30 30
#21
#50 20 10
#4
#200 10 0 
#0
N, S, O = input().split()
N = float(N)
S = float(S)
O = float(O)
print((N*0.01*(100-S))*O*0.01)

