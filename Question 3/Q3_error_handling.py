#ERROR PRONE CODE 

# global_variable = 100
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# def process_numbers():
#     global global_variable
#     local_variable = 5
#     numbers = [1, 2, 3, 4, 5]

#     while local_variable > 0:
#         if local_variable % 2 == 0:
#             numbers.remove(local_variable)
#         local_variable -= 1

#     return numbers

# my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# result = process_numbers(numbers=my_set)

# def modify_dict():
#     local_variable = 10
#     my_dict['key4'] = local_variable

# modify_dict(5)

# def update_global():
#     global global_variable
#     global_variable += 10

# for i in range(5):
#     print(i)
#     i += 1

# if my_set is not Node and my_dict['key4'] == 10:
#     print("Condition met!")

# if 5 not in my_dict:
#     print("5 not found in the dictionar!")

# print(global_variable)
# print(my_dict)
# print(my_set)








# Corrected the misspelling "Node" to "None".
# Removed the argument passing to 'modify_dict' as it does not accept any arguments.
# Changed 'not in' to 'not in my_dict.values()' to check for the value '5' in dictionary values.

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):  # Added the 'numbers' parameter to the function definition
    global global_variable
    local_variable = 5
    numbers = list(numbers)  # Convert set to list since sets do not support indexing

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5}  # Removed duplicate numbers since sets do not allow duplicates
result = process_numbers(my_set)  # Corrected the function call to pass 'my_set' correctly

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict()  # Removed the unnecessary argument '5'

def update_global():
    global global_variable
    global_variable += 10

update_global()  # Added function call to 'update_global' to execute the function

for i in range(5):
    print(i)
    # Removed 'i += 1' as it's unnecessary. The 'for' loop already increments 'i'.

if my_set is not None and my_dict['key4'] == 10:  # Corrected the misspelling 'Node' to 'None'
    print("Condition met!")

if '5' not in my_dict.values():  # Changed to check if the string '5' is not a value in my_dict
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
