from collections import defaultdict
with open('input') as file:
    dimensions = file.read().splitlines()
    dimensions = [int(x) for x in dimensions]

dist = defaultdict(int)
for mask in range(1, 1 << len(dimensions)):
    p = [d for i, d in enumerate(dimensions) if (mask & (1 << i)) > 0]
    if sum(p) == 150:
        dist[len(p)] += 1

print("total:", sum(dist.values()))
print("min:", dist[min(dist.keys())])
