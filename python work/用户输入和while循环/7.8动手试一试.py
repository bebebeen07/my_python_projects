#熟食店

sandwich_orders = ['aaa', 'bbb', 'ccc']
finished_sandwiches = []
 
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
 
print(f"\nfinished_sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


sandwich_orders=['tomato','potato','chicken']
finished_sandwich=[]
for sandwich_order in sandwich_orders:
    print(f"I made you a {sandwich_order} sandwich.")
    sandwich1=sandwich_orders.pop()
    finished_sandwich.append(sandwich1)

print("Here are all finished sandwichs:")

for finished_sandwichs in finished_sandwich:
    print(f"These is {finished_sandwichs} sandwich")
