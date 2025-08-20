cars=input("What kind of car would you like to rent:")
print(f"Let me see if I can find a {cars.title()}")

book=input("How many people are there in the restaurant:")
book=int(book)

if book>8:
    print(f"There aren't more table for {book}.")
else:
    print(f"We do have some tables for {book} left now.")