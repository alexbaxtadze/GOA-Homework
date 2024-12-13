num1=int(input("enter number:"))
range5=range(num1+1)
for x in range5():
    print(x)




correct_password = "12345678"
user_guess = input("Enter password: ")
counter = 0

while user_guess != correct_password:
    user_guess = input("Enter password: ")
    counter += 1

print("Access granted")
print("Your guess count:", str(counter))



my_name=7
your_name=input("enter your name")
while your_name!=my_name:
    your_name=input("enter your name")
    counter +=1

    print("you_guessed")
    print("your guessed number:",str(counter))
