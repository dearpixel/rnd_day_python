import random

with open('source.txt', 'r') as file:
    for line in file:
        values = line.strip().split(" ")
        time = values[0]
        values.remove(values[0])
        random_value = random.choice(values).replace("_"," ")
        print(time+" "+random_value)