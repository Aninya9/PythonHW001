m = int(input())
n = int(input())
k = int(input())

proof1 = k % m
proof2 = k % n

if (proof1 == 0 or proof2 == 0):
    print('yes')
else: print('no')