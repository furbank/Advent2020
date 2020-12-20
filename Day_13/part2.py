with open("Day_13\input") as f:
    data = f.read().splitlines()

#data = ['939', '7,13,x,x,59,x,31,19']

timetable = [d for d in data[1].split(',')]
[print(t) for t in timetable]

