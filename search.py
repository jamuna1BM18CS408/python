def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False
lis=[]
while True:
    a=int(input("enter the element"))
    if a!=-1:
        lis.append(a)
    else:
        break
b=int(input("enter the element to be searched"))
v=search(lis,b)
if v==True:
    print("element found")
else:
    print("not found")
    
