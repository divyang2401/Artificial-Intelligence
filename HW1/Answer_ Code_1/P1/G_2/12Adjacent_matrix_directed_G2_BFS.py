#12Adjacent_matrix_directed_G2_BFS: Queue 
from collections import deque
matrix=[[0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0,0,0]]

dic ={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'G','7':'h','8':'p','9':'q','10':'r','11':'s'}
dicp ={'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','G':'6','h':'7','p':'8','q':'9','r':'10','s':'11'}
def replacement(ls):
    counter=0
    ts=[]
    for i in ls:
        if (i>0):
           ts.extend(dic.get(str(counter)))
        counter=counter+1        
    return ts               

def bfssearchings(matrix, start,goal):
    visited= []
    path=[]
    initial =dic.get(str(start))
    end=dic.get(str(goal))
    queue=deque([initial])
    
    while queue:
        vertex= queue.popleft()
        
        if vertex not in visited:        
           path.extend(vertex) 
           visited.extend(vertex)
        temp=replacement(matrix[int(dicp.get(vertex))])
        queue.extend(list(set(temp)-set(path)))
        if end in path:
            return (path,visited)
    return (path,visited)
p=[]
p.extend(bfssearchings(matrix,11,6))
print("path :",p[0])
print("visited nodes:",p[1])

