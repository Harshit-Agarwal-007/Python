names=str(input())
name_split=names.split(", ")
print(name_split)
import random
i=random.randint(0,len(name_split)-1)
print(len(name_split))
print(i)
print(name_split[i])
print(random.choice(name_split))

