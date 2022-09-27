#Created using Python 3.10 (corepy).

print('hello world')  # Print "hello world" with single line of code.
# or like this:
statement = 'hello world'
print(statement)  # Print "hello world" with variable.

list_1 = ['list1', 'list2', 'list3', 1.10, 2.20, 3.30, 1, 2, 3]  # Create list with strings, floats, and integers.
print(type(list_1))  # Confirm the list object type.
print(list_1[3])  # Print the value of the 4th position in the list.

dict_1 = {'first_key': '1st_val', 'second_key': 2}  # Create dictionary with strings and integers.
print(type(dict_1))  # Confirm the dictionary object type.
print(dict_1['first_key'])  # Print the value of the first_key in the dictionary.

tuple_1 = ('1:00PM', 2.00, '3:PM', 4)  # Create a tuple with strings, floats, and integers.
print(type(tuple_1))  # Confirm the tuple object type.
print(tuple_1[2])  # Print the value of the 3rd index position in the tuple.

list_2 = [list_1, dict_1, tuple_1, '"hello world"']  # Create list containing the four object types created above.
print("There are " + str(len(list_2)) + " objects in list_2!")  # Confirm how many index positions in list_2.
print("The first object in list_2 is: " + str(list_2[0][0]))  # Print the value of the first position in the -
# first object (list_1) in list_2.
print("There are " + str(len(list_2[0])) + " objects in list_1!")  # Confirm how many index positions in the -
# first object in list_2.
print("These are the objects in list_1: " + str(list_2[0]) + " which is in the first position in list_2!") # Print -
# the whole object in the first position of list_2.

print(list_2[3] + ' is the fourth object in list_2!')  # Print "hello world" from list_2.
