def welcome():
    print("Welcome Students")

#welcome() #>>call by reference
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
def sum(num1,num2):
    print (num1+num2)
def diff(num1,num2):
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)

sum (num1,num2)
diff(num1,num2)

