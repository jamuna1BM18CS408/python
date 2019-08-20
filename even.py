def get():
    l=[]
    n=int(input("enter the count"))
    for i in range(n):
        y=int(input("enter the items"))
        l.append(y)
    return l,n

def compute(l,n):
    even=[]
    for i in range(n):
        if l[i]%2==0:
           even.append(l[i])
    print(even)
    
def main():
              n=0
              length=0
              l,length=get()
              compute(l,length)

main()

          
        
          
