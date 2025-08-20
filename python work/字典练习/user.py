#遍历所有的键值对
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")


#遍历字典中的所有键
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}

for name in favorite_languages.keys():
    print(name.title())


favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
friends={'edward','sarah'}
for name in favorite_languages.keys():
    print(f"HI {name.title()}")
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language.title()}!")


#遍历字典中所有的值
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


#动手试一试
vocs={
    '键值对':'键值对应',
    '元组':'固定的',
    '切片':'列表的一段',
    '列表':'列举',
    '遍历':'循环',
}
print("The following words have been mentioned:")
for words in vocs.keys():
    print(words)
print("\nThe following values have been mentioned:")
for Values in vocs.values():
    print(Values)

rivers={'nile':'egypt','yellow river':'china','amazon':'brazil'}
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")