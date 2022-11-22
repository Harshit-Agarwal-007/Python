user=int(input("0 for rock, 1 for paper, 2 for scissors:  "))
import random


computer=random.randint(0,2)
list1=['rock', "paper", 'scissors']
print(f'you choose {list1[user]}')
print(f' computer chose {list1[computer]}')
list=[user, computer]
if list[0]==list[1]:
    print("once more")
elif list[0]==0 and list[1]==1:
    print("you lost")
elif list[0]==1 and list[1]==2:
    print("you lost")
elif list[0]==2 and list[0]==0:
    print("you lost")
elif list[0]>=3:
    print("invalid output")
else:
    print("you won")

