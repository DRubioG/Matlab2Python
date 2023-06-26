
file_name = "../matlab examples/example1.m"

file = open(file_name, 'r')
file_lines = file.readlines()

print(file_lines)

# substitute comments
list1 = []
for i in file_lines:
    line = i.replace("%", "#")
    list1.append(line)
print(list1)

# clear \n
list2 = []
for i in list1:
    line = i.replace("\n", "")
    if line is not "":
        list2.append(line)
print(list2)

# TODO: change ";"
# list2 = []
# for line in list1:
    
#     if line.find(";") != -1:
#         line_split = line.split(";", -1)
#         if line_split[1] != "":
#             pass

#         # if len(line_split) > 2:
#         #     list2.append(line_split)
#     else:
#         list2.append(line)
# print(list2)

# change vector/array shape
list_array = []
cont = 0
for array in list2:
    if array.find("[") != -1:
        cont += 1
        flag = 1
    if array.find("]") != -1:
        cont += -1
    
    if flag == 1:
        list_array.append(array)
    
    if flag == 1 and cont == 0:
        flag = 0


        list_array = []





# change matlab function to python function
for i in list_array:
    i.replace("disp", "print")


# regenerate file