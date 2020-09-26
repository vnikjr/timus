k,n=map(int,input().split())
a=map(int,input().split())
cars=0
for x in a:
    cars+=x
    cars-=k
    if cars <0:
        cars=0
print(cars)
#timus
