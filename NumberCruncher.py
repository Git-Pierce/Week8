import random

def crunch_numbers(data):
    total = 0
    for number in data:
        total += number

    average = round(total/len(data))
    median_index = len(data)//2 # integer division
    median = data[median_index]
    minimum = min(data)
    maximum = max(data)
    dups = get_dups(data)
    print("dups", dups)
    print("Average =", average, "Median =", median)
    print("Min =", minimum, "Max =", maximum, "Dups =", dups)

def get_dups(data):
    dups=[]
    for i in range(len(data)//2):
        count = data.count(i) #counts occurences of i
        print("data.count(i)", data.count(i))
        if count >=2:
            dups.append(i)
    return dups

def main():
    fixed_tuple = (0, 5, 10, 15, 20, 25, 30 ,35)
    random_list = [0] * 11
    for i in range(len(random_list)):
        random_list[i] = random.randint(0, 50)
    random_list.sort()

    print("TUPLE DATA:", fixed_tuple)
    crunch_numbers(fixed_tuple)
    print()
    print("RANDOM DATA:", random_list)
    crunch_numbers(random_list)

main()