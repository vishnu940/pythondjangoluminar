# #variable length
# def add(*args):
#    return sum(args)
# #total=add(10,20,30,40,50,60)
# print(total)

# def add(*args):
#     for num in args:
#         print(num)
#     return sum(args)
# total=add(10,20,30,40)
# print(total)

# def print_data(*args):
#     print(args)
# print_data("Ajay","Kochi","Thrissur")
#
# #*args means printing any number of arguements in the form of tuple

def print_data(**kwargs):
    print(kwargs)
print_data(name="Ajay",workplace="Ernakulam",address="Thrissur")
#**kwargs means printing any number of arguements in the form of tuple