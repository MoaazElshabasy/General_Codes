print("Hello Adventurer")
Quit = 0
# x and y are the coordinates
y = 0
x = 0
# c is the number of moves the player made
c = 0
while Quit == 0:
    Move = input("Please Chose Your Next Move: ")
    if Move == 'q' or Move == 'Q':
        Quit = 1
    if Move == 'n' or Move == 'N':
        x += 1
        c += 1
    elif Move == 's' or Move == 'S':
        x -= 1
        c += 1
    elif Move == 'e' or Move == 'E':
        y += 1
        c += 1
    elif Move == 'w' or Move == 'W':
        y -= 1
        c += 1
print(f'( ( {x} , {y} ), {c} )')