#loops

#for <variable> in <iterable>:
    #body

#a = [23,45,67,2]
#for i in a:
# s= input("Enter a number")
#print(s)

#range(start,stop,step)
#range(10)>>>>(1-9)
# sum = 0
# for i in range(16):
#     sum += i  # sum = sum +i
#     print(sum)
# print(f"Sum is  {sum}")

# myList = []
# for i in range(10):
#     n = input("Enter Number:")
#     if n % 2 == 0:
#         myList.append(n)

# print(myList)

# Multiple = []
# for i in range(1,50):
#     if i%3 == 0:
#         Multiple.append(i)

# print(Multiple)

# #List comprehension

# alist = [i for i in range(1,51)]
# #print(alist)

# slist =  [i for i in range(1,51) if i % 3 == 0]
# print(slist)

# main = []
# even = []
# odd = []
# duplicate = []
# for i in range(15):
#     n = input(("Enter number:"))
#     if n not in main:
#         if n % 2 == 0:
#             even.append(n)
#         else:
#             odd.append(n)
#     else:
#         duplicate.append(n)
#     main.append(n)
# print(main)
# print(even)
# print(odd)
# print(duplicate)

# n = "12d567d895d56"
# total = 0
# values = n.split("d")
# for i in values:
#     total += int(i)
# #print(total)

# total = sum([int(i) for i in n.split("d")])
# print(total)

# print(sum(range(4, 51,4)))