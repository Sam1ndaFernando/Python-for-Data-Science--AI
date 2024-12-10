# with open("my_file.txt", "w") as file:    
#     content = file.write("hello worled\n")
#     file.write("this ie our python class")
#     print(content)


# with open("my_file.txt", "w") as file: 
#    my_list=["hello wirled\n", "this ie our python class "]    # list eka widiyata eha paththta yawanna thiyana karamayak mekath 
#    file.writelines(my_list)



# with open("my_file.txt", "w") as file: 
#    my_list=["hello wirled\n", "this ie our python class \n"]    # list eka widiyata eha paththta yawanna thiyana karamayak mekath 
#    my_list.append("suddh")
#    file.writelines(my_list)


with open("my_file.txt", "a") as file: 
    file.write("\n we are studdent")