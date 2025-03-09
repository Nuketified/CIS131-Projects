

from datetime import datetime

x = datetime.now()

# make some time pass and stuff happen between calls to datetime.now()
# so that x and y have different values
counter = 0 
while counter < 100000:
    counter+=1

y = datetime.now()

print(x)
print(y)

print(x.year, x.month, x.day, x.hour, x.minute, x.second)
print(y.year, y.month, y.day, y.hour, y.minute, y.second)

if x > y:
    print("The first time is larger???")
if x < y:
    print("The second time is larger.")
if x == y :
    print("The time objects are equal.")  

difference = y - x
print(difference)            