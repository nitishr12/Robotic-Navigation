import numpy
#Algorithm
#    Check for the number of possible states. Ensure that chosen state is not in useless. Choose the one with the least heuristic and add the remaining to the discovered state
#    Make the chosen as visited state
#    if val is 2, 
#        check if one of the neighbours were already marked as a warning. 
#        If yes, go to that node
#        else
#            check if there is atleast one discovered node, if no, exit the program with no solution
#            else
#                mark its neighbours as warnings and backtrack to the recent discovered node
#                as you backtrack, add them to the useless node
#1. visited - As you go, add
#2. discovered - Other Possible ways
#3. warning nodes- dangerous crossings
#4. useless - backtracked nodes
state=[
    [0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0], #1
    [0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1], #2
    [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0], #3
    [0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,0],
    [0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0],
    [1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],
    [0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1],
    [0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
    [0,1,1,0,0,0,0,1,0,1,1,1,0,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0],
    [0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,1],
    [0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],
    [0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1],
    [0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0]]

x = 16
y = 0
dest_x = 0
dest_y = 16
visited=[(x,y)]
discovered=[]
warning=[]
useless=[]
i=-1
def getStates(x,y,state):
    best=[]
    if(x+1<17) and (x+1,y) not in visited and (x+1,y) not in useless:
        if state[x+1][y]==0:
            best.append(((x+1,y),abs(x+1-dest_x)+abs(y-dest_y))) 
    if(x-1>=0) and (x-1,y) not in visited and (x-1,y) not in useless:
        if state[x-1][y]==0:
            best.append(((x-1,y),abs(x-1-dest_x)+abs(y-dest_y)))
    if(y-1>=0 ) and (x,y-1) not in visited and (x,y-1) not in useless:
        if state[x][y-1]==0:
            best.append(((x,y-1),abs(x-dest_x)+abs(y-1-dest_y)))
    if(y+1<17 ) and (x,y+1) not in visited and (x,y+1) not in useless:
        if state[x][y+1]==0:
            best.append(((x,y+1),abs(x-dest_x)+abs(y+1-dest_y)))
    return best

def bestState(x,y,state):
    best=getStates(x, y, state)
    if(len(best)>0):
        best.sort(key=lambda l:l[1], reverse=True)
        best_x,best_y=best.pop()[0]
        best.sort(key=lambda l:l[1], reverse=False)
        while (len(best)>0):
            discovered.append(best.pop()[0])
        return (best_x,best_y)
    else:
        return (0,0)
flag=True
while (x != dest_x or y != dest_y):
    x,y=bestState(x, y, state)
    #print(x,y)
    #if((8,13) in visited):
        #print ("Print",discovered[len(discovered)-1])
    #Keep visiting the new states until it gets stuck
    if (x,y) != (0,0):
        visited.append((x,y))
    #If there are no ways of getting forward, backtrack to the recent discovered node
    else:
        #useless.append((x,y))
        near_x,near_y=discovered.pop()
        loop=True
        iterator=len(visited)-1
        while(loop):
            
            old_x,old_y=visited[iterator]
            #print("Looking for",near_x,near_y)
            #if((7,12) not in discovered):
                #print("True",old_x,old_y)
            #print(old_x,old_y)
            if abs(old_x-near_x)+abs(old_y-near_y)<=1:
                x,y=near_x,near_y
                visited.append((x,y))
                #useless.append((old_x,old_y))
                loop=False
                #discovered.pop()
            else:
                visited.pop()
                iterator=iterator-1
                useless.append((old_x,old_y))
    

print(visited)
print (x,y)