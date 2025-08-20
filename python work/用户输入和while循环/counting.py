#使用while循环
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

#让用户选择何时退出
prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit'to end the program."

message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
         print(message)

#使用break语句退出循环
prompt="\nPlease enter the name of a city you have visited"
prompt+="\n(Enter 'quit' when you are finished.)"

while True:
    city=input(prompt)

    if city =='quit':
        break
    else:
        print(f"I;d love to go to the {city.title()}!")

#在循环中使用continue
current_number=0
while current_number<=10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

#避免无限循环
#动手试一试
prompt="\nPlease add something in your pizza:"
while True:
    topping=input(prompt)
    if topping=='quit':
     break
    else:
        print(f"Adding {topping.title()}")
    
prompt = "Enter 'quit' to end"
prompt += "\nPlease enter your age:"
 
while True:
    age = input(prompt)
 
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print("免费")
        elif (int(age) >= 3) and (int(age) <= 12):
            print("您的票价为10元。")
        else:
            print("您的票价为15元。")
