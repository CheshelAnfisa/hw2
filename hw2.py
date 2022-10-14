#1
s=int(input())
print(s*2)

#2
s=int(input())
print(s**2)

#3
print('Hours')
a=int(input())
print('Minutes')
b=int(input())
print('Seconds')
c=int(input())
s=a*3600+b*60+c
print(s, s/(3600*24))

#4
s=int(input())
if s%10==7:
    print('TRUE')
else:
    print('FALSE')

#5
print('a')
a=int(input())
print('b')
b=int(input())
print('c')
c=int(input())
d=b**2-4*a*c
if a==0:
    if b==0:
        print('Корней нет')
    else:
        print(-c/b)
else:
    if d>0:
        x1=(d**0.5-b)/(2*a)
        x2 = (-1*(d ** 0.5 - b) / (2 * a))
        print('x1=', x1, 'x2=', x2)
    if d<0:
        print('Корней нет')
    if d==0:
        x1=-b/(2*a)
        print(x1)

#6
a=[]
for i in range(3):
    a[i]=int(input())
print(max(a))

#7
s=int(input())
a=0
d=0
for i in range(s+1):
    if i%5==0 or i%2==0:
        a+=1
        d+=i
a=1
sr=d/a
strsr=str(sr)
dot(strsr.fund('.'))
print(strsr[:(dot+3)])