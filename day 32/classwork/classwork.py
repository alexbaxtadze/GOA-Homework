#def generate_big_sentence(name, surname, age):
    
 #   print("My name is {}, my surname is {}, and I am {} years old.".format(name, surname, age))


#name = input("Enter your name: ")
#surname = input("Enter your surname: ")
#age = input("Enter your age:")


#generate_big_sentence(name, surname, age)




#def generate_big_sentence(name, surname, age):
    
 #   print(f"My name is {name}, my surname is {surname}, and I am {age} years old.")


#name = input("Enter your name: ")
#surname = input("Enter your surname: ")
#age = input("Enter your age:")

#generate_big_sentence(name, surname, age)




#def my_split(main_string, string_to_split):
    
#    split_result = main_string.split(string_to_split)
#    print(split_result)


#main_string = input("Enter the main string: ")
#string_to_split = input("Enter the string to split by: ")


#my_split(main_string, string_to_split)


def manual_append(main_list , item_to_insert): 
    length = len(main_list)

    print(main_list)
    main_list.insert(length,item_to_insert)
    print(main_list)

manual_append([1, 2, 3,], [4, 5, ])

