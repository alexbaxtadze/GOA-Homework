def uppercase(sentence):
    print(sentence.upper())

uppercase("this is uppercase sentence")




def display_name_uppercase(): 
    name = input("enter your name: ") 
    print(f"enter your name in big letters: {name.upper()}") 
    display_name_uppercase() 



def list_to_uppercase(strings): 
    return [string.upper() for string in strings] 
print(list_to_uppercase(["apple", "banana", "cherry"])) 




def to_lowercase(sentence):
     print(sentence.lower()) 
     to_lowercase("THIS IS LOWERCASE SENTENCE.") 


def store_email_lowercase(): 
    email = input("enter your email: ")
    print(email.lower())
    store_email_lowercase() 



def to_lowercase_return(string): 
    return string.lower() 
print(to_lowercase_return("this is chosen words.")) 







def capitalize_list(strings): 
    return [string.capitalize() for string in strings]
    print(capitalize_list(["apple", "banana", "cherry"])) 



def capitalize_string(string): 
    return string.capitalize() 
print(capitalize_string("hello word from alex"))
capitalize_string("h,a")