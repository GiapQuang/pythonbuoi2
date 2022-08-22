'''for x in range (10) : print(x,end=" ")
n=int(input("Nhap n: "))
s=0
for x in range (1,n+1) : s += x*(n+1-x)
print("Tong day = ",s)
'''
# Ham zip
'''a=[1,2,3,4,5]
b=['a','b','c']
c=list(zip(a[::4],b))
print(c)
'''
'''
n=int(input())
a=list(range(1,n+1))
s=0
for x,y in zip(a,a[1:]):s += x*y
print(s)'''
'''from math import sqrt
# kiem tra so nguyen to
n=int(input())
m=int(sqrt(n))
ok=True
for i in range (2,m+1):
    if n % i == 0 :
        ok = False
        break
print("yes" if ok and n>1 else "no")'''

#in ra day fibonacy
'''n = int(input())
F = 2 * [1]
for _ in range(n):
    F.append(F[-1] + F[-2])
print(*F[:n])
'''
#Nhap day so nguyen va tinh
#s1 tong binh phuong cac phan tu
#2 tong nhung so chan
#3 s3 = a1 + (a1 + a2) + (a1 + a2 + a3) + .... (a1 + ..... + an)

'''a = list(map(int, input().split()))
b = [x*x for x in a]
print(sum(b))
c = [x for x in a if x % 2 == 0]
if c == []: print("Khong co so chan")
else:
    print("Tong chan ", sum(c))
    
s = 0
t = 0
for x in a:
    t += x
    s += t
print(s)'''

'''a = [4, 7, 2, 8, 1]
for i, x in enumerate(a):
    print(i, x)
'''

# Nhap day so nguyen kiem tra day so do co tang dan hay khong
'''a = list(map(int, input().split()))
ok = True
for i in range(len(a)-1):
    if (a[i] >= a[i+1]):
        ok = False
        break
print("day tang" if ok else "khong phai day tang")'''

'''a = list(map(int, input().split()))
b = [0 for x, y in zip(a, a[1:]) if x >=y]
print("Day tang " if b==[] else "Khong phai day tang")

'''

'''a = list(map(int, input().split()))
print("doi xung" if a == a[::-1] else "Khong doi xung")'''

'''a = list(map(int, input().split()))
b = [1 for x, y, z in zip(a, a[1:], a[2:]) if x + z == 2 * y]
print("So bo 3 lien tuc csc: ", sum(b))'''

# nhap n tinh tong cac chu so

'''n = int(input())
s = 0
while n > 10:
    s += n % 10
    n = n // 10  # / chia so thuc // chia so nguyen
print(s)
print(sum(map(int,input().split())))'''
# cach 2 print(sum(map(int, input()))))
# giai phuong trinh x^x = a voi thuoc [1, 10^10]
'''a = float(input())
L, R = 1, 10
while R - L > 0.00001:
    M = (L + R) / 2
    if pow(M, M) < a: R = M
    else: L = M
print("x = ", L)'''
from math import *
def kc(x, y, z, t): return sqrt((x - z)*(x - z) + (y - t) * (y - t))

if __name__ == '__main__':
    x0, y0, r, xM, yM = map(float, input().split())
    if kc(x0, y0, xM, yM) <= r: print(xM, yM)
    else:
        xP, yP = x0, y0
        while abs(xP - xM) > 0.0001 or abs(yP - yM) > 0.0001:
            xQ = (xP + xM) / 2
            yQ = (yP + yM) / 2
            if kc(x0, y0, xQ, yQ) > r: xM, yM = x0, yQ
            else: xP, yP = xQ, yQ
        print(xM, yM)