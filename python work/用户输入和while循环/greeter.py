#编写清晰的提示
name=input("Please enter your name:")
print(f"Hello {name}!")

prompt="If you share your name,we can personalize the messages you see."
prompt+="\nWhat is your first name?"

name=input(prompt)
print(f"\nHello {name}!")

height=input("How tall are you,in inches?")
height=int(height)

if height >=48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll able to ride when you're little older.")

number=input("Enter a number, and I will tell you if it's even or odd:")
number=int(number)

if number%2==0:
    print(f"\nThe number {number}is even.")
else:
    print(f"\nThe number {number} is odd.")