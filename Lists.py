#Creating an empty list called my_list
my_list = []
#Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After Appending:",my_list)

#Inserting value 15 to the second position of the list
my_list.insert(1,15)
print("After inserting 15:",my_list)

#Extending the list
my_list.extend([50,60,70])
print("After Extending:",my_list)

#Removing the last element of the list
del my_list[-1]
print("after deleting the last element:",my_list)

#sorting the list in ascending order
my_list.sort()
print("After sorting:",my_list)

#Finding the index of the element 30 in the list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

