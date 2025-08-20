motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

baby_name=[]
baby_name.append('Cherry')
baby_name.append("blueberry".title())
baby_name.insert(0,'Blueberry')
print(baby_name)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles=['honda','yamaha','suzuki']
last_owned=motorcycles.pop()
print(f'the last motorcycle i owned was a {last_owned.title()}'.title())

motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print(f'the first motorcycle i owned was a {first_owned.title()}'.title())

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")