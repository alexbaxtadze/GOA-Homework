

list1=[2 , 4, 6, 8, 10, 12, 14, 16, 18,20]
for x in list1:
    print(x)



              #0  1  2  3  4  5  6  7  8  9
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# მომხმარებლის რიცხვების შეყვანა
num1 = int(input("enter first number : "))
num2 = int(input("enter seconed number : "))

# შემოწმება და slicing
if num1 > num2:
    new_list = my_list[num2:num1]
    print("new list (num1 > num2):", new_list)
elif num2 > num1:
    new_list = my_list[num1:num2]
    print("new list (num2 > num1):", new_list)
else:
    print("numbers are equal, empty list:", )


numbers = [10, 20, 30, 40, 50, 60, 70]

# Printing the first, third, and last elements
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[6])




strings = ["apple", "banana", "cherry", "date", "elderberry"]

# Reversing the list using slicing
reversed_list = strings[::-1]

# Printing the reversed list
print("Reversed list:", reversed_list)



words = ["sun", "moon", "star", "planet", "galaxy", "universe"]

# Printing every second element starting from the first
result = words[::2]

# Output the result
print("Every second element:", result)