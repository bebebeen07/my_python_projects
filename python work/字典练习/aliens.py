#字典列表
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


#创建一个用于存储外星人的列表
aliens=[]

#创建30个绿色外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    if alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#在字典中存储列表
#存储顾客所点pizza的信息
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
#概述顾客点的pizza
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

#在字典中存储字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'eindstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']

    print(f"\tFull_name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")


#动手试一试
ElonMusk= {'first_name':'Elon', 'last_name':'Musk', 'age':'53', 'city':'Pretoria'}
MaYun= {'first_name':'Yun', 'last_name':'Ma', 'age':'60', 'city':'HangZhou'}
WangChuanfu= {'first_name':'Chuanfu', 'last_name':'Wang', 'age':'58', 'city':'ShenZhen'}
nams=[ElonMusk,MaYun,WangChuanfu]
for nam in nams:
    print(nam)

favorite_places = {
    'feifei':['Beijing', 'SuZhou'],
    'Bob':['ShangHai','HangZhou', 'ShenZhen'],
    'huahua':['Chengdu', 'ChongQing'],
}
for k,v in favorite_places.items():
    print(f"\n{k.title()}'s favorite places are:")
    for fp_v in v:
        print(fp_v)