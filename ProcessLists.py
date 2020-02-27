import random

scores = [70, 80, 90, 100]
total = 0
for score in scores:
    total += score
    print("total", total)
print(total)
print("==========================")
scores = [70, 80, 90, 100]
total = 0
i = 0
while i < len(scores):
    total += scores[i]
    i += 1
    print("total while loop:", total)
print(total)

print("========immutable arguments======")
def double_the_number(value):
    value = value * 2  # new int object created
    return value       # new int object must be returned

value1 = 25            # int object created
value2 = double_the_number(value1)
print("value1", value1)          # 25
print("value2", value2)          # 50

value1 = double_the_number(value1)
print("value1", value1)          # 25
#print("value2", value2)          # 50

print("=======sorted list==============")
foodlist = ["orange", "apple", "Pear", "banana"]
sorted_foodlist = sorted(foodlist)
print(sorted_foodlist)# ["Pear", "apple", "banana", "orange"]
sorted_foodlist = sorted(foodlist, key=str.lower)
print(sorted_foodlist)# ["apple", "banana", "orange", "Pear"]

print("==========min and max list===============")
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
minimum = min(numlist)               # 2
maximum = max(numlist)               # 84
print("min num: ", minimum)
print("max num: ", maximum)

print("=============random numbers===============")
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14]
choice = random.choice(numlist) # gets random item
print("choice:", choice)
random.shuffle(numlist)         # shuffles items randomly
print("numlist:", numlist)