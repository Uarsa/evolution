import random, os, time


row = col = 20
board = row - 1
a = random.randint(0, board)
b = random.randint(0, board)
#a, b = 5, 5
p = [a, b]
pos = [p]
level = 30

#for i in range(level - 1):
while (level - 1) != 0:
    
    sign = random.randint(0, 1)
    
    if sign == 0:
        index = random.randint(0, 1)
        if index == 0:
            x = p[0] + 1
            if x > board:
                x = p[0] - 1
            p = [x, p[1]]
        else:
            x = p[1] + 1
            if x > board:
                x = p[1] - 1
            p = [p[0], x]
    else:
        index = random.randint(0, 1)
        if index == 0:
            x = p[0] - 1
            if x < 0:
                x = p[0] + 1
            p = [x, p[1]]
        else:
            x = p[1] - 1
            if x < 0:
                x = p[1] + 1
            p = [p[0], x]
            
    if p in pos:
        p = pos[-1]
        continue
    
    level = level - 1    
    pos.append(p)
    
    

for x in range(len(pos)):
    for i in range(row):
        #count = 0
        for j in range(col):
            count = 0
            for z in range(x+1):

                if i == pos[z][0] and j == pos[z][1]:
                    print("⬛", end=" ")
                    count = 1
                    
            if count != 0:
                continue
    
            print(".", end=" ")
        print()
        
        
    time.sleep(0.3)
    if x == len(pos)-1:
        break
    os.system("clear")
    
    
    
