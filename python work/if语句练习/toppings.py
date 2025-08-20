#检查特殊元素
requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')
print('\nFinished making your pizza!')


requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print('Sorry,we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}')
print('\nFinished making your pizza.')


#确定列表非空
requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}.')
    print('\nFinished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')


#使用多个列表
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping.title()}')
    else:
        print(f"Sorry,we don't have {requested_topping.title()}")
print('\nFinished making your pizza.')


#动手试一试
nams=['tiffa','vivian','john','admin','serina']

for nam in nams:
    if nam=='admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print(f'Hello {nam.title()},thank you for logging in again.')
else:
        print('We need to find some users!')
print(nams)
nams.pop(0)
nams.pop(0)
nams.pop(0)
nams.pop(0)
nams.pop(0)   
print(nams)


current_users=['Tiffa','Vivian','John','ADMIN','Serina']
new_users=['bob', 'admin', 'alice', 'jake', 'licy']

for new_user in new_users:
    if new_user.upper() in current_users:
       print('You need to change your name') 
    elif new_user.upper() not in current_users:
        print('the name have not been used yet')


nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num==1:
        print(f'{num}st')
    elif num==2:
        print(f'{num}nd')
    elif num==3:
        print(f'{num}rd')
    else:
        print(f'{num}th')