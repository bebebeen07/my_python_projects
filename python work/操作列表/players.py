#切片
players=['charlie','martina','michael','florence','eli']
print(players[-3:])
#遍历切片
players=['charlie','martina','michael','florence','eli']
print('Here are the first three players on my team:')
for players in players[:3]:
    print(players.title())
#复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
#动手试一试
#4.10切片
numbers=list(range(1,20))
print(f'the first three items on the list are {numbers[:3]}')
print(f'Three items from the middle of the list are:{numbers[8:11]}')
print(f'The last three items on the list are：{numbers[-3:]}')
#你的比萨，我的比萨
friends_pizzas=['tomato','potato','chicken']
my_pizzas=friends_pizzas[:]
friends_pizzas.append('beef')
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
print('My friend favorite pizzas are:')
for friend_pizza in friends_pizzas:
    print(friend_pizza)
#使用多个循环
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for my_food in my_foods:
    print(my_food)
