
used = set()
def check(four,used):
    eight = four * 2
    appear = used.copy()
    eight = str(eight)
    eight = eight.zfill(5)
    for i in range(len(eight)):
        if int(eight[i]) in appear:
            return False
        appear.add(int(eight[i]))
    return True

def dfs(four,step):
    if step == 4:
        if check(four,used):
            print ('%04d + %04d = %05d' %(four,four,2*four))
        return
    for i in range(10):
        if i in used:
            continue
        used.add(i)
        dfs (four + i *(10 ** step),step + 1)
        used.remove(i)

if __name__ == '__main__':
    dfs (0,0)
