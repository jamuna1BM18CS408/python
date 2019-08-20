def get():
    n=int(input("enter the number of series"))
    return n

def Fibanocci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c

def main():
          n=0
          n=get()
          Fibanocci(n)
        
main()
