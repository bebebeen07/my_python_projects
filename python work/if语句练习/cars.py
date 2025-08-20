#一个简单的示例
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


#条件测试_检查是否不等
requested_topping='mushrooms'

if requested_topping!='anchovies':
    print('Hold the anchovies!')


#数值比较
answer=17

if answer!=42:
    print('that is not the correct answer.Please try again!')


#检查特定的值不在列表里
banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(f'{user.title()},you can post a response if you wish.')


#布尔表达式
#动手试一试
cars='bmw'

if cars=='audi':
    print('My predition is right')
else:
    print('My predition is wrong.')

car = 'subaru'
print(car == 'subaru')
print(car == 'audi')

num=8
print(num!=3)
print(num==8)

car='bmw'
print(car.upper()=='BMW')
print(car.title()=='Bmw')

age_0=19
age_1=20
print(age_0==19 and age_1==21)
print(age_0<21 or age_1<19)

fruits=['apple','banana','pear']
fruit='strawberry'
if fruit in fruits:
    print('I like it.')
else:
    print(f'{fruit.title()},I hate it')
