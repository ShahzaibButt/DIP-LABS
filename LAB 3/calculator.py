def Add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
op=input("Enter operator")
if(op == "+"):
    print(Add(a,b))
elif(op == "-"):
    print(sub(a,b))
elif(op == "*"):
    print(mul(a,b))
elif(op == "/"):
  print(div(a,b))
