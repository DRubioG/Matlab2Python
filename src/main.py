
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
        
        self.conversion(file_path)
    

    def conversion(self, file_path):
        numpy_flag = False

        file = self.open_file(file_path)

        file_aux = self.subs(file, "%", "#")

        file_aux = self.subs(file_aux, "\n")

        numpy_flag, file_aux = self.change_array(file_aux)

        file_aux = self.multiple_lines(file_aux)

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
    
    def multiple_lines(self, line):
        list = []
        for i in line:
            j = i.split(";")
            if not j[-1]:
                j=j[0:-1]
            if len(j) != 1 and j:
                list.extend(self.is_comment(j))
            else:
                list.append(i)
        return list
    
    def is_comment(self, line):
        out = ""
        lis = []
        flag = 0
        flag2 = 0
        if type(line) is list:
            cont = 0
            for l in line:
                l = l.lstrip()
                if l[0] == "#":
                    flag = 1
                    cont -= 1
                    break
                cont += 1

            cont2 = 0
            
            if flag == 1:
                for l in  line:
                    if cont2 == cont:
                        out += l
                        flag2 = 1
                    else:
                        cont2 += 1
                        lis.append(l)

                if flag2 == 1:
                    lis.append(out)
            else:
                lis = line
            
            
        return lis

    def change_array(self, list):
        lis = []
        numpy_flag = False
        con = 0
        flag = False
        for line in list:
            if line.find("[") != -1:
                con += 1
                flag = True
            if line.find("]") != -1:
                con -= 1
            if con != 0 and flag:
                print()

        return numpy_flag, lis



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