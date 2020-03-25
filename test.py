list1 = [1,2,3,4, [4,1]]
list2 = [1,2,3,4, [4,1]]


A = set()
A.add(str(list1))

if str(list2) in A:
    print("sabii")