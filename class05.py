# using loop in tuple
# a = {'name': 'Sandip', 'address': 'Ktm', 'contact': '9867241584', 'gender': 'Unknown'}
# for key in a.keys():
#     print(key)

# for key, value in a.items():
#     print(key,value)


# properties ={
#     "data":{
#         "profiles":[
#             {
#                 "name":"Ram",
#                 "rank": 1,
#                 "Contact":["987633","97623"]
#             },
#             {
#                 "name":"Sita",
#                 "rank":2,
#                 "contact":["9372523","986322"]
#             }
#         ]
#     },
#     "total_count":2,
# }
# profiles = properties.get("data").get("profiles")
# for profile  in profiles:
#     print("**************")
#     print(f"name: {profile.get('name')}")
#     print(f"rank:{profile.get('rank')}")
#     for idx,contact in enumerate (profile.get("contact"),1):
#         print(f"contact {idx}: {contact}")

# *args , **kwargs search in google

def profile(name, contact, address):
    print(f"Name: {name}")
    print(f"contact: {contact}")
    print(f"address: {address}")

profile("Ram","97864567","Ktm")#positional argument
print("################")
profile(name = "Ram", address = "Ktm", contact= "97864567")#keyword argument
