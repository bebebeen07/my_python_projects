#遍历整个列表
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title())
#在for循环中执行更多操作
magicians=['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()},that was a great trick!')
    print(f'I can not wait to see your next trick,{magician.title()}.\n')
#在for循环之后执行一些操作
print('Thank you,everyone.That was a great magic show!')
#避免缩进错误
#动手试一试
pizzas=['tomato','potato','chicken']
for pizza in pizzas:
    print(pizza.title())
    print(f'I like {pizza.title()} pizza.')
print('\nI really like pizza.')
#animals
animals=['panda','girrfi','lion']
for animal in animals:
    print(animal.title())
    print(f'A {animal.title()} would be a great pet.')
print('Any of these animals would make a great pet!')
