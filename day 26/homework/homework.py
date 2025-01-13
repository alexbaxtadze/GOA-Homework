

def sum_of_two_numbers(num1, num2):
   
    return num1 + num2


result = sum_of_two_numbers(5, 7)
print("The sum is:", result)




def even_or_odd_return(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_or_odd_return(4)
print(result)  # შედეგი: Odd


def reverse_string(s):
   
    return s[::-1]


result = reverse_string("hello")
print("Reversed string:", result)  
