name="Eric"
message="Hello "+name.title()+",would you like to learn some python today"
print(message.title())


name="albert einstein"
print(name.title())
print(name.upper())
print(name.lower())
first_name="albert"
last_name="einstein"
full_name=f"{first_name.title()} {last_name.title()}"
message=full_name+" once said,"+'"A person who never made a mistake never tried anything new '
print(message.title())


name=" ada lovelace "
print(name.rstrip())
print(name.lstrip())
print(name.strip())


file_name='python_notes.txt'
file_name.removesuffix(".txt")


number='8'
message="my favorite number is "+number
print(message)