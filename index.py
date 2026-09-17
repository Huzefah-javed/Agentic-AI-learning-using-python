# prompts = [
#     "Write a Next.js component", 
#     "Add Tailwind CSS", 
#     "Connect to MongoDB", 
#     "Fix the WebSocket bug"
# ]

# latest_prompt,  *history  = prompts
# for a,b in enumerate(history):
#     print(f"Context {a} : ",b)

# seasons = [2008, 2014, 2016, 2017]
# goals = [42, 51, 51, 42]

# print(f"highest goal count {max(goals)}")
# print(f"total goal count {sum(goals)}")
# for year, goal in zip(seasons, goals):
#     print(f"In {year}, he scored {goal} goals")


# import copy

# milestones = [
#     ["Design UI", "Completed"],
#     ["Build WebSocket Chat", "Pending"],
#     ["Deploy to Vercel", "Pending"]
# ]

# milestones_backup = copy.deepcopy(milestones)
# milestones_backup[1][1] = "Completed"
# milestones_backup.append(["Client Review", "Pending"])

# print(milestones_backup)
# print(milestones)

a = [1,2,3,4,5,6,7,8,9,10]
condFn = lambda x: x*5

print(list(enumerate(a)))

data = {
    "name":"Huzefa javed",
    "age": 21,
}

print({k:v.upper() for k,v in data.items() if isinstance(v, str)})


data = {1,4,3,5,2,11}
data.discard(5)
print(data)