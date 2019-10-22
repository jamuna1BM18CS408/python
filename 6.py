
class Validate:
    def __init__(self):
        self.open_list=['[','{','(']
        self.close_list = [']','}',')']
        self.str1 = None
        self.valid = False

    def checkstring(self,str1):
        self.str1 = str1
        stack = []
        for i in str1:
            if i in self.open_list:
                stack.append(i)
            elif i in self.close_list :
                pos = self.close_list.index(i)
                if len(stack)>0 and self.open_list[pos] == stack[-1] :
                    stack.pop()
                else:
                    return "Invalid"
        if len(stack)==0:
            return "Valid"

obj = Validate()
str1 = input("Enter string : ")
print(str1,'-',obj.checkstring(str1))
