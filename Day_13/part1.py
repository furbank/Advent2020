with open("Day_13\input") as f:
    data = f.read().splitlines()

#data = ['939', '7,13,x,x,59,x,31,19']

eta = int(data[0])
timetable = [int(d) for d in data[1].split(',') if d !='x']

arrivals = {t:t*(eta//t+1) for t in timetable}

nextBusId = min(arrivals, key=arrivals.get)

print('Solution:', nextBusId * (arrivals.get(nextBusId) - eta))

