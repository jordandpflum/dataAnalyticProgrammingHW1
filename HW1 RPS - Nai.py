import random

total_game = 0
h_win = 0
h_choice = 0
comp_choice = 0
choices = ['rock','paper','scissors']
r = 0
p = 0
s = 0

while h_choice != 'n':

    record = [r,p,s]

    if r == p and r == s and p == s:
        comp_choice = choices[random.randint(0,len(choices)-1)]
        print('random')
    else:
        if max(record) == r and r!=0 and r!=p and r!=s :
            comp_choice = 'paper'
        if max(record) == p and p!=0 and p!=r and p!=s:
            comp_choice = 'scissors'
        if max(record) == s and s!=0 and s!=p and s!=r:
            comp_choice = 'rock'
        if r == p > s:
            comp_choice = 'paper'
        if r == s > p:
            comp_choice = 'rock'
        if s == p > r:
            comp_choice = 'scissors'

    h_choice = input('What is your choice? or press n to exit. ')
    h_choice = h_choice.lower()

    if h_choice not in choices and h_choice != 'n':
        print("Please enter 'rock', 'paper' or 'scissors'")
    else:
        total_game += 1
        if h_choice == comp_choice:
            print ("This round is a draw.")
            print()
        if h_choice == 'rock':
            r += 1
            if comp_choice == 'scissors':
                h_win += 1
        if h_choice == 'paper':
            p += 1
            if comp_choice == 'rock':
                h_win += 1
        if h_choice == 'scissors':
            s += 1
            if comp_choice == 'paper':
                h_win += 1

print('Total games played:',total_game-1)
print('Total games won:', h_win)

