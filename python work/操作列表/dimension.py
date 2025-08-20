#定义元组
dimensions=(200,50)

print(dimensions[0])
print(dimensions[1])


#遍历元组中的所有值
for dimension in dimensions:
    print(dimension)


#修改元组变量
dimensions=(200,50)

print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)

print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)


#动手试一试
foods=('banana','cherry','rice','noodles','apple')

print('Original foods are:')
for food in foods:
    print(food)

Modified_foods=('pear','blueberry','rice','noodles','apple')

print('\n\nModified foods are:')
for Modified_food in Modified_foods:
    print(Modified_food)
