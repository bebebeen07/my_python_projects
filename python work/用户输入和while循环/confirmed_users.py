#首先，创建一个待验证用户列表
#和一个用于存储以验证用户的空列表
unconfirmed_users=['alice','brain','candance']
confirmed_users=[]
#验证每一个用户，直到没有未验证用户为止
#将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)
#显示所有的已验证用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#删除为特定值的所有列表元素
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#使用用户输入填充字典
responses={}
polling_active=True
while polling_active:
    name=input("What is your name?")
    response=input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("Would you like to let another person to respond?(yes/no)")
    if repeat=='no':
        polling_active=False
print("\n---POLL RESULT---")
for name,response in responses.items():
    print(f"{name} would you like to climb {response}")