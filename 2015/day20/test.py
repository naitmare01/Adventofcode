MIN_P = 29000000
N_HOUSES = 30000000

def findIndex(houses):
    for x in range(len(houses)):
        if houses[x] >= MIN_P:
            return x
    return None

# Part 1
houses = [0 for x in range(N_HOUSES + 1)]
for i in range(1, len(houses) // 10):
    for j in range(i, len(houses), i):
        houses[j] += 10*i
houses[0] = -1
print(findIndex(houses))

# Part 2             
houses = [0 for x in range(N_HOUSES + 1)]
for i in range(1, len(houses) // 10):
    total_presents = 0
    for j in range(i, len(houses), i):
        houses[j] += 11*i
        total_presents += 1
        if total_presents == 50:
            break
houses[0] = -1
print(findIndex(houses))  
