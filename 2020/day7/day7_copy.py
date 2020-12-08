from functools import lru_cache

# Read the data into a graph structure. Yes, regex are awesome, blah blah blah
graph = {}
for line in open("input"):
    name, contents = line.split(" bags contain ")
    contents = [item[:item.find(" bag")] for item in contents.split(", ")]
    if contents[0] == "no other":
        graph[name] = dict()
    else:
        graph[name] = {item[2:]: int(item[0]) for item in contents}

# Part 1 - find all the possible 'parents' of 'shiny gold'
targets = set(["shiny gold", ])
new_parents, all_parents = set(), set()

while len(targets) > 0:
    for target in targets:
        for bag in graph:
            if target in graph[bag] and bag not in all_parents:
                new_parents.add(bag)
    all_parents |= new_parents
    targets, new_parents = new_parents, set()

print("Overall, found", len(all_parents), "parents of 'shiny gold'")

# Part 2 - find how many bags 1 'shiny gold' must contain


@lru_cache(maxsize=None)
def value(bag):
    return sum(graph[bag][child] * (1 + value(child)) for child in graph[bag])


print("The 'shiny gold' bag must contain", value('shiny gold'), "bags")
