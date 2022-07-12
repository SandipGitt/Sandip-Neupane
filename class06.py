# def product_one(num1, num2):
#     print(num1 * num2)

# ans = product_one(10 , 12)
# print(f"Answer: {ans}")

# def product_two(num1, num2):
#     return (num1 * num2)

# ans = product_two(10,12)
# print(f"Answer: {ans}")

# def example(*args):
#     print(args)
# example(5,6,45,36,7)

# def example_two(**kwargs):
#     print(kwargs)
# example_two(name ="Sandip", address = "Baneshwor ktm")

def example_three(*args,**kwargs):
    print(args)
    print(kwargs)

example_three(1,4,6,9, name ="Sandip", address = "Baneshwor ktm")



