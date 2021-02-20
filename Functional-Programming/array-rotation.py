#check array rotation for the given lists

# lst=[1,2,3,4,5,6]
# rot_lst=[4,5,6,1,2,3]
#
# def rotate(lst,rot_lst):
#     new_lst=lst[len(lst)//2:]+lst[:len(lst)//2]
#     print(new_lst)
#     if new_lst==rot_lst:
#         print("rotation")
#     else:
#         print("no rotation")
# rotate([1,2,3,4,5,6],[4,5,6,1,2,3])

lst1=[1,2,3,4,5,6]
rot_lst=[4,5,6,1,2,3]


def rotate(lst1,rot_lst):
    new_lst = lst1[len(lst1) // 2:] + lst1[:len(lst1) // 2]
    print(new_lst)
    if new_lst==rot_lst:
        print("rotation")
    else:
        print("no rotation")
rotate([1,2,3,4,5,6],[4,5,6,1,2,3])

