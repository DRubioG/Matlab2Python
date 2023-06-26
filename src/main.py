
# file_name = "../matlab examples/example1.m"

# file = open(file_name, 'r')
# file_lines = file.readlines()

# print(file_lines)

# substitute comments
# list1 = []
# list_array = ""
# for i in file_lines:
#     line = i.replace("%", "#")
#     line = line.replace("\n", "")
#     list1.append(line)
#     if line.find("[") != -1:
#         pos_i = line.find("[")
#         list_array = line[pos_i+1:]
#     if line.find("]") != -1:
#         pos_f = line.find("]")
#         list_array = line[pos_i+1:pos_f]
#     if list_array.find(";")!= -1:
#         pass
#     else:
#         list_array = list_array.replace(" ", ",")

# print(list1)

class Matlab2Python:
    def __init__(self, file_path):
        # self.file_path = file_path
        self.conversion(file_path)
    

    def conversion(self, file_path):
        file = self.open_file(file_path)

        file1 = self.subs(file, "%", "#")
        file2 = self.subs(file1, "\n")

        pass
        
    def open_file(self, file_path):
        file = open(file_path, 'r')
        list_file = file.readlines()
        return list_file

    def subs(self, list, char_prev, char_next=""):
        new_list = []
        for i in list:
            new_list.append(i.replace(char_prev, char_next))
        return new_list
    

if __name__=="__main__":
    obj = Matlab2Python("../matlab examples/example1.m")

# # clear \n
# list2 = []
# for i in list1:
#     line = i.replace("\n", "")
#     if line is not "":
#         list2.append(line)
# print(list2)

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
# list_array = []
# cont = 0
# for array in list2:
#     if array.find("[") != -1:
#         cont += 1
#         flag = 1
#     if array.find("]") != -1:
#         cont += -1
    
#     if flag == 1:
#         list_array.append(array)
    
#     if flag == 1 and cont == 0:
#         flag = 0


#         list_array = []


# change 



# change matlab function to python function
# for i in list_array:
#     i.replace("disp", "print")


# regenerate file