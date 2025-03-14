my_list = []
print (my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending: ",my_list)
my_list.insert(1,15)
print("After inserting:",my_list)
numbers=[50,60,70]
print(numbers)
my_list.extend(numbers)
print("After extending:",my_list)
del my_list[-1]
print(my_list)
my_list.sort()
print(my_list)
index_of30 =my_list.index(30)
print("Found index of 30:",index_of30)
