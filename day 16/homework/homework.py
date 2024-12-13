#while ციკლი გამოიყენება მაშინ როდესაც ჩვენ არ გვაქვს ინფორმაცია რამდენი იტერაცია გვაქვს
#for ციკლი გამოიყენება მაშინ როდესაც ვიცით რამდენი იტერაცია გვაქვს
#1 davaleba
for v in range(50):
    print("goa")


#2 dav
counter= 1
while counter<=10:
    print("counter")
counter+=1

#3 dav
counter=2
while counter <=20:
    print(counter)
counter +=2

#4 dav
password = "goa academy"
user_guess = input("Enter password: ")
counter = 0

while user_guess != password:
    user_guess = input("Enter password: ")
    counter += 1

#5 dav
countdown=10
while countdown<=1:
    print("blast off!")



password="GOA ACADEMY"
username="bakhtadze"

user_guess=input("enter password")
user_guess=input("enter username")
counter= 1

while user_guess !=password and username:
    user_guess=input("enter password")
    user_guess=input("enter username")
    counter+=1

