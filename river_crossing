import heapq
import pprint
def reconstruct_path(path_from,current):
    path = [current]
    while current in path_from:
        current = path_from[current]
        path.append(current)
    return path

def H_cost_estimate(step,goal):
    return sum([sum (x) for x in zip(step,goal)])
def check(step):
    man = 0
    for i in range(3):
        man += step[i*2]
    if (man % 3 == 0):
        return True
    legal = True
    for i in range(3):
        legal = legal and (step[2*i] == step[2*i+1])
    if legal:
        return True
    return False
def move(x):
    if x ==0:
        return 1
    else:
        return 0
def create_onetwostep_move():
    move = []
    for i in range(6):
        for j in range(i,6):
                move.append([i,j])
    return move
def astar(start,goal):
    open_set = []
    close_set = set()
    path_from = {}
    move_onetwo = create_onetwostep_move()
    gscore = {start:0}
    fscore = {start:H_cost_estimate(start,goal)}
    heapq.heappush(open_set,(fscore[start],start))
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(path_from,current)
        close_set.add(current)
        for i, j in move_onetwo:
            next = list(current)
            if not (next[i] == next[6]): continue
            if not (next[j] == next[6]): continue  
            next[i] = move(next[i])
            if i != j:
                next[j] = move(next[j])
            next[6] = move(next[6])
            next = tuple(next)
            if not check(next):
                continue
            if next in close_set:
                continue
            
            next_gscore = gscore[current] + 1
            if next_gscore >= gscore.get(next,999999):
                continue
            path_from[next] = current
            gscore[next] = next_gscore
            fscore[next] = next_gscore + H_cost_estimate(next,goal)
            if next not in [i[1] for i in open_set]:
                heapq.heappush(open_set,(fscore[next],next))
            


                
if __name__ == "__main__":
    start = (0,0,0,0,0,0,0)
    goal = (1,1,1,1,1,1,1)
    path = astar(start,goal)
    path.reverse()
    pp = pprint.PrettyPrinter()
    print ('Total step :%d' % len(path))
    pp.pprint (path)
