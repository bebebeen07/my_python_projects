#简单的if语句
age=19

if age>=18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')


#if-else语句
age=17

if age>=18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry,you are too young to vote.')


#if-elif-else语句
age=45

if age<14:
    price=0
elif age<18:
    price=25
elif age>=18:
    price=40
print(f'Your admission cost is {price}')


#测试多个条件
requested_toppings=['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
elif 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print('\nFinished msking your pizza!')


#动手试一试
alien_color=['green','yellow','red']

if 'green' in alien_color:
    print('You get 5')


alien_color=['green','yellow','red']
if 'green' in alien_color:
    print('You get 5')
else:
    print('you get 10')


age=30

if age<2:
    print('he is a baby')
elif 2<=age<4:
    print('he is a child')
elif 4<=age<13:
    print('he is a teenager')
elif 13<=age<18:
    print('he is an adult')
elif 18<=age<65:
    print('he is a grown man')
else:
    print('he is old enough')


favorite_fruits=['banana','apple','pear']
if 'banana' in favorite_fruits:
    print('You really like banana')
if 'apple' in favorite_fruits:
    print('You really like apple')
if 'pear' in favorite_fruits:
    print('You really like pear')