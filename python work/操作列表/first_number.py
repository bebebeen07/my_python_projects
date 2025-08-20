#创建数值列表
for value in range(1,5):
    print(value)
#使用range()创建数值列表
numbers=list(range(1,6))
print(numbers)
#even_number
even_numbers=list(range(2,11,2))
print(even_numbers)
#square_number
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
#对数值列表执行简单的统计运算
#列表推导式
squares=[value**2 for value in range(1,11)]
print(squares)
#动手试一试
for values in range(1,21):
    print(values)
numbers=list(range(1,21,2))
for value in numbers:
    print(value)
three_numbers = list(range(3,31,3))
print(f"3~30之间的奇数：{three_numbers}")
for value in three_numbers:
    print(value)
squares=[]
for value in range(1,11):
    square=value**3
    squares.append(square)
print(squares)
squares=[value**3 for value in range(1,11)]
print(squares)