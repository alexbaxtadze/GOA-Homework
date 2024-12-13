num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3



score = float(input("Enter the score (0-100): "))

# Checking the range and assigning the grade
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score"

print("The grade is: {grade}")




num1=float(input("enter number:"))

if num1("is positive"):
    print("num1 is positive:")
elif num1("is negative:"):
    print("num1 is negative")
else:
    print("num1 is zero")




start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))


total_sum = 0


for number in range(start, end + 1):  
    total_sum += number


print(f"The sum of numbers between {start} and {end} is: {total_sum}")
