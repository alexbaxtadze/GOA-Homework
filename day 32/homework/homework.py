# 2. Format და f-string-ის მაგალითები
def format_example(name, age):
    return "Welcome, {}! You are {} years old.".format(name, age)

def fstring_example(name, age):
    return f"Welcome, {name}! You are {age} years old."
print(format_example("Alex", 30))


def welcome_user(name, age):
    return f"Hello, {name}! You are {age} years old."
print(format_example("Alex", 30))
 


def capitalize_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"
print(capitalize_name("john", "alex"))
 


def reverse_string(text):
    return f"The reversed text is: {text[::-1]}"
print(reverse_string("Hello"))



def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return ' '.join(words)
print(insert_word("This is a test sentence", "great", 2))


def sentence_to_words(sentence):
    return sentence.split()
print(sentence_to_words("This is a test."))
   

def csv_to_list(csv_string):
    return csv_string.split(',')
print(csv_to_list("apple,banana,cherry"))


def paragraph_to_sentences(paragraph):
    return paragraph.split('.')
print(paragraph_to_sentences("This is a sentence. This is another one."))


def append_to_list(lst, item):
    lst.append(item)
    return lst
print(append_to_list([1, 2, 3], 4))



    
   
   