import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_num = random.randint(0, len(friends) - 1)
print(random_num)
print(friends[random_num])

print(random.choice(friends))

