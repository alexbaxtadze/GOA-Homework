#საკლასო დავალება:

#მომხმარებელს შემოატანინეთ სახელი და შეინახეთ name ცვლადში.

#შემდეგ შემოატანინეთ არჩევანი (რომელიც იქნება "u" ან "l") და შეინახეთ ეს ინფორმაცია choice ცვლადში.

#თუ choice ტოლია "u"-სი, მაშინ მომხმარებლის სახელი გამოიტანეთ uppercase-ში.
#თუ choice ტოლია "l"-ის, მაშინ მომხმარებლის სახელი გამოიტანეთ lowercase-ში.
#სხვა შემთხვევაში, დაუბეჭდეთ wrong information.


name=input("enter your name:")
choice=input("select case u/l-")

if choice == "u": print(name.upper())
elif choice=="l": print(name.lower())
else:print("wrong answer")

