#嘉宾名单
name=['jack','lisa','kate']
print(f'i want to invite {name[0].title()},{name[1].title()} and {name[2].title()} into my party.')
#修改嘉宾名单
print(f'due to sth,{name[0].title()} could not been here')
name[0]='steven'
print(f'i want to invite {name[0].title()},{name[1].title()} and {name[2].title()} into my party.')
#添加嘉宾
print('Good news!I have found a new table,we could invite more than 3 person!')
name.insert(0,'becky')
name.insert(2,'john')
name.append('vivian')
print(f'I want to invite {name[1].title()} to my party')
print(f'I want to invite {name[2].title()} to my party')
print(f'I want to invite {name[3].title()} to my party')
print(f'I want to invite {name[4].title()} to my party')
print(f'I want to invite {name[5].title()} to my party')
#缩短名单
print("i am really sorry that the table could not been here on time so that we could just invite 2 person.")
poped_name1=name.pop()
print(poped_name1)
print('i am sorry for my mistake')
poped_name2=name.pop()
print(poped_name2)
print('i am sorry for my mistake')
poped_name3=name.pop()
print(poped_name3)
print('i am sorry for my mistake')
print(f'Dear {name[0].title()},you are still in the list')
print(f'Dear {name[1].title()},you are still in the list')
print(f'Dear {name[2].title()},you are still in the list')
print(name)
del name[0]
del name[1]
print(name)
del name[0]
print(name)