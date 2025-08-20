#一个简单的字典
alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])


#使用字典
#访问字典中的值
new_points=alien_0['points']
print(f'You just earned {new_points} points')

#添加键值对
alien_0={'color':'green','points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)


#从创建一个空字典开始
alien_0={}
alien_0['color']='greeen'
alien_0['points']=5

print(alien_0)


#修改字典中的值
alien_0={'color':'green'}
print(f'The alien color is {alien_0["color"].title()}.')
alien_0['color']='yellow'
print(f'The alien color is {alien_0["color"].title()} now.')

#一个有趣的小例子
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f'Original position:{alien_0["x_position"]}')

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    #这个外星人的移动速度肯定很快
    x_increment=3

#新位置为旧位置加上移动距离
alien_0['x_position']=alien_0['x_position']+x_increment

print(f"New position:{alien_0['x_position']}")


#删除键值对
alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['color']
print(alien_0)


#由类似的对象组成的字典
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")


#使用get()来访问值
alien_0={'color':'green','speed':'slow'}

point_value=alien_0.get('points','No point value assigned.')
print(point_value)

#动手试一试
sarah_smiths={'first_name':'sarah','last_name':'smiths','age':18,'city':'chongqing'}
print(f"Sarah's first name is {sarah_smiths['first_name'].title()},and the last name is {sarah_smiths['last_name'].title()}")
print(f"Sarah is living in {sarah_smiths['city']} and she is {sarah_smiths['age']} now")

person_nums={
    'tiffa':6,
    'sebrina':8,
    'vivian':9,
    'john':4,
    'kathy':3,
}
for person_num in person_nums:
    print(f"{person_num.title()}'s favorite number is {person_nums[person_num]}")

vocs={
    '键值对':'键值对应',
    '元组':'固定的',
    '切片':'列表的一段',
    '列表':'列举',
    '遍历':'循环',
}
for voc in vocs:
    print(f"{voc}:{vocs[voc]}\n")
