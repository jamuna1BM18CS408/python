try :
    file1 = open("prime.txt","r")
    file2 = open("happy.txt","r")
    prime_str = file1.read()
    happy_str = file2.read()
    prime = prime_str.split(", ")
    happy = happy_str.split(", ")
    lst3 = [int(val) for val in prime if val in happy] #using list comprehension
    print("Overlapping numbers :")
    print(lst3)
    file1.close()
    file2.close()
except IOError :
    print("Files not found")
